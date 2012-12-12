#coding=utf-8
#an automated tool for submiting form based on template config file
import string
import sys
import urllib,urllib2,cookielib
from urllib2 import  URLError, HTTPError
import socket
import types
import codecs
import chardet
 
class Autoform:
    def __init__(self):
        self._opener = self._setOpener()
       
    def _setOpener(self):
        #if the opener is already set, use the opener,if not, build a new opener.
        if urllib2._opener:
            self._opener = urllib2._opener
        else:
            cookiehandler = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
            redirectHandle = urllib2.HTTPRedirectHandler()
            proxyHandle = urllib2.ProxyHandler({})  #proxy set empty,not to use a proxy
            opener = urllib2.build_opener(cookiehandler,redirectHandle,proxyHandle)
            opener.addheaders = [('User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')]
            return opener
         
    def readTemplate(self, tplFile):
        charset = chardet.detect(open(tplFile).read())
        if charset:
            return dict([line.strip().split(':', 1) for line in codecs.open(tplFile, 'r', encoding=charset['encoding'])]) 
        else:
            raise 'charset detect error!'
        
    def open(self, url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        return self._opener.open(url, data, timeout)
        
    def submit(self, url, tpl=None, paras=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        #use a template or not
        if tpl:
            formTemplate = self.readTemplate(tpl)
            formTemplate.update(paras)
            enparams = urllib.urlencode(formTemplate)
        else:   
            enparams = urllib.urlencode(paras)
            
        html = ''
        req = urllib2.Request(url, enparams)
        try:
            html = self._opener.open(req, timeout=timeout).read()
        except:
            pass 
        return html
