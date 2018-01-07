from urllib import request

from spider.baidu.decorator.log import log


class HtmlDownloader(object):
    @log
    def download(self, url):
        new_url = url
        if new_url is None:
            return None
        res = request.urlopen(str(new_url.encode('utf-8'))[2:])
        if res.getcode() != 200:
            return None
        cont = res.read().decode('utf-8')
        return cont
