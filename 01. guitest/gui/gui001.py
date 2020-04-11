import tkinter as TKI


def click_btn():
    # 入力欄の文字列を変数txtに代入
    txt = entry.get()
    # ボタンの文字列をtxtの値にする
    button["text"] = txt


"""
 メイン
"""
root = TKI.Tk()
root.title("はじめてのテキスト入力欄")
root.geometry("400x200")
# 半角20文字分の入力欄の部品作成
entry = TKI.Entry(width=20)
# 入力欄の配置
entry.place(x=10, y=10)

# ボタンの部品作成
button = TKI.Button(text="文字列の取得", command=click_btn)
button.place(x=20, y=100)

# ウィンドウの表示
root.mainloop()
