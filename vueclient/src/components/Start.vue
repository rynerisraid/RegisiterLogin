<template>
  <div class="container">
    <div class="row clearfix">
      <div class="col-md-12 column">
        <div class="row clearfix">
          <div class="col-md-6 column">
            <img alt="Vue logo" src="../assets/logo.png">
          </div>
          <div class="col-md-6 column">
            <div id="dynamic-component-demo" class="demo">
              <el-tabs v-model="activeName" > <!--@tab-click="handleClick"-->
                <el-tab-pane label="登录" name="first">
                  <Login>
                    登录
                  </Login>
                </el-tab-pane>
                <el-tab-pane label="注册" name="second">
                  <Register>
                    注册
                  </Register>
                </el-tab-pane>
              </el-tabs>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
  <!--
<div>
  <img alt="Vue logo" src="../assets/logo.png">
  <div id="dynamic-component-demo" class="demo">
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="登录" name="first">

      </el-tab-pane>
      <el-tab-pane label="注册" name="second">
        <Register>
          注册
        </Register>
      </el-tab-pane>
    </el-tabs>
  </div>
</div>
-->
</template>

<script>
import Register from "@/components/userinfo/Register";
import Login from "@/components/userinfo/Login";
export default {
  name: "Start",

  components:{
    Register,
    Login,
  },
  data(){
    return {
      activeName: 'first',
    };
  },

}
</script>

<style scoped>

</style>