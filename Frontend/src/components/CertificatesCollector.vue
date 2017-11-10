<template>
  <div>

<Affix :offset-top="75">
 <Row style="background: transparent;margin-top:3.5em;" type="flex" justify="start">
        <Col span="8" :offset="3" align="left">
        <p style="font-size:2.5em;">采集结果</p>
        </Col>
        </Row>

</Affix>


 <Row style="background: transparent;margin-top:2em;" type="flex" justify="center">
        <Col span="6"  align="middle">
        <Affix :offset-top="185">
          <Menu :open-names="['2']" @on-select="handleSelect" style="background: transparent;" >          
            <MenuItem name="0"><Icon type="key"></Icon> 数字证书</MenuItem>
            <Submenu name="2">
              <template slot="title">
                <Icon type="lock-combination"></Icon>
                证书链
              </template>


              <MenuItem v-for="(certificate, index) in certificates.certificates_chain" :name="index+1"><Icon type="link"></Icon> 证书{{index+1}}</MenuItem>
            </Submenu>
          </Menu>
          
        </Affix>
            
        </Col>
        <Col span="14" >
          <certificate :certificate="certificate">
          </certificate>
        </Col>
    </Row>
  </div>
</template>

<script>
import Cert from '@/components/Cert'
export default {
  data() {
    return {
      certificates:{},
      certificate:{}

    };
  },
  mounted() {
    this.certificates = this.$ls.get('certificates', []);
    this.certificate = this.certificates.certificate
  },
  components:{
    'certificate': Cert
  },
  methods: {
    handleSelect() {
      if (arguments[0] == 0) {
        this.certificate = this.certificates.certificate;
      }
      else {
        this.certificate = this.certificates.certificates_chain[arguments[0]-1];

      }
    }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
