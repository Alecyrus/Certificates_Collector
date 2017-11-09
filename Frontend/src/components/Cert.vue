<template>
  <div>

    <Row align="middle" style="background: transparent;margin-top:0em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:2em;">证书详情</p>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="21" align="left">
        <p style="font-size:1.5em;">版本</p>
      </Col>
      <Col span="4" align="left">
        <p style="font-size:1.5em;"><Tag>X509 v{{certificate.version}}</Tag></p>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="21" align="left">
        <p style="font-size:1.5em;">序列号</p>
      </Col>
      <Col span="4" align="left">
        <p style="font-size:1.5em;"><Tag>{{certificate.serial_number}}</Tag></p>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="21" align="left">
        <p style="font-size:1.5em;">签名算法</p>
      </Col>
      <Col span="4" align="left">
        <p style="font-size:1.5em;"><Tag>{{certificate.signature_algorithm}}</Tag></p>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="21" align="left">
        <p style="font-size:1.5em;">有效期</p>
      </Col>
      <Col span="12" align="left">
        <p style="font-size:1.5em;"><Tag>{{certificate.validity.notBefore}} </Tag>至 <Tag> {{ certificate.validity.notAfter}} </Tag></p>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="21" align="left">
        <p style="font-size:1.5em;">使用者</p>
      </Col>
      <Col span="21" align="left">
        <p style="font-size:1.5em;"><Tag>{{certificate.subject}}</Tag></p>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="21" align="left">
        <p style="font-size:1.5em;">颁发者</p>
      </Col>
      <Col span="21" align="left">
        <p style="font-size:1.5em;"><Tag>{{certificate.issuer}}</Tag></p>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">公钥</p>
      </Col>
      <Col span="21" align="left">
        <p style="font-size:1em;">{{certificate.public_key}}</p>
      </Col>
    </Row>
        <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">授权信息访问</p>
      </Col>
      <Col span="21" align="left">
      <p style="font-size:1.5em;"><Tag>{{certificate.extentions.authorityInfoAccess}}</Tag></p>
      </Col>
    </Row>
        <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">证书策略</p>
      </Col>
      <Col span="21" align="left">
      <p style="font-size:1.5em;"><Tag>{{certificate.extentions.certificatePolicies}}</Tag></p>
      </Col>
      </Row>
        <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">基本约束</p>
      </Col>
      <Col span="21" align="left">
      <p style="font-size:1.5em;"><Tag>{{certificate.extentions.basicConstraints}}</Tag></p>
      </Col>
      </Row>
        <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">使用者可选名称</p>
      </Col>
      <Col span="21" align="left">
      <p style="font-size:1.5em;"><Tag>{{certificate.extentions.subjectAltName}}</Tag></p>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">增强型密钥算法</p>
      </Col>
      <Col span="21" align="left">
      <p style="font-size:1.5em;"><Tag>{{certificate.extentions.extendedKeyUsage}}</Tag></p>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">使用者密钥标识符</p>
      </Col>
      <Col span="21" align="left">
      <p style="font-size:1.5em;"><Tag>{{certificate.extentions.extendedKeyUsage}}</Tag></p>
      </Col>
    </Row>

    <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">授权密钥标识符</p>
      </Col>
      <Col span="21" align="left">
      <p style="font-size:1.5em;"><Tag>{{certificate.extentions.authorityInfoAccess}}</Tag></p>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">密钥用法</p>
      </Col>
      <Col span="21" align="left">
      <p style="font-size:1.5em;"><Tag>{{certificate.extentions.keyUsage}}</Tag></p>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">指纹算法</p>
      </Col>
      <Col span="21" align="left">
      <p style="font-size:1.5em;"><Tag>{{certificate.digest.algorithm}}</Tag></p>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">指纹</p>
      </Col>
      <Col span="21" align="left">
      <p style="font-size:1.5em;"><Tag>{{certificate.digest.content}}</Tag></p>
      </Col>
    </Row>
  </div>
</template>

<script>
export default {
  props:['certificate'],
  data() {
    return {

    };
  },
  methods: {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
