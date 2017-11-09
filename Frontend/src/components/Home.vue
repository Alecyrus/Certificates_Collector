<template>
  <div>

<Row type="flex"  justify="center" >

      <Col :span="20" >
          <Alert closable show-icon>
        输入网址或者ip，示例输入：www.xxx.com, 202.123.13.23,...。输入网址时，不要添加http，https等协议前缀。
    </Alert>

      </Col>
      </Row>

    <Row type="flex"  justify="center" >

      <Col :xs="12" :sm="8" :md="6" :lg="6" :xl="6">

<Card  class="inputCard" :padding="0" style="background: transparent;">
          <p slot="title" style="font-size:1.3em;font-weight:normal">
            数字证书采集实现Demo
          </p>
        
          <Row   type="flex" justify="center">
            <Col :span="18" >

    <Form class="inputForm" ref="formInline" :model="formInline" :rules="ruleInline" inline>
        <FormItem prop="ip">
            <Input type="text" style="width: 200px;margin-top:2em" @keyup.enter.native="submitForm('inputForm')" v-model="formInline.ip" placeholder="IP地址或网址">
            </Input>
        </FormItem>
          <FormItem>
            <Button type="primary" @click="handleSubmit('formInline')">采集</Button>
        </FormItem>

        </Form>
            </Col>
          </Row>
        </Card>
      </Col>
    </Row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formInline: {
        ip: '',
      },
      ruleInline: {
        ip: [
        { required: true, message: '此项不能为空', trigger: 'blur' }
        ],
      }
    };
  },
  methods: {
    handleSubmit(name) {
      this.$Loading.start();
      this.$refs[name].validate((valid) => {
        if (valid) {
          this.$Message.loading('开始采集');
          this.$request.get('/api/v1/certificates?target='+this.formInline.ip)
          .then((response) => {
            if (response.data.certificates_chain.length > 0){
              this.$ls.set('certificates', response.data, 60 * 60 * 1000);
              this.$Message.info({
                content: '采集成功',
                closable: true
              });

              this.$router.push('/certificatescollector');
              this.$Loading.finish();

            }
            else {
              this.$Message.info('采集为空，目标服务器未提供服务器证书');
              this.$Loading.finish();
            }

          })
          .catch((error) => {
            this.$Message.error('请检查输入是否正确');
            console.log(error);
            this.$Loading.error();
          });

        } else {
          this.$Message.error('无效输入');
          this.$Loading.error();
        }
      })
    }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.inputCard {
  margin-top: 10em;
  box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .10), 0px 0px 12px 0px rgba(0, 0, 0, .04)
}

.inputForm {
    margin:30px 20px 0px 20px;
}
</style>
