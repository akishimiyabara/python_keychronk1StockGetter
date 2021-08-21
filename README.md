# python_keychronk1_stock_getter

## 概要
Keychron K1（91_TKL_茶軸）の在庫状況を通知してくれるBot 

## 各種設定
### 1.Line Notifyアクセストークン取得
https://notify-bot.line.me/ja/ からアクセストークンの発行（開発者向け）。

### 2.config.ini作成
line.pyのあるディレクトリにconfig.iniを作成。  
config.iniに下記を記載する。
```
[line]
token = 取得したLine Notifyアクセストークン（書き換える）
```

### 3.ファイル実行
```
python keychronK1_stock_getter.py
```
実行すると、LINE Notifyから通知が飛びます。  
※AWS Lambda実行の場合には「ランタイム設定 - ハンドラ」に「keychronk1_stock_getter.lambda_handler」を設定する。
