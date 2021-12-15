#!/bin/bash
cd ~/AIspeaker_yosie
python3 sc_FT.py
./fortune-m.sh
python3 sc_Weather.py
./weather-m.sh
python3 sc_News.py
./news-m.sh
./jtalk-start.sh 起動
python3 julius_python2.py
