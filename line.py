import sys
import urllib.parse
import configparser

LINE_NOTIFY_URL="https://notify-api.line.me/api/notify"

def notify_sender(msg):
    config = configparser.ConfigParser()
    config.read('config.ini')

    method = "POST"
    headers = {"Authorization": "Bearer %s" % config.get('line', 'token')}
    payload = {"message": msg}
    try:
        payload = urllib.parse.urlencode(payload).encode("utf-8")
        req = urllib.request.Request(
            url=LINE_NOTIFY_URL, data=payload, method=method, headers=headers)
        urllib.request.urlopen(req)
    except Exception as e:
        print ("Exception Error: ", e)
        sys.exit(1)