#-*-coding:utf-8-*-
# date: 2018-11-07
import requests
import json
import hashlib
import urllib
import random

def baidu_translate(text, from_lang='auto', to_lang='zh', appid = 'your appid', secretKey = 'your secretKey'):
    '''调用百度翻译接口，传入文本，自动返回翻译结果。from_lang设置为auto能够自动检测输入数据语言类型。
    appid与secretKey为在百度翻译申请得到的开发者参数。
    '''
    url = 'https://api.fanyi.baidu.com/api/trans/vip/translate'
    salt = random.randint(32768, 65536)
    sign = appid + text + str(salt) + secretKey
    m = hashlib.md5()
    m.update(sign.encode("utf8"))
    sign = m.hexdigest()
    url = url + '?appid=' + appid + '&q=' + urllib.parse.quote(text) + '&from=' + from_lang + '&to=' + to_lang + '&salt=' + str(salt) + '&sign=' + sign
    try:
        result = eval(requests.get(url).text)
        result = result['trans_result'][0]['dst']
    except Exception as e:
        result = ''
        print (e)
    finally:
        return result

if __name__ == '__main__':
    res = baidu_translate('Create a new branch for this commit and start a pull request')
    print(res)
