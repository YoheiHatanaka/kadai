### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
import pandas as pd

df = pd.read_csv('source.csv')
source = list(df["name"])
print(source)

### 検索ツール

word =input("鬼滅の登場人物の名前を入力してください >>> ")

### ここに検索ロジックを書く
if word in source:
    print(f"{word}が見つかりました")
else:
    print(f"{word}が見つかりません")
    add_flg = source.append(word)

df=pd.DataFrame(source,columns=["name"])
df.to_csv("source.csv",encoding="utf_8-sig")
print(source)
