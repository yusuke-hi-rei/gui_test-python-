import tkinter as TKI

pnum = 0
def PhotoGraph():
    global pnum
    canvas.delete("PH")
    canvas.create_image(400, 300, image=photo[pnum], tag="PH")
    pnum = pnum + 1
    if pnum >= len(photo):
        pnum = 0
    root.after(7000, PhotoGraph)


"""
 メイン
"""
root = TKI.Tk()
# ウィンドウタイトル
root.title("デジタルフォトフレーム")

# キャンバス作成
canvas = TKI.Canvas(root, width=800, height=600)
# キャンバス配置
canvas.pack()

photo = [
    TKI.PhotoImage(file="cat00.png"),
    TKI.PhotoImage(file="cat01.png"),
    TKI.PhotoImage(file="cat02.png"),
    TKI.PhotoImage(file="cat03.png"),
]
PhotoGraph()

# ウィンドウの表示
root.mainloop()
