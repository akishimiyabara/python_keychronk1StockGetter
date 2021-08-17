import urllib.request
from bs4 import BeautifulSoup

# Keychron K1 ワイヤレス・メカニカルキーボード White LED（テンキーレス）
url = 'https://superkopek.stores.jp/items/60c011eb4be7ef5c6d083a60'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '
'AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/55.0.2883.95 Safari/537.36 '
productName='White LEDライト-日本語（テンキーレス）-Gateron茶軸'
targetClass='main_content_result_item'

req = urllib.request.Request(url, headers={'User-Agent': ua})
html = urllib.request.urlopen(req)
soup = BeautifulSoup(html, "html.parser")
topicsindex = soup.find('div', attrs={'class': targetClass})
topics = topicsindex.find_all('li')
for topic in topics:
  if topic.find('h2').text == productName:
    print(topic.find('button').text)
    break