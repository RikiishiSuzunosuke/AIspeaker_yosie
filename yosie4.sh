#!/bin/bash
export LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0
cd ~/AIspeaker_yosie
./jtalk-start.sh 起動中です。起動には二分ほどかかります。

python3 sc_FT.py
./fortune-m.sh
python3 sc_Weather.py
./weather-m.sh
python3 sc_News.py
./news_make.sh
./muute_off.sh

./jtalk-start.sh 起動しました。ご用件をお申し付けください。
python3 julius_python_AI.py
