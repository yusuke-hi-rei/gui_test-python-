import tkinter as TKI

# Global変数
# タイマー値
tmr = 0
# キー入力
key = 0


# タイマー関数
def count_up():
    # Global変数を関数内で使用
    global tmr
    tmr = tmr + 1
    label["text"] = tmr
    root.after(1000, count_up)

# キー入力関数
def key_down(event):
    global key
    key = event.keycode
    # コンソールにkey値を表示
    print("KEY:" + str(key))


root = TKI.Tk()
label = TKI.Label(font=("Times New Roman", 80))
label.pack()
# 1秒おきにcount_up関数の呼び出し
root.after(1000, count_up)

# キーを押したときに実行する関数
root.bind("<KeyPress>", key_down)
""" 
 他のキーイベント
 <KeyRelease> : キーを離したとき
 <Motion> : マウスポインタを動かしたとき
 <ButtonPress> or <Button> : マウスボタンをクリック
"""

# ウィンドウの表示
root.mainloop()
