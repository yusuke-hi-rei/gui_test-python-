import tkinter as TKI
import random


def click_btn():
    """ ボタンクリック """
    label["text"] = random.choice(["大吉", "中吉", "小吉", "凶"])
    label.update()

"""
 ウィンドウオブジェクト作成
"""
root = TKI.Tk()
"""
 タイトル設定
"""
root.title("おみくじソフト")
"""
 ウィンドサイズの固定(リサイズ不可) False(横不許可), False(縦不許可)
"""
root.resizable(False, False)
"""
 キャンバス作成
"""
canvas = TKI.Canvas(root, width=800, height=600)
# キャンバスの配置
canvas.pack()
"""
 画像読み込み
"""
picture = TKI.PhotoImage(file="miko.png")
# 画像の配置
canvas.create_image(400, 300, image=picture)
"""
 ラベルの配置
"""
label = TKI.Label(root, text="？？", font=("Times New Roman", 120), bg="white")
label.place(x=380, y=60)
"""
 ボタンの配置
"""
button = TKI.Button(root, text="おみくじを引く", font=("Times New Roman", 36), command=click_btn, fg="skyblue")
button.place(x=360, y=400)

"""
 ウィンドウの表示
"""
root.mainloop()
