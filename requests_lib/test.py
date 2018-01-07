import requests
from urllib import request

params = {
    'params': 'mj4h7V28kjGVqpKTvMV5rAS8OmOo0u4ZvaBWvito6Dw897eY6ZElXdYbiZ7EmfRUMve+jcaNIyIx1p4pqB0X0A7cWeh18EVQvuWNVn0BwyjVJq409x/ltMveD9kFo6FO',
    'encSecKey': '8fb5fef391f4de96d194a84d6f67a0c3dc4b357f0ee91e10ae98817042c134574a991735e2c8eb208b5991434562869f1b33726385eb35f56fb898416b14965b4ca69c8b53b24afbf2d8bbfb51936ce1315d2ae769ff874e92d76dc366f46f620403f159f487b9568e342907130195872c5f3dc018daee189734a328f7aa2426'
}
response = requests.post(url='http://music.163.com/weapi/song/enhance/player/url?csrf_token=', data=params)
data = response.json().get('data')[0].get('url')
print('资源文件下载地址:' + data)
# 将资源下载至桌面
request.urlretrieve(data, r'C:\Users\hasee\Desktop\how long.mp3')
