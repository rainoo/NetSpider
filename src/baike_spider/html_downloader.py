#coding=utf-8
import urllib2

'''
下载器类
'''
class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return None
        
        ''' 请求该url内容 '''
        response = urllib2.urlopen(url)
        
        ''' 如果返回值不是200，直接返回 '''
        if response.getcode() != 200:
            return None
        
        ''' 访问正常的情况返回read()方法 '''
        return response.read()
            
    
    



