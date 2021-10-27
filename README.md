# AIスピーカーYoSiE
卒業制作用リポジトリ
## システムの流れ

![image](https://user-images.githubusercontent.com/84367202/138005932-7bfbf8a7-f4c6-4913-8cd4-85a2595cedf1.png)


## YoSiEの機能について
音声を認識<br>
機械学習にかけて質問を理解<br>
質問に応じた関数(機能)を返す<br>
・暫定で決まっている機能<br>
　・カメラで写真撮影<br>
　・ニュース読み上げ [参考サイト](https://rurukblog.com/post/python-webscraping-ynews/)<br>
　・天気予報読み上げ [参考サイト](https://www.webzoit.net/hp/it/internet/homepage/env/iot/raspberry_pi/smart_speaker/weather/)<br>
　・日付/時刻読み上げ<br>
　・本日の星座占い(自作コード)
 
## 使用する技術
### 音声認識
+ Julius
### AI
+ MeCab(形態素解析)
+ tensorflow(機械学習)
### スクレイピング
+ BeautifulSoup4
### 合成音声
+ OpenJTalk
### 音声入力
+ 全指向性マイク
### 音声出力
+ スピーカー

### イメージ図

![外見案](https://user-images.githubusercontent.com/84367300/137059780-6375c5bd-a04a-4c02-830e-173781ab133f.png)

## [ガントチャート](https://brabioproject.appspot.com/project/ganttchart/ahJzfmJyYWJpb3Byb2plY3RocmRyEQsSB1Byb2plY3QY47LTxzUM/)

## 作業進捗
10/22時点
+ スクレイピング結果をOpenJtalkに喋らせることに成功
+ 上記を一つのシェルスクリプトにまとめて、一括実行できるようにした
+ スクレイピングのサンプルコードを一つのフォルダにまとめた
+ MeCabとFastTextを利用した機械学習を検討中

+ FastTextによる機械学習のサンプルコードの動作を確認
+ トレーニングデータの形式等も理解

10/27時点
+ scraping.pyをinputboxではなく、引数入力に改変(Julius等を実装した際に、そちらの方が動かしやすいため)
+ yosie.shをラズパイ起動時に自動実行できるようになった
+ Juliusをインストール中
