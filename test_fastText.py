import MeCab

tagger = MeCab.Tagger("")
result = tagger.parse("私は東京に住んでいます。")
print(result)