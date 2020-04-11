import tkinter as TKI

MAX_CHECK_COUNTS = 7

"""
 診断結果リスト
"""
RESULT = [
    "前世が猫っだった可能性は薄いです。",
    "いたって普通の人間です。",
    "特別、おかしなところはありません。",
    "やや猫っぽいところがあります。",
    "猫に近い性格のようです。",
    "猫にかなり近い性格です。",
    "前世は猫だったかもしれません。",
    "見た目は人間、中身は猫の可能性があります。",
]


# 「診断する」ボタン押下
def click_btn():
    count = 0
    for i in range(MAX_CHECK_COUNTS):
        if bvar[i].get() == True:
            count = count + 1
    nekodo = int(100 * count / MAX_CHECK_COUNTS)
    text.delete("1.0", TKI.END)
    text.insert("1.0", "＜診断結果＞\nあなたの猫度は" + str(nekodo) + "％です。\n" + RESULT[count])
    # text.delete("1.0", TKI.END)
    # text.insert("1.0", "チェックの数は" + str(count))


"""
 メイン
"""
root = TKI.Tk()
# ウィンドウタイトル
root.title("猫度診断アプリ")

# ウィンドウサイズ変更不可
root.resizable(False, False)

# キャンバス作成
canvas = TKI.Canvas(root, width=800, height=600)
# キャンバス配置
canvas.pack()

# 画像の読み込み
picture = TKI.PhotoImage(file="sumire.png")
# 画像の表示
canvas.create_image(400, 300, image=picture)

# ボタンの作成
button = TKI.Button(text="診断する", font=("Times New Roman", 32), bg="lightgreen", command=click_btn)
# ボタンの配置
button.place(x=400, y=480)

# テキスト入力作成
text = TKI.Text(width=40, height=5, font=("Times New Roman", 16))
# テキスト入力配置
text.place(x=320, y=30)

# チェックボックステキストリスト
ITEM = ["高いところが好き",
        "ボールを見ると転がしたくなる",
        "びっくりすると髪の毛が逆立つ",
        "ネズミの玩具が気になる",
        "匂いに敏感",
        "魚の骨をしゃぶりたくなる",
        "夜、元気になる",
        ]

# BooleanVarオブジェクト配列
bvar = [None] * MAX_CHECK_COUNTS
# チェックボックスオブジェクト配列
cbtn = [None] * MAX_CHECK_COUNTS
for i in range(MAX_CHECK_COUNTS):
    # BooleanVarオブジェクト作成
    bvar[i] = TKI.BooleanVar()
    bvar[i].set(False)
    # チェックボックス作成
    cbtn[i] = TKI.Checkbutton(text=ITEM[i], font=("Times New Roman", 12), variable=bvar[i], bg="#dfe")
    # チェックボックス配置
    cbtn[i].place(x=400, y=160+40*i)

# ウィンドウの表示
root.mainloop()
