import requests
from bs4 import BeautifulSoup

data = {
    'source': 'index_anv',
    'redir': 'https://www.douban.com/',
    'login': '登陆'
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 '
                  'Safari/537.36 '
}
urls = 'https://www.douban.com/login'
after_url = 'https://www.douban.com/people/95231173/'


def login(user, passwd, url):
    data['form_email'] = user
    data['form_password'] = passwd
    s = requests.session()
    login_result = s.post(url, data=data, headers=header)
    print(login_result.text)
    # 验证是否需要验证码
    code = get_captcha(login_result.text)
    if code is None:
        # 如果需要验证码则获取验证码
        data['captcha-id'] = code
        login_result = s.post(url, data=data, headers=header)
    print(login_result.text)
    response = s.get(after_url, cookies=login_result.cookies, headers=header)
    return response.content


def get_captcha(url_cont):
    soup = BeautifulSoup(url_cont, 'html.parser')
    captcha = soup.find('div', class_='captcha_block')
    if captcha is None:
        return None
    captcha = captcha.find('input', type='hidden')
    print(captcha.get('value'))
    code = captcha.get('value')
    return code


if __name__ == '__main__':
    username = ''
    password = ''
    cont = login(username, password, urls)
    print(cont.decode('utf-8'))
