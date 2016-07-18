#coding=utf-8

'''
URL管理器类
需要维护两个列表：
1，待爬取的URL列表；
2，爬取过的URL列表。
'''
class UrlManager(object):
    
    def __init__(self):
        ''' 待爬取的url '''
        self.new_urls = set()
        ''' 爬取过的url '''
        self.old_urls = set()
    
    ''' 向URL管理器中添加一个新的URL '''
    def add_new_url(self, url):
        ''' 参数判断，空不进行添加 '''
        if url is None:
            return
        ''' url既不在待爬取的也不在爬取过的列表时，说明为全新的url，用来待爬取 '''
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    
    ''' 向URL管理器中添加批量的URL '''
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
    
    ''' 判断URL管理器中是否有新的待爬取的URL '''
    def has_new_url(self):
        return len(self.new_urls) != 0
    
    ''' 从URL管理器中获取一个待爬取的URL '''
    def get_new_url(self):
        ''' pop（）这个方法从列表中获取一个url并移除该url '''
        new_url = self.new_urls.pop()
        ''' 将该url添加进old_urls（爬取过的urls） '''
        self.old_urls.add(new_url)
        ''' 将该url返回 '''
        return new_url
    