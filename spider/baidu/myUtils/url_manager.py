from spider.baidu.decorator.log import log


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    @log
    def add_new_url(self, url):
        if url is None:
            print('url为空')
            return
        print('当前已解析的url列表:{}'.format(self.old_urls))
        if url not in self.new_urls and url not in self.old_urls:
            print('添加的url:{}'.format(url))
            self.new_urls.add(url)

    @log
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    @log
    def has_new_url(self):
        return len(self.new_urls) != 0

    @log
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
