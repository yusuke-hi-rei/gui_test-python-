import tkinter as TKI
import tkinter.messagebox as MessageBox

key = ""
mx = 1
my = 1
MAX_YUKA_COUNT = 30
maxYuka = MAX_YUKA_COUNT

def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global mx, my, maxYuka
    """
     左SHIFTキー押下
    """
    if key == "Shift_L" and maxYuka < MAX_YUKA_COUNT:
        canvas.delete("PAINT")
        mx = 1
        my = 1
        maxYuka = MAX_YUKA_COUNT
        for y in range(7):
            for x in range(10):
                if maze[y][x] == 2:
                    maze[y][x] = 0
    """
     通路を通った処理
    """
    if key == "Up" and maze[my-1][mx] == 0:
        my = my - 1
    if key == "Down" and maze[my+1][mx] == 0:
        my = my + 1
    if key == "Left" and maze[my][mx-1] == 0:
        mx = mx - 1
    if key == "Right" and maze[my][mx+1] == 0:
        mx = mx + 1
    # キャラクターのいる場所が通路なら、値を２にし、ピンク色にする
    if maze[my][mx] == 0:
        maze[my][mx] = 2
        # 通った通路はピンク色にする
        canvas.create_rectangle(mx*80, my*80, mx*80+79, my*80+79, fill="pink", width=0, tag="PAINT")
        # 通っていない通路の計算
        maxYuka = maxYuka - 1

    # 一旦キャラクタを削除
    canvas.delete("MYCHR")
    # 再度キャラクタの画像を表示する
    canvas.create_image(mx*80+40, my*80+40, image=img, tag="MYCHR")
    if maxYuka == 0:
        canvas.update()
        MessageBox.showinfo("Congratulations！", "すべての通路を通りました！")
        return
    #canvas.coords("MYCHR", mx*80+40, my*80+40)
    root.after(100, main_proc)

root = TKI.Tk()
root.title("迷路内を移動する")

root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

canvas = TKI.Canvas(width=800, height=560, bg="white")
canvas.pack()

"""
 迷路
"""
maze = [
    [1] * 10,
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1] * 10
]
# 迷路の表示
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x*80, y*80, x*80+79, y*80+79, fill="skyblue", width=0)

img = TKI.PhotoImage(file="mimi_s.png")
canvas.create_image(mx*80+40, my*80+40, image=img, tag="MYCHR")
main_proc()

root.mainloop()
