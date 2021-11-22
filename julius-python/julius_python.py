import socket
import time
import scraping
import os

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
                    fin_flag = True

            # 話した言葉毎に、print文を実行
            if fin_flag == True:
                strTemp = julius.text_change(strTemp) # [s],[/s]を削除
                if '天気' in strTemp:
                    func = "0"
                elif 'ニュース' in strTemp:
                    func = "1"
                elif '日時' in strTemp:
                    func = "2"
                elif '占い' in strTemp:
                    func = "3"
                else:
                    func = "99"
                os.system('./jtalk-start.sh 処理中です、しばらくお待ちください')
                scraping.yosie_action(func)
                os.system('./jtalk.sh')

                fin_flag = False
                strTemp = ""
                func = ""

if __name__ == "__main__":
    julius = Julius()
    julius.run()


