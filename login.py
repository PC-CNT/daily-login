

import datetime
import random
import os
import unicodedata


d_today = datetime.date.today().strftime("%Y/%m/%d")
# d_today = d_today.strftime("%Y/%m/%d")

stones = ["Intel Core 2 Duo E7500", "Intel Core 2 Duo E7300", "Intel Core 2 Duo E7400", "Intel Core 2 Duo E8400",
          "Intel Core 2 Duo E8600", "Intel Core 2 Quad Q8200", "AMD A6-5400K", "AMD Ryzen 5 1600AF", "Intel Xeon E-2134"]

bonus = (f"{random.choice(stones)}")

daycounter = 1

path_md = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ログボ.md")

def len_aa(text: str) -> int:
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 1
        else:
            count += 0.5
    return int(count)

#* 強調AA
def aa_impact(moji: str) -> str:
    aa = ""
    aa += (f"＿{'人' * (len_aa(moji) + 2)}＿\n＞  {moji}  ＜\n￣{'Y^' * (len_aa(moji) + 2)}￣")
    return aa


#* md初期化
if os.path.exists(path_md) == False:
    with open(path_md, "w", encoding="utf-8") as f:
        f.write(f"# ログインボーナス\n")
        print("プロファイルを新規作成しました")


#* 今日実行したかどうか
with open(path_md, "r", encoding="utf-8") as f:
    for line in f.readlines():
        if line.startswith("## "):
            daycounter += 1
        if (line.startswith("## " + str(d_today))):
            print(f"今日（{d_today}）のログインボーナスは取得済みです！")
            exit()


#* ログインボーナス取得
message = (f"""
## {d_today}

{daycounter}日目のログインボーナス

- **{bonus}**
""")

with open(path_md, "a", encoding="utf-8") as f:
    f.write(message)
    print(f"""今日（{d_today}）のログインボーナスを取得しました！\n{aa_impact(bonus)}""")
