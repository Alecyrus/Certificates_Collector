<template>
  <div>

    <Row align="middle" style="background: transparent;margin-top:0em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:2em;">证书详情</p>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:2em;" type="flex" justify="start">
      <Col span="21" align="left">
        <p style="font-size:1.5em;">版本</p>

      </Col>
      <Col span="10" align="left">
       <Card style="background: transparent;">
        <p style="font-size:1.5em;"> <Tag>X509.V{{certificate.version}}</Tag></p>
      </Card>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1.5em;" type="flex" justify="start">
      <Col span="21" align="left">
        <p style="font-size:1.5em;">序列号</p>
      </Col>
      <Col span="10" align="left">
      <Card style="background: transparent;">
        <div style="font-size:1em;" v-html="certificate.serial_number.substring(2)"></div>
      </Card>
      
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1.5em;" type="flex" justify="start">
      <Col span="21" align="left">
        <p style="font-size:1.5em;">签名算法</p>
      </Col>
      <Col span="10" align="left">
      <Card style="background: transparent;">
        <div style="font-size:1em;" v-html="certificate.signature_algorithm"></div>
      </Card>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1.5em;" type="flex" justify="start">
      <Col span="21" align="left">
        <p style="font-size:1.5em;">有效期</p>
      </Col>
      <Col span="12" align="left">
        <Card style="background: transparent;">
            <p style="font-size:1em;"><Tag>{{certificate.validity.notBefore}} </Tag>至 <Tag> {{ certificate.validity.notAfter}} </Tag></p>
        </Card>
        
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1.5em;" type="flex" justify="start">
      <Col span="21" align="left">
        <p style="font-size:1.5em;">使用者</p>
      </Col>
      <Col span="21" align="left">
      <Card style="background: transparent;">
        <div style="font-size:1em;" v-html="certificate.subject"></div>
      </Card>
      
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1.5em;" type="flex" justify="start">
      <Col span="21" align="left">
        <p style="font-size:1.5em;">颁发者</p>
      </Col>
      <Col span="21" align="left">
      <Card style="background: transparent;">
        <div style="font-size:1em;" v-html="certificate.issuer"></div>
      </Card>
      
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1.5em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">公钥</p>
      </Col>
      <Col span="21" align="left">

      <Card style="background: transparent;">
        <div style="font-size:1em;" v-html="certificate.public_key"></div>
      </Card>
        
      </Col>
    </Row>
        <Row  align="middle" style="background: transparent;margin-top:1.5em;" type="flex" justify="start">
      <Col span="4" align="left">

        <p style="font-size:1.5em;">授权信息访问</p>
      </Col>
      <Col span="21" align="left">
      <Card style="background: transparent;"> 
        <div style="font-size:1em;" v-html="certificate.extentions.authorityInfoAccess"></div>
      </Card>
      
      </Col>
    </Row>
        <Row  align="middle" style="background: transparent;margin-top:1.5em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">证书策略</p>
      </Col>
      <Col span="21" align="left">
      <Card style="background: transparent;">
        <div style="font-size:1em;" v-html="certificate.extentions.certificatePolicies"></div>
      </Card>
      </Col>
      </Row>
        <Row  align="middle" style="background: transparent;margin-top:1.5em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">基本约束</p>
      </Col>
      <Col span="21" align="left">
      <Card style="background: transparent;">
        <div style="font-size:1em;" v-html="certificate.extentions.basicConstraints"></div>
      </Card>
      </Col>
      </Row>
        <Row  align="middle" style="background: transparent;margin-top:1.5em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">使用者可选名称</p>
      </Col>
      <Col span="21" align="left">
      <Card style="background: transparent;">
        <div style="font-size:1em;" v-html="certificate.extentions.subjectAltName"></div>
      </Card>
     
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1.5em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">增强型密钥算法</p>
      </Col>
      <Col span="21" align="left">
      <Card style="background: transparent;">
        <div style="font-size:1em;" v-html="certificate.extentions.extendedKeyUsage"></div>
      </Card>
      
      </Col>
    </Row>

    <Row  align="middle" style="background: transparent;margin-top:1.5em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">授权密钥标识符</p>
      </Col>
      <Col span="21" align="left">
            <Card>
        <div style="font-size:1em;" v-html="certificate.extentions.authorityInfoAccess"></div>
      </Card>
      
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1.5em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">密钥用法</p>
      </Col>
      <Col span="21" align="left">
      <Card>
        <div style="font-size:1em;" v-html="certificate.extentions.keyUsage"></div>
      </Card>
     
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1.5em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">指纹算法</p>
      </Col>
      <Col span="21" align="left">
       <Card>
        <div style="font-size:1em;" v-html="certificate.digest.algorithm"></div>
      </Card>
      </Col>
    </Row>
    <Row  align="middle" style="background: transparent;margin-top:1.5em;" type="flex" justify="start">
      <Col span="4" align="left">
        <p style="font-size:1.5em;">指纹</p>
      </Col>
      <Col span="21" align="left">
      <Card>
        <div style="font-size:1em;" v-html="certificate.digest.content"></div>
      </Card>
     
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
