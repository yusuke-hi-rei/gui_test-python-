import tkinter as TKI

# Global変数
# キー入力
key = ""


def main_proc():
    label["text"] = key
    root.after(100, main_proc)


# キー入力関数
def key_down(event):
    global key
    key = event.keysym
    # コンソールにkey値を表示
    #print("KEY:" + str(key))


root = TKI.Tk()
root.title("リアルタイムキー入力")
# キーを押したときに実行する関数
root.bind("<KeyPress>", key_down)
""" 
 他のキーイベント
 <KeyRelease> : キーを離したとき
 <Motion> : マウスポインタを動かしたとき
 <ButtonPress> or <Button> : マウスボタンをクリック
"""

label = TKI.Label(font=("Times New Roman", 80))
label.pack()

main_proc()

# ウィンドウの表示
root.mainloop()
