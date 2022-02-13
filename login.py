

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
"Intel Core 2 Duo E6540",
"Intel Core 2 Duo E6550",
"Intel Core 2 Duo E6600",
"Intel Core 2 Duo E6700",
"Intel Core 2 Duo E6750",
"Intel Core 2 Duo E6850",

"Intel Core 2 Duo E7200",
"Intel Core 2 Duo E7300",
"Intel Core 2 Duo E7400",
"Intel Core 2 Duo E7500",
"Intel Core 2 Duo E7600",
"Intel Core 2 Duo E8190",
"Intel Core 2 Duo E8200",
"Intel Core 2 Duo E8300",
"Intel Core 2 Duo E8400",
"Intel Core 2 Duo E8500",
"Intel Core 2 Duo E8600",

"Intel Core 2 Quad Q6600",
"Intel Core 2 Quad Q6700",

"Intel Core 2 Quad Q8200s",
"Intel Core 2 Quad Q8200",
"Intel Core 2 Quad Q8300",
"Intel Core 2 Quad Q8400s",
"Intel Core 2 Quad Q8400",
"Intel Core 2 Quad Q9300",
"Intel Core 2 Quad Q9400s",
"Intel Core 2 Quad Q9400",
"Intel Core 2 Quad Q9450",
"Intel Core 2 Quad Q9505",
"Intel Core 2 Quad Q9550s",
"Intel Core 2 Quad Q9550",
"Intel Core 2 Quad Q9650",
]

Intel_LGA1155_Sandy_Bridge = [
"Intel Pentium G620T",
"Intel Pentium G630T",
"Intel Pentium G640T",
"Intel Pentium G645T",
"Intel Pentium G860T",
"Intel Pentium G620",
"Intel Pentium G630",
"Intel Pentium G640",
"Intel Pentium G645",
"Intel Pentium G840",
"Intel Pentium G850",
"Intel Pentium G860",
"Intel Pentium G870",
"Intel Celeron G440",
"Intel Celeron G460",
"Intel Celeron G465",
"Intel Celeron G470",
"Intel Celeron G530T",
"Intel Celeron G540T",
"Intel Celeron G550T",
"Intel Celeron G530",
"Intel Celeron G540",
"Intel Celeron G550",
"Intel Celeron G555",
"Intel Xeon E3-1220",
"Intel Xeon E3-1225",
"Intel Xeon E3-1220L",
"Intel Xeon E3-1230",
"Intel Xeon E3-1235",
"Intel Xeon E3-1240",
"Intel Xeon E3-1245",
"Intel Xeon E3-1260L",
"Intel Xeon E3-1270",
"Intel Xeon E3-1275",
"Intel Xeon E3-1280",
"Intel Xeon E3-1290",
]

Intel_LGA1155_Ivy_Bridge = [
"Intel Pentium G2020T",
"Intel Pentium G2030T",
"Intel Pentium G2100T",
"Intel Pentium G2120T",
"Intel Pentium G2010",
"Intel Pentium G2020",
"Intel Pentium G2030",
"Intel Pentium G2120",
"Intel Pentium G2130",
"Intel Pentium G2140",
"Intel Celeron G1610T",
"Intel Celeron G1620T",
"Intel Celeron G1610",
"Intel Celeron G1620",
"Intel Celeron G1630",
"Intel Xeon E3-1220 v2",
"Intel Xeon E3-1225 v2",
"Intel Xeon E3-1220L v2",
"Intel Xeon E3-1230 v2",
"Intel Xeon E3-1235 v2",
"Intel Xeon E3-1240 v2",
"Intel Xeon E3-1245 v2",
"Intel Xeon E3-1260L v2",
"Intel Xeon E3-1270 v2",
"Intel Xeon E3-1275 v2",
"Intel Xeon E3-1280 v2",
"Intel Xeon E3-1290 v2",
]

AMD_Socket_FM1 = [
"AMD A8-3870K",
"AMD A8-3850",
"AMD A8-3820",
"AMD A8-3800",
"AMD A6-3670K",
"AMD A6-3650",
"AMD A6-3620",
"AMD A6-3600",
"AMD A6-3500",
"AMD A4-3400",
"AMD A4-3300",
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

AMD_Socket_AM4_ZenPlus = [
"AMD Ryzen5 1600 AF"    #* ここ当たり枠
]

stones = {
"LGA775": Intel_LGA775,
"LGA1155_Sandy_Bridge": Intel_LGA1155_Sandy_Bridge,
"LGA1155_Ivy_Bridge": Intel_LGA1155_Ivy_Bridge,
"SocketFM1": AMD_Socket_FM1,
"SocketFM2": AMD_Socket_FM2,
"SocketAM4_ZenPlus": AMD_Socket_AM4_ZenPlus,
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
