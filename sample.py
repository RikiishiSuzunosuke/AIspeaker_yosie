import MeCab

mecab = MeCab.Tagger("")
target_str = "DOS窓では、基本的には日本語がアウトです"
print(mecab.parse(target_str))