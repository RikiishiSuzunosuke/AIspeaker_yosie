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
        f = open("j-train_data.txt","w")
        while True:

            data = self.sock.recv(DATASIZE).decode('utf-8')

            for line in data.split('\n'):
                index = line.find('WORD="')
                if index != -1:
                    strTemp = strTemp + line[index+6:line.find('"',index+6)]

                if '</RECOGOUT>' in line:
                    fin_flag = True

            if fin_flag == True:
                strTemp = julius.text_change(strTemp)
                f.write(strTemp + "\n")
                print(strTemp + ":書き込みました")
                fin_flag = False
                strTemp = ""
                func = ""
        f.close()

if __name__ == "__main__":
    julius = Julius()
    julius.run()


