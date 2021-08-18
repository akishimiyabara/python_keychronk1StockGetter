import urllib.request
from bs4 import BeautifulSoup

# Keychron K1 ワイヤレス・メカニカルキーボード White LED（テンキーレス）
url1 = 'https://superkopek.stores.jp/items/60c011eb4be7ef5c6d083a60'
productName1='White LEDライト-日本語（テンキーレス）-Gateron茶軸'
# Keychron K1 ワイヤレス・メカニカルキーボード RGB（テンキーレス）
url2 = 'https://superkopek.stores.jp/items/603db1146728be5bc4c1aaec'
productName2='RGBライト-日本語（テンキーレス）-Gateron茶軸'
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '
'AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/55.0.2883.95 Safari/537.36 '
targetClass='main_content_result_item'

def main():
  # Keychron K1 ワイヤレス・メカニカルキーボード White LED（テンキーレス）
  stockGetter(url1, productName1)
  # Keychron K1 ワイヤレス・メカニカルキーボード RGB（テンキーレス）
  stockGetter(url2, productName2)

def stockGetter(url, productName):
  req = urllib.request.Request(url, headers={'User-Agent': userAgent})
  html = urllib.request.urlopen(req)
  soup = BeautifulSoup(html, "html.parser")
  topicsindex = soup.find('div', attrs={'class': targetClass})
  topics = topicsindex.find_all('li')
  for topic in topics:
    if topic.find('h2').text == productName:
      print(topic.find('h2').text + ' ' + topic.find('button').text)
      break

if __name__ == "__main__":
  main()