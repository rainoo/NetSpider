#coding=utf-8
from bs4 import BeautifulSoup
import re
import urlparse

'''
解析器类
'''
class HtmlParser(object):

    ''' 取得所有的分支URL '''
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /view/123.htm
        
        ''' 使用正则表达式得到所有的枝条URL '''
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        
        ''' 处理URL '''
        for link in links:
            new_url = link['href']
            ''' 拼接成一个完全的url '''
            new_full_url = urlparse.urljoin(page_url, new_url)
            ''' 将取得的url添加到new_urls中 '''
            new_urls.add(new_full_url)
        
        return new_urls
    
    
    ''' 取得数据 '''
    def _get_new_data(self, page_url, soup):
        res_data = {}
        
        ''' url也放置到结果中方便使用 '''
        res_data['url'] = page_url
        
        ''' 
        <dd class="lemmaWgt-lemmaTitle-title">
        <h1 >Python</h1>
        ''' 
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        
        ''' 
        <div class="lemma-summary" label-module="lemmaSummary">
        ''' 
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        
        return res_data
    
    
    '''
        解析器方法
        需要我们从cont中解析出两个数据，新的URL和数据
    '''
    def parse(self, page_url, html_cont):
        
        ''' 参数判断，为空直接返回 '''
        if page_url is None or html_cont is None:
            return
        
        ''' 将cont加载到soup '''
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        ''' 使用两个本地方法getUrl和getData '''
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        ''' 返回URL和数据 '''
        return new_urls, new_data
    
    



