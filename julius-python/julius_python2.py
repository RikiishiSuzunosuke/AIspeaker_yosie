import socket
import time
import sc_Days
import news_get
import get_time
import os
import random

HOST = '127.0.0.1'   # juliusサーバーのIPアドレス
PORT = 10500         # juliusサーバーの待ち受けポート
DATASIZE = 1024     # 受信データバイト数

class Julius:

    def __init__(self):
        self.sock = None
        #self.sock = None

    def text_change(self, text):
        text = text.replace('[s]', '')
        text = text.replace('[/s]', '')
        return text

    def run(self):
        # socket通信でjuliusサーバーに接続
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))

        strTemp = "" # 話した言葉を格納する変数
        fin_flag = False # 話終わりフラグ
        func = "" #出力内容

        while True:

          # juliusサーバからデータ受信
            data = self.sock.recv(DATASIZE).decode('utf-8')

            for line in data.split('\n'):
                # 受信データから、<WORD>の後に書かれている言葉を抽出して変数に格納する。
                # <WORD>の後に、話した言葉が記載されている。
                index = line.find('WORD="')
                if index != -1:
                    # strTempに話した言葉を格納
                    strTemp = strTemp + line[index+6:line.find('"',index+6)]

                # 受信データに</RECOGOUT>'があれば、話終わり ⇒ フラグをTrue
                if '</RECOGOUT>' in line:
                    if 'ねぇよしえ' in strTemp:
                        fin_flag = True
                        strTemp = julius.text_change(strTemp) # [s],[/s]を削除
                        strTemp = strTemp[5:] # ねぇよしえを削除
                    else:
                        strTemp = ""

            # 話した言葉毎に、print文を実行
            if fin_flag == True:
                os.system('./muute_on.sh')
                print(strTemp)
                if '天気' in strTemp:
                    os.system('./jtalk-start.sh 天気予報をお伝えします')
                   #os.system('./jtalk-weather.sh')
                    os.system('./weather-p.sh')
                   #get_time.time_sleep("weather.wav")

                elif 'ニュース' in strTemp:
                    os.system('./jtalk-start.sh 本日のニュースを読み上げます')
                    num = random.randrange(8)
                   #os.system('./jtalk-news.sh')
                    os.system('./news-p-'+ str(num) + '.sh')
                   #get_time.time_sleep("news.wav")

                elif '日時' in strTemp:
                    os.system('./jtalk-start.sh 現在の日時をお伝えします')
                    sc_Days.get_days()
                    os.system('./jtalk-days.sh')
                  #get_time.time_sleep("open_jtalk.wav")

                elif '占い' in strTemp:
                    os.system('./jtalk-start.sh 本日の星座占いを読み上げます')
                   #os.system('./jtalk-fortune.sh')
                    os.system('./fortune-p.sh')
                   #get_time.time_sleep("fortune.wav")

                else:
                    pass
                fin_flag = False
                strTemp = ""
                os.system('./muute_off.sh')

if __name__ == "__main__":
    julius = Julius()
    julius.run()


