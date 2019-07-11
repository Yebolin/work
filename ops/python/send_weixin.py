#!/usr/bin/env python
# -*- coding: utf-8 -*-
#GuoYabin
 
import requests,json,sys,imp
imp.reload(sys)
 
class WeChat(object):
 
    def __init__(self):
        self.url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        self.corpid = '你的企业微信corpid'
        self.corpsecret = '你的企业微信corpsecret '
         
    def auth(self):
        params={'corpid':self.corpid,'corpsecret':self.corpsecret}
        try:
            rs=requests.get(self.url,params=params)
            return(rs.json()['access_token'])
            rs.close()
        except:
            print('get access_token error!')
 
    def getToken(self):
        try:
            file=open('token.txt','r')
            token=file.read()
            file.close()
        except:
            token=self.auth()
            file=open('token.txt','w')
            file.write(token)
            file.close()
        return(token)
 
 
    def message(self,touser,message):
        data=json.dumps({
            'touser':touser,
            'toparty':'2',
            'msgtype':'text',
            'agentid':'1',
            'text':{
                'content':message},
            'safe':'0'
        },ensure_ascii=True)
        return(data)
         
    def send(self,touser,message):
        try:
            url='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+self.getToken()
            res=requests.post(url,data=self.message(touser,message))
            print(res.json())
            res.close()
        except:
            print('send error!')
             
if __name__ == '__main__':
    weixin=WeChat()
    weixin.send(sys.argv[1],sys.argv[3])
