#!/bin/bash
tempfile=`tempfile`
option="-m /usr/share/hts-voice/mei/mei_happy.htsvoice \
-x /var/lib/mecab/dic/open-jtalk/naist-jdic \
-r 1.5 \
-a 0.55 \
-ow $tempfile result.txt"

echo "$1" | open_jtalk $option
aplay -q $tempfile
rm $tempfile
