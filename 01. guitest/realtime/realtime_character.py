import tkinter as TKI

# Global変数
# キー入力
key = ""


# キー入力関数
def key_down(event):
    global key
    key = event.keysym
    # コンソールにkey値を表示
    #print("KEY:" + str(key))


def key_up(event):
    global key
    key = ""


cx = 400
cy = 300
def main_proc():
    global cx, cy
    if key == "Up":
        cy = cy - 20
    if key == "Down":
        cy = cy + 20
    if key == "Left":
        cx = cx - 20
    if key == "Right":
        cx = cx + 20
    canvas.coords("MYCHR", cx, cy)
    root.after(100, main_proc)


root = TKI.Tk()
root.title("キャラクターの移動")
# キーを押したときに実行する関数
root.bind("<KeyPress>", key_down)
# キーを離したときに実行する関数
root.bind("<KeyRelease>", key_up)
""" 
 他のキーイベント
 <KeyRelease> : キーを離したとき
 <Motion> : マウスポインタを動かしたとき
 <ButtonPress> or <Button> : マウスボタンをクリック
"""
# キャンバスの作成
canvas = TKI.Canvas(width=800, height=600, bg="lightgreen")
canvas.pack()
# 画像の読み込み
img = TKI.PhotoImage(file="mimi.png")
canvas.create_image(cx, cy, image=img, tag="MYCHR")

main_proc()

# ウィンドウの表示
root.mainloop()
