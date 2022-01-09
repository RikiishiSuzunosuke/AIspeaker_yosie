#!/bin/bash
option="-m /usr/share/hts-voice/mei/mei_happy.htsvoice \
-x /var/lib/mecab/dic/open-jtalk/naist-jdic \
-r 1.5 \
-a 0.55 \
-ow weather.wav weather.txt"

echo "$1" | open_jtalk $option