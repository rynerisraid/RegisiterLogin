<template>
<div>

  <el-card class="box-card">
    <el-row type="flex" justify="left">
      <el-col :span="24">
        <el-form
          label-position="left"
          label-width="80px"
          :model="formLogin"
          :rules="rules"
          ref="formLogin">
          <!-- $refs 只在组件渲染完成后才填充，并且它是非响应式的。它仅仅作为一个直接访问子组件的应急方案——应当避免在模版或计算属性中使用 $refs 。 -->
          <el-form-item label="账号" prop="name">
            <el-input v-model="formLogin.name"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input type="password" v-model="formLogin.password"></el-input>
          </el-form-item>
          <!--
          <el-form-item label="确认密码" prop="checkPassword">
            <el-input v-model="formLogin.checkPassword"></el-input>
          </el-form-item>
          -->
          <el-form-item>
              <el-button type="primary" @click="login">登录</el-button>
              <el-button @click="resetForm">取消</el-button>
          </el-form-item>

        </el-form>
      </el-col>
    </el-row>
  </el-card>
  <el-dialog title="验证码" :visible.sync="dialogFormVisible">
    <el-form :model="form">
      <el-form-item label="请输入验证码" :label-width="formLabelWidth">
        <el-input v-model="form.veritifyCode" autocomplete="off"></el-input>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button type="primary" @click="formVeritifyCode">确 定</el-button>
      <el-button @click="dialogFormVisible = false">取 消</el-button>
    </div>
  </el-dialog>
</div>
</template>

<script>
import {mapActions} from 'vuex';
import axios from 'axios';
import { JSEncrypt } from "jsencrypt";

export default {
  name: "Login",
  data() {
    let checkUserName = (rule,value,cb)=>{
      if(!value){
          return cb(new Error('账户不能为空!'))
        }else{
          cb(); // 将判断传递给后面
        }
      }
    let checkPassword = (rule,value,cb)=>{
        if(!value){
          return cb(new Error('密码不能为空!'))
         }else{
          cb();
         }
      }
    let checkPasswordAgain = (rule,value,cb)=>{
        if(!value){
          return cb(new Error('再次输入密码不能为空!'))
         }else if(value !== this.formLogin.password){
          return cb(new Error('两次输入密码不一致!'));
         }else{
          cb();
         }
      }



      return{
        formLogin:{
          name: '',
          password: '',
          checkPassword: ''
        },

        dialogFormVisible: false,

        beforelogin :'',

        formLabelWidth:'30%',

        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        },
        //formLabelWidth: '50%',

        rules:{
          name:[
            {validator:checkUserName,trigger: 'blur'}
          ],
          password:[
            {validator:checkPassword,trigger: 'blur'}
          ],
          checkPassword:[
            {validator:checkPasswordAgain,trigger: 'blur'}
          ]
        },


      }
    },
    methods:{
      ...mapActions(['userLogin']),


      // 向登录接口发起请求
      /*
      login(){
        let user = this.formLogin;

        let formData = {
          username: user.name,
          password: user.password
        };
        const path = `http://localhost:5000/login`;
        axios.post(path,{username:user.name,state_type:"beforelogin"}).then((res)=>{
          window.console.log(res.data);
          if(res.data.status=="invalid user"){
            this.$notify.error("用户名或密码无效") //invalid user
            return;
          }else if(res.data.status=="invalid pwd"){
            this.$notify.error("用户名或密码无效") //invalid password
            return;
          }

          let encrypt = new JSEncrypt();
          encrypt.setPublicKey(res.data);
          let result = encrypt.encrypt(JSON.stringify(formData.password));
          window.console.log(result.length);

          axios.post(path,{username:formData.username, logindata:result,state_type:"logging"}).then((res2)=>{
            window.console.log(res2.data.success);
            if (res2.data.status=='success') {
              this.$notify.success(`${res2.data.status}`)
              // 登录成功 跳转至首页
              // this.$router.push({name:'Home'})
              this.$router.push('/books')
            }else{
              this.$notify.error({title: '错误', message: '登录失败！'});
            }

        })


        })

      },
      */

      // 向登录接口发起请求 加入验证码弹窗功能
      login(){

        let user = this.formLogin;


        /*
        let formData = {
          username: user.name,
          password: user.password
        };
        */
        const path = `http://localhost:5000/login`;
        axios.post(path,{username:user.name,state_type:"beforelogin"}).then((res)=>{
          window.console.log(res.data);
          this.beforelogin = res.data;
          if(res.data.status=="invalid user"){
            this.$notify.error("用户名或密码无效") //invalid user
            return;
          }else if(res.data.status=="invalid pwd"){
            this.$notify.error("用户名或密码无效") //invalid password
            return;
          }
          this.dialogFormVisible = true;

          /*
          axios.post(path,{username:formData.username, logindata:result,state_type:"logging"}).then((res2)=>{
            window.console.log(res2.data.success);
            if (res2.data.status=='success') {
              this.$notify.success(`${res2.data.status}`)
              // 登录成功 跳转至首页
              // this.$router.push({name:'Home'})
              this.$router.push('/books')
            }else{
              this.$notify.error({title: '错误', message: '登录失败！'});
            }

          });
          */
        })
        /*
        axios.post(path,formData).then((res) => {
          if(res.data.status=='success'){
            this.$message.success(`${res.data.status}`)
            this.$router.push('/books')
          }
          this.message = 'Login！';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.message = 'ERROR！';
        });
        */

        // 表单验证
        /*
        this.$refs['formLogin'].validate((valid) => {
          if (valid) {
            // 通过验证之后才请求登录接口
            console("提交登录表单")
            this.$http.post('localhost:5000/login',formData)
                .then(res => {
                    console.dir(res.data)
                    if (res.data.success) {
                      this.userLogin(res.data);
                      this.$message.success(`${res.data.message}`)
                      // 登录成功 跳转至首页
                      // this.$router.push({name:'Home'})
                      this.$router.push('/')
                    }else{
                      this.$message.error(`${res.data.message}`);
                      return false;
                    }
                })
                .catch(err => {
                    this.$message.error(`${err.message}`, 'ERROR!')
                })
          } else {
            this.$message.error('表单验证失败!')
            return false;
          }
        });*/
      },
      // 表单重置
      resetForm(){
        console.log('session')
        this.$refs['formLogin'].resetFields();
      },

      formVeritifyCode(){
        const path = `http://localhost:5000/login`;
        this.dialogFormVisible = true;
        window.console.log("formVeritifyCode");
        let encrypt = new JSEncrypt();
        encrypt.setPublicKey(this.beforelogin);

        let result = encrypt.encrypt(JSON.stringify(this.formLogin.password+"||||"+this.form.veritifyCode));

        window.console.log(result);



        axios.post(path,{username:this.formLogin.name, logindata:result,state_type:"logging"}).then((res)=>{
            window.console.log(res.data.success);
            if (res.data.status=='success') {
              this.$notify.success(`${res.data.status}`)
              // 登录成功 跳转至首页
              // this.$router.push({name:'Home'})
              this.$router.push('/books')
            }else{
              this.$notify.error({title: '错误', message: '登录失败！'});
            }

          });

      }
    }


};
</script>


<style scoped>

</style>