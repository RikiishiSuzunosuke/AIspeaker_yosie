import socket
import time
import sc_Days
import news_get
import os
import random
import predict

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
                    	strTemp = strTemp[5:]
                    	print(strTemp)

            # 話した言葉毎に、print文を実行
            if fin_flag == True:

            	pre_label = predict.predict(strTemp)

                strTemp = julius.text_change(strTemp) # [s],[/s]を削除
                if pre_label == '0':
                    os.system('./jtalk-start.sh 処理中です、しばらくお待ちください')
                    os.system('./jtalk-weather.sh')

                elif pre_label == '1':
                    os.system('./jtalk-start.sh 処理中です、しばらくお待ちください')
                    news_get.news_get()
                    os.system('./jtalk-news.sh')

                elif pre_label == '2':
                    os.system('./jtalk-start.sh 処理中です、しばらくお待ちください')
                    sc_Days.get_days()
                    os.system('./jtalk-days.sh')
                elif pre_label == '3':
                    os.system('./jtalk-start.sh 処理中です、しばらくお待ちください')
                    os.system('./jtalk-fortune.sh')
                
                fin_flag = False
                strTemp = ""
                func = ""

if __name__ == "__main__":
    julius = Julius()
    julius.run()


