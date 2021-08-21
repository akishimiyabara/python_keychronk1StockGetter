import urllib.request
import line
from bs4 import BeautifulSoup

# Keychron K1 ワイヤレス・メカニカルキーボード White LED（テンキーレス）
URL1 = 'https://superkopek.stores.jp/items/60c011eb4be7ef5c6d083a60'
PRODUCT_NAME1='White LEDライト-日本語（テンキーレス）-Gateron茶軸'
# Keychron K1 ワイヤレス・メカニカルキーボード RGB（テンキーレス）
URL2 = 'https://superkopek.stores.jp/items/603db1146728be5bc4c1aaec'
PRODUCT_NAME2='RGBライト-日本語（テンキーレス）-Gateron茶軸'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '
'AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/55.0.2883.95 Safari/537.36 '
TARGET_CLASS='main_content_result_item'

def main():
  line.notify_sender(stock_getter(URL1, PRODUCT_NAME1) + '\n' + stock_getter(URL2, PRODUCT_NAME2))

def lambda_handler(event, lambda_context):
  main()

def stock_getter(url, product_name):
  req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
  html = urllib.request.urlopen(req)
  soup = BeautifulSoup(html, "html.parser")
  topics_index = soup.find('div', attrs={'class': TARGET_CLASS})
  topics = topics_index.find_all('li')
  for topic in topics:
    if topic.find('h2').text == product_name:
      return '【' + topic.find('h2').text + '】' + topic.find('button').text

if __name__ == "__main__":
  main()