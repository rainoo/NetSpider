#coding=utf-8

'''
输出器方法
需要我们从cont中解析出两个数据，新的URL和数据
'''
class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
    
    '''
        收集数据方法
    '''
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)


    '''
        将收集好的数据写出到html文件中
    '''
    def output_html(self):
        fout = open('output.html', 'w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table border='1'>")
        
        # ascii 转 utf-8
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")