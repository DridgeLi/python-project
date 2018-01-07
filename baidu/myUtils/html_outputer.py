import os

from myDecorator.log import log


class HtmlOutPuter(object):
    def __init__(self):
        self.datas = []

    @log
    def collect_data(self, data):
        if data is None:
            print('data为空')
            return
        self.datas.append(data)

    @log
    def output_html(self):
        print('记录数据')
        os.chdir('D:/test/')
        with open('output.html', 'a+', encoding='utf-8') as f:
            f.write('<html>')
            f.write('<body>')
            f.write('<table>')

            for data in self.datas:
                print(data)
                f.write('<tr>')
                f.write('<td>{}</td>'.format(data['url']))
                f.write('<td>{}</td>'.format(data['title']))
                f.write('<td>{}</td>'.format(data['summary']))
                f.write('</tr>')
            f.write('</table>')
            f.write('</body>')
            f.write('</html>')
