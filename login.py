

import datetime
import random
import os
import unicodedata


d_today = datetime.date.today().strftime("%Y/%m/%d")
# d_today = d_today.strftime("%Y/%m/%d")

Intel_LGA775 = [
"Intel Core 2 Duo E4300",
"Intel Core 2 Duo E4400",
"Intel Core 2 Duo E4500",
"Intel Core 2 Duo E4600",
"Intel Core 2 Duo E4700",
"Intel Core 2 Duo E6300",
"Intel Core 2 Duo E6320",
"Intel Core 2 Duo E6400",
"Intel Core 2 Duo E6420",
"Intel Core 2 Duo E6600",
"Intel Core 2 Duo E6700",
"Intel Core 2 Duo E7300",
"Intel Core 2 Duo E7400",
"Intel Core 2 Duo E7500",
"Intel Core 2 Duo E8400",
"Intel Core 2 Duo E8600",
"Intel Core 2 Duo E8500",
"Intel Core 2 Quad Q9400",
]
AMD_Socket_FM2 = [
"AMD A10-5700",
"AMD A10-5700",
"AMD A10-5800K",
"AMD A10-5800K",
"AMD A10-6700",
"AMD A10-6700T",
"AMD A10-6790K",
"AMD A10-6800K",
"AMD A10-6800K",
"AMD A4-4000",
"AMD A4-4020",
"AMD A4-5300",
"AMD A4-5300",
"AMD A4-6300",
"AMD A4-7300",
"AMD A6-5400K",
"AMD A6-5400K",
"AMD A6-6400K",
"AMD A8-5500",
"AMD A8-5500",
"AMD A8-5600K",
"AMD A8-5600K",
"AMD A8-6500",
"AMD A8-6600K",
]

stones = {
"LGA775": Intel_LGA775,
"SocketFM2": AMD_Socket_FM2,
}

bonus = (f"{random.choice(random.choice(list(stones.items()))[1])}")

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
