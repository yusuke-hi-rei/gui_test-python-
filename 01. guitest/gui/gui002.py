import tkinter as TKI


def click_btn():
    text.insert(TKI.END, "モンスターが現れた！")


"""
 メイン
"""
root = TKI.Tk()
root.title("複数行のテキスト入力")
root.geometry("400x200")

# ボタンの部品作成
button = TKI.Button(text="メッセージ", command=click_btn)
button.pack()
text = TKI.Text()
text.pack()

# ウィンドウの表示
root.mainloop()
