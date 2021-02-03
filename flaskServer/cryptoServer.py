from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
from Cryptodome.Hash import SHA
from Cryptodome import Random
from base64 import b64decode

##后端生成密钥
def generate_key():
    '''
    生成公钥和私钥

    :return: 公钥和私钥
    '''
    rsa = RSA.generate(1024)

    private_key = rsa.export_key()
    public_key = rsa.publickey().export_key()
    return private_key,public_key


def rsa_decrypy(private_key,message):
    '''
    rsa解密函数

    :param private_key: 私钥
    :param message:  加密后的密文
    :return: 解密后原始信息
    '''
    dsize = SHA.digest_size
    sentinel = Random.new().read(1024+dsize)
    private_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_v1_5.new(private_key)
    return cipher_rsa.decrypt(b64decode(message),sentinel)

def rsa_encrypt(public_key,message):
    '''
    rsa加密函数

    :param public_key:
    :param message:
    :return: 加密后的密文
    '''

    public_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_v1_5.new(public_key)
    return cipher_rsa.encrypt(str.encode(message))


