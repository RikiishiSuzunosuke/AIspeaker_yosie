#!/bin/bash
cd ~/AIspeaker_yosie
python3 sc_FT.py
python3 sc_Weather.py
python3 sc_News.py
./jtalk-start.sh うぇいくあっぷ
python3 julius_python2.py
