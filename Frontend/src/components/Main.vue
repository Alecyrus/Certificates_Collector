<template>
  <div >
    <div >
      <vue-particles class="background"  shapeType="circle" :particleOpacity="0.4" :particlesNumber="100" linesColor="#85004B" color="#85004B"></vue-particles>
    </div>

    <Affix>
      <Menu style="opacity:0.8;box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .05), 0px 0px 8px 0px rgba(0, 0, 0, .04);" ref="mainMenu" mode="horizontal" theme="light" :active-name="activeMenu" @on-select="handleMenuSelect">
        <div class="layout-logo"></div>
        <div class="layout-nav">
          <MenuItem name="/">                   
            首页
          </MenuItem>
          <MenuItem name="/certificatescollector">
            最新采集结果
          </MenuItem>
        </div>
      </Menu>

    </Affix>

    <div class="layout-content">

      <transition name="component-fade" mode="out-in">
        <router-view></router-view>
      </transition>
    </div>
    <BackTop></BackTop>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        activeMenu: '',

      }
    },
    methods: {
      handleMenuSelect() {
         this.$router.push(arguments[0]);
      }

    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .layout-logo{
    width: 6.1em;
    height: 2em;
    background-color: #85004B;
    opacity:0.8;
    border-radius: 0.18em;
    float: left;
    position: relative;
    top: 15px;
    left: 20px;
/*    -webkit-filter: blur(20px);
    -moz-filter: blur(2px);
    -ms-filter: blur(2px);
    -o-filter: blur(2px);
    filter: blur(15px);    */
  }
    .background {
        position: fixed;
        right:0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        height: auto;
        overflow:hidden;
        -webkit-filter:blur(7px);
        filter:blur(7px);
        width: auto;
    } 
  .layout-logo-in {
    z-index: 999;
  }

  .layout-nav{
    width: 20em;
    margin: 0 auto;
    float: right;
    position: relative;
  }

  .layout-content {
    min-height: 600px;
    margin: 15px;
    overflow: hidden;
    border-radius: 4px;
  }
</style>
