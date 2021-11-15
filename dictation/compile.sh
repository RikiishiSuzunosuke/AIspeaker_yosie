#!/bin/bash
rm tmp*
rm test.dfa test.dict test.term
mkdfa.pl ~/grammar/test
mv test.dfatmp test.dfa
