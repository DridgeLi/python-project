from urllib import request

from myDecorator.log import log


class HtmlDownloader(object):
    @log
    def download(self, url):
        if url is None:
            return None
        print(url)
        res = request.urlopen(url)
        if res.getcode() != 200:
            return None
        cont = res.read().decode('utf-8')
        print(cont)
        return cont
