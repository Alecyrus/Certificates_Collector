import re
import arrow
import logging
import cryptography

from sanic import Sanic
from sanic.response import json
from sanic.exceptions import ServerError
from OpenSSL import SSL
from datetime import datetime
from socket import socket


DEFAULT_TIME = 5
DEFAULT_PORT = 443

app = Sanic()
app.config.REQUEST_TIMEOUT = 4


def b2s(b):
    return str(b, encoding = "utf-8")

def handle_tuple(issues):
    res = ""
    for issue in issues:
        res += "%s=%s, " %(b2s(issue[0]), b2s(issue[1]))
    return res

def get_extentions(cert):
    index = cert.get_extension_count()
    exts = dict()
    for i in range(index):
        try:
            if b2s(cert.get_extension(i).get_short_name()) != "UNDEF":
                exts[b2s(cert.get_extension(i).get_short_name())] = cert.get_extension(i).__str__().replace('\n', '<br>')
        except Exception as e:
            pass
    return exts

def handle_time(anc_time):
    time = arrow.get(datetime(int(anc_time[:-1][:4]),
                              int(anc_time[:-1][4:6]),
                              int(anc_time[:-1][6:8]),
                              int(anc_time[:-1][8:10]),
                              int(anc_time[:-1][10:12]),
                              int(anc_time[:-1][12:14])))
    return time.format('YYYY-MM-DD HH:mm:ss ZZ')
    

def parse_certs(certificates, certs=None):
    for cert in certificates: 
        try:
            temp = dict()
            temp['version'] = cert.get_version()
            temp['serial_number'] = hex(cert.get_serial_number())
            temp['signature_algorithm'] = b2s(cert.get_signature_algorithm())
            temp['issuer'] = handle_tuple(cert.get_issuer().get_components())
            temp['validity'] = {"notBefore": handle_time(b2s(cert.get_notBefore())), 
                            "notAfter": handle_time(b2s(cert.get_notAfter()))}
            temp['subject'] = handle_tuple(cert.get_subject().get_components())
            temp['expired'] = cert.has_expired()
            temp['digest'] = {
                     "algorithm":"sha1",
                     "content":b2s(cert.digest("sha1"))
                     }
            temp['public_key'] = cert.get_pubkey().to_cryptography_key().public_bytes(cryptography.hazmat.primitives.serialization.Encoding.PEM, \
 cryptography.hazmat.primitives.serialization.PublicFormat.PKCS1)
            temp['extentions'] = get_extentions(cert)
        except Exception as e:
            logging.exception(e)
        finally:
            if certs is not None:
                certs.append(temp)
            else:
                return temp
        
        

def get_certs(ip):
    certs = list()
    temp = list()
    try:
        ssl_context = SSL.Context(SSL.SSLv23_METHOD)
        ssl_context.set_timeout(DEFAULT_TIME)
        s_socket = socket()
        s_socket.connect((ip, DEFAULT_PORT))
        conn = SSL.Connection(ssl_context, s_socket)
        conn.set_connect_state()
        conn.do_handshake()
        cert = parse_certs([conn.get_peer_certificate()])
        parse_certs(conn.get_peer_cert_chain(), certs)
    except Exception as e:
        logging.exception(e)
    finally:
        return certs, cert   
    
    
@app.get("/v1/certificates")
async def test(request):
    try:
        params = request.args['target'][0]
        j_ip=re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')   
        regex = re.compile(
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if not j_ip.match(params) and not regex.match(params):
            raise
        certs_chain, cert = get_certs(params)
    except Exception as e:
        logging.exception(e)
        raise ServerError("Invlid request", status_code=500)
    return json({
            "certificates_chain": certs_chain,
            "certificate": cert
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8182, workers=4,request_timeout=)

