<template>
<div>
  <el-card class="box-card">
    <el-row type="flex" justify="left">
      <el-col :span="24">
        <el-form
          label-position="left"
          label-width="80px"
          :model="formRegister"
          :rules="rules"
          ref="formRegister">
          <!-- $refs 只在组件渲染完成后才填充，并且它是非响应式的。它仅仅作为一个直接访问子组件的应急方案——应当避免在模版或计算属性中使用 $refs 。 -->
          <el-form-item label="账号" prop="name">
            <el-input v-model="formRegister.name"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input type="password" v-model="formRegister.password"></el-input>
          </el-form-item>

          <el-form-item label="确认密码" prop="checkPassword">
            <el-input type="password" v-model="formRegister.checkPassword"></el-input>
          </el-form-item>
          <el-form-item label="手机号码" prop="phoneNumber">
            <el-input v-model="formRegister.phoneNumber"></el-input>
          </el-form-item>
          <el-form-item label="验证码" prop="veritifyCode">
            <el-input v-model="formRegister.veritifyCode"></el-input>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="SendSMS">发送短信</el-button>
            <el-button type="primary" @click="Register">创建</el-button>
            <el-button @click="resetForm">取消</el-button>
          </el-form-item>

        </el-form>
      </el-col>
    </el-row>
  </el-card>
</div>
</template>

<script>
import {mapActions} from 'vuex';
import axios from "axios";
import { JSEncrypt } from "jsencrypt";

export default {
  name: "Register",
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
         }else if(value !== this.formRegister.password){
          return cb(new Error('两次输入密码不一致!'));
         }else{
          cb();
         }
      }
      return{
        formRegister:{
          name: '',
          password: '',
          checkPassword: '',
          phoneNumber:'',
          veritifyCode:''
        },
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
        }
      }
    },
    methods:{
      ...mapActions(['userRegister']),
      // 向注册接口发起请求
      /*
      Register(){
        let user = this.formRegister;
        let formData = {
          username: user.name,
          password: user.password,
          phone_number:user.phoneNumber,
          veritify_code: user.veritifyCode,
          state_type:"register info"
        };
        // 表单验证
        this.$refs['formRegister'].validate((valid) => {
          if (valid) {
            // 通过验证之后才请求登录接口
            window.console.log(formData)
            axios.post('http://localhost:5000/register',formData)
                .then(res => {
                    if (res.data.status=='success') {

                      this.$message.success(`注册结果：${res.data.status}`)
                      // 登录成功 跳转至首页
                      // this.$router.push({name:'Home'})
                      this.resetForm()
                    }else{
                      this.$message.error(`注册结果：$${res.data.status}`);
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
        });
      },
      */
      // 向注册接口发起请求：加密版

      Register(){
        let user = this.formRegister;

        let formData = {
          username: user.name,
          password: user.password,
          phone_number:user.phoneNumber,
          veritify_code: user.veritifyCode
        };
        // 表单验证
        const path = 'http://localhost:5000/register';
        let encrypt = new JSEncrypt();
        axios.post(path,{username:formData.username,state_type:"before register"}).then((res)=> {
          window.console.log(res.data);

          encrypt.setPublicKey(res.data);
          let result = encrypt.encrypt(JSON.stringify(formData.password+"||||"+formData.veritify_code));
          window.console.log({username:formData.username, registerdata:result,state_type:"register info"});


          axios.post(path, {username:formData.username, phone_number:formData.phone_number,registerdata:result,state_type:"register info"})
              .then((res2)=>{
            window.console.log(res2.data);
            if(res2.data.status=='success'){
              this.$message.success(`注册结果：${res2.data.status}`);
            }else{
              this.$message.error(`注册结果：${res2.data.status}`);
            }
          })

        }).catch(err => {
          this.$message.error(`${err.message}`, 'ERROR!')
        })


      },

      // 表单重置
      resetForm(){
        console.log('session')
        this.$refs['formRegister'].resetFields();
      },

      SendSMS(){
        let user = this.formRegister;
        let phoneNumber = user.phoneNumber
        axios.post('http://localhost:5000/register', {phone_number:phoneNumber,state_type:"register sms"})
            .then(res => {
                    if (res.data.status=='success') {
                      this.$message.success(`短信发送结果：${res.data.status}`)
                    }else{
                      this.$message.error(`短信发送结果：${res.data.status}`);
                      return false;
                    }
                })
            .catch(err => {
                    this.$message.error(`${err.message}`, 'ERROR!')
                })

      }
    }

};
</script>


<style scoped>

</style>