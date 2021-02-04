from flask import Flask,jsonify,request,redirect
from flask_cors import CORS
from Book import BookInfo
from userinfo import UserInfo



#配置Debug模式
DEBUG = True

#实例化App
app = Flask(__name__)
app.config.from_object(__name__)
#实例化操作类
book = BookInfo()
userinfo = UserInfo()

#enable CORS
CORS(app, resources={r'/*':{'origins':'*'}})
#测试路由
@app.route('/ping',methods=['GET'])
def ping_pong():
    return jsonify('pong!')

#打开 /book页面
@app.route('/books',methods=['GET','POST'])
def all_books():
    return book.all_books()

@app.route('/books/<book_id>', methods=['PUT','DELETE'])
def single_book(book_id):
    return book.single_book(book_id)

@app.route('/flask')
def hello_world():
    return 'Hello World!'

#登录与注册功能
@app.route('/login',methods=['POST'])
def login_veritify_code():
    #print("====router:login=====")
    #return userinfo.login_no_veritify_code()
    #return userinfo.login_rsa_decrypt_no_veritify_code()
    #login_rsa_decrypt_with_veritify_code
    return userinfo.login_rsa_decrypt_with_veritify_code()

@app.route('/register',methods=['POST'])
def register_with_sms_code():
    #print("register_with_sms_code")
    #print("====router:register=====")
    return userinfo.register_with_sms_code()

@app.route('/code',methods=['GET'])
def get_veritify_code():
    return jsonify(userinfo._PHONE)

if __name__ == '__main__':

    app.run()
