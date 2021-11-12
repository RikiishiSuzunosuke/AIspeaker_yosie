#!/bin/bash
cd ~/grammar
julius -C ~/grammar/grammar-kit-4.3.1/hmm_mono.jconf -input mic -gram ~/grammar/test -nostrip -module
