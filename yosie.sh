#!/bin/bash
cd ~/AIspeaker_yosie
while :
do
	python3 scraping.py
	./jtalk.sh
done
