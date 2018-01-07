import re
from urllib import parse

from bs4 import BeautifulSoup

from spider.baidu.decorator.log import log


class HtmlParser(object):
    @log
    def parse(self, url, html_cont):
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data

    @log
    def _get_new_urls(self, url, soup):
        new_urls = set()
        a = soup.find_all('a', href=re.compile(r'/item/'))
        for i in a:
            print(i['href'])
            new_full_url = parse.urljoin(url, i['href'])
            new_urls.add(new_full_url)
        return new_urls

    @log
    def _get_new_data(self, url, soup):
        res_data = {'url': url, 'title': '', 'summary': ''}
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        # <dd class="lemmaWgt-lemmaTitle-title">
        title_nodes = soup.find_all('dd', class_='lemmaWgt-lemmaTitle-title')
        for title_node in title_nodes:
            res_data['title'] = res_data['title'] + title_node.find('h1').get_text()
        # <div class="para" label-module="para">
        summary_nodes = soup.find_all('div', class_='para')
        for summary_node in summary_nodes:
            res_data['summary'] = res_data['summary'] + summary_node.get_text()
        return res_data
