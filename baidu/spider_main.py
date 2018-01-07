import myUtils.html_downloader as html_downloader
import myUtils.html_parser as html_parser
import myUtils.url_manager as url_manager

import myUtils.html_outputer as html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutPuter()

    # url调度器
    def craw(self, url):
        count = 1
        url = url
        # 先初始化要解析的url
        self.urls.add_new_url(url)
        # 当队列中还存在需要解析的url则执行下面操作
        while self.urls.has_new_url():
            # 取出需要解析的url
            new_url = self.urls.get_new_url()
            # 使用下载器下载url内容
            html_cont = self.downloader.download(new_url)
            # 解析url中的数据
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            # 解析出的新url添加到url管理器列表中
            self.urls.add_new_urls(new_urls)
            # 将解析到的数据输出
            self.outputer.collect_data(new_data)
            if count == 1000:
                break
            count += 1
        self.outputer.output_html()


if __name__ == '__main__':
    print("开始运行---")
    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
