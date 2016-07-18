#coding=utf-8

from baike_spider import url_manager, html_downloader, html_parser, html_outputer

'''
爬虫总调度程序
'''
class SpiderMain(object):
    ''' 构造函数，初始化URL管理器，下载器，解析器和输出器四个对象 '''
    def __init__(self):
        ''' 初始化URL管理器 '''
        self.urls = url_manager.UrlManager()
        ''' 初始化下载器  '''
        self.downloader = html_downloader.HtmlDownloader()
        ''' 初始化解析器 '''
        self.parser = html_parser.HtmlParser()
        ''' 初始化输出器 '''
        self.outputer = html_outputer.HtmlOutputer()

    ''' 爬虫调度程序 '''
    def craw(self, root_url):
        ''' 设定待爬取的URL初始值 '''
        count = 1
        ''' 将入口URL添加到URL管理器 '''
        self.urls.add_new_url(root_url)
        ''' 当URL管理器里面有待爬取的URL的时候，启动循环处理 '''
        while self.urls.has_new_url():
            try:
                ''' 获取到待爬取的URL '''
                new_url = self.urls.get_new_url()
                ''' 打印爬取的URL的数量值 '''
                print 'craw %d : %s' % (count, new_url)
                ''' 使用下载器下载待爬取URL的页面 '''
                html_cont = self.downloader.download(new_url)
                ''' 使用解析器解析爬取到的URL页面：传入两个参数，当前的URL和页面数据，得到新的URL和数据 '''
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                ''' 新的URL添加进URL管理器 '''
                self.urls.add_new_urls(new_urls)
                ''' 收集数据 '''
                self.outputer.collect_data(new_data)
                
                ''' 目标爬取1000个页面，超过退出爬取 '''
                if count == 100:
                    break
                
                ''' 爬取数量加1 '''
                count = count + 1

            except:
                ''' 爬取异常的情况打印失败 '''
                print 'craw failed!'
        
        ''' 调用outpuer将收集好的数据输出到HTML页面 '''
        self.outputer.output_html()
    
    
''' main函数，设定爬虫的入口URL和要启动的爬虫 '''
if __name__=="__main__":
    ''' 设置要爬取的入口URL '''
    root_url = "http://baike.baidu.com/view/21087.htm"
    ''' 创建一个spider '''
    obj_spider = SpiderMain()
    ''' 调用spider的craw方法来启动爬虫 '''
    obj_spider.craw(root_url)