#!/bin/bash
cd ~/AIspeaker_yosie
sleep 6
./jtalk-start.sh うぇいくあっぷ
python3 julius_python.py
# while :
# do
# 	#a=$(python3 -c "from julius_python import julius; run()")
# 	#a=$(python3 julius_python.py.run())
# 	#a=$(python3 -c "import julius_python.julius; julius_python.julius.run()")
# 	#a=$(python3 julius_python.py)
# 	python3 scraping.py $a
# 	./jtalk.sh
# done
