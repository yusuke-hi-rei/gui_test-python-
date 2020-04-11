import tkinter as TKI
import random
import winsound as SOUND

"""
 ゲーム変数
"""
# ゲーム進行を管理する
index = 0
# 時間を管理する
timer = 0
# スコアを管理する
score = 0
# 次回セットするネコの値
next_neko = 0
# ハイスコアを管理する
hi_score = 0
# 難易度を管理する
difficulty = 0

"""
 カーソル変数
"""
# カーソルの横方向位置
cursor_x = 0
# カーソルの縦方向位置
cursor_y = 0

"""
 マウス変数
"""
# マウスポインタ X座標
mouse_x = 0
# マウスポインタ Y座標
mouse_y = 0
# マウスクリック UP/DOWNフラグ
mouse_c = 0


# マウスを動かしたときの関数
def mouse_move(event):
    global mouse_x, mouse_y
    mouse_x = event.x
    mouse_y = event.y


# マウスをクリックしたときの関数
def mouse_press(event):
    global mouse_c
    mouse_c = 1

    SOUND.Beep(440, 200) # ラの周波数で0.3秒出力

"""
 マス目管理
"""
neko = []
check = []
for i in range(10):
    neko.append([0, 0, 0, 0, 0, 0, 0, 0])
    check.append([0, 0, 0, 0, 0, 0, 0, 0])
# neko = [
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
# ]


# 表示する関数
def draw_neko():
    cvs.delete("NEKO")

    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]], tag="NEKO")


# 縦、横、斜めに3つ以上並んだか調べる関数
def check_neko():
    for y in range(10):
        for x in range(8):
            check[y][x] = neko[y][x]

    for y in range(1, 9):
        for x in range(8):
            if check[y][x] > 0:
                if check[y-1][x] == check[y][x] and check[y+1][x] == check[y][x]:
                    neko[y-1][x] = 7
                    neko[y][x] = 7
                    neko[y+1][x] = 7

    for y in range(10):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y][x-1] == check[y][x] and check[y][x+1] == check[y][x]:
                    neko[y][x-1] = 7
                    neko[y][x] = 7
                    neko[y][x+1] = 7

    for y in range(1, 9):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y-1][x-1] == check[y][x] and check[y+1][x+1] == check[y][x]:
                    neko[y-1][x-1] = 7
                    neko[y][x] = 7
                    neko[y+1][x+1] = 7
                if check[y+1][x-1] == check[y][x] and check[y-1][x+1] == check[y][x]:
                    neko[y+1][x-1] = 7
                    neko[y][x] = 7
                    neko[y-1][x+1] = 7


# そろったネコを消す関数
def sweep_neko():
    num = 0
    for y in range(10):
        for x in range(8):
            if neko[y][x] == 7:
                neko[y][x] = 0
                num = num + 1
                SOUND.Beep(523, 100) # ドの周波数で0.1秒出力
    return num


# ネコを落下させる関数
def drop_neko():
    flg = False
    for y in range(8, -1, -1):
        for x in range(8):
            if neko[y][x] != 0 and neko[y+1][x] == 0:
                neko[y+1][x] = neko[y][x]
                neko[y][x] = 0
                flg = True
    return flg


# 最上段に達したか調べる関数
def over_neko():
    for x in range(8):
        if neko[0][x] > 0:
            return True
    return False


# 最上段にネコをセットする関数
def set_neko():
    for x in range(8):
        neko[0][x] = random.randint(0, difficulty)


# 影付きの文字列を表示する関数
def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold")
    cvs.create_text(x+2, y+2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)


"""
 タイトルロゴの表示
"""
def game_title_logo():
    # グローバル変数宣言
    global index
    global mouse_c
    draw_txt("ねこねこ", 312, 240, 100, "violet", "TITLE")
    # Easy
    cvs.create_rectangle(168, 384, 456, 456, fill="skyblue", width=0, tag="TITLE")
    draw_txt("Easy", 312, 420, 40, "white", "TITLE")
    # Normal
    cvs.create_rectangle(168, 528, 456, 600, fill="lightgreen", width=0, tag="TITLE")
    draw_txt("Normal", 312, 564, 40, "white", "TITLE")
    # Hard
    cvs.create_rectangle(168, 672, 456, 744, fill="orange", width=0, tag="TITLE")
    draw_txt("Hard", 312, 708, 40, "white", "TITLE")
    #draw_txt("click to start.", 312, 560, 50, "orange", "TITLE")
    index = 1
    mouse_c = 0


"""
 タイトル画面スタート待ち
"""
def game_title_start():
    # グローバル変数宣言
    global index, score, next_neko
    global cursor_x, cursor_y
    global mouse_x, mouse_y, mouse_c
    global difficulty

    difficulty = 0
    if mouse_c == 1:
        if 168 < mouse_x and mouse_x < 456 and 384 < mouse_y and mouse_y < 456:
            difficulty = 4
        if 168 < mouse_x and mouse_x < 456 and 528 < mouse_y and mouse_y < 600:
            difficulty = 5
        if 168 < mouse_x and mouse_x < 456 and 672 < mouse_y and mouse_y < 744:
            difficulty = 6
    if difficulty > 0:
        for y in range(10):
            for x in range(8):
                neko[y][x] = 0
                mouse_c = 0
                score = 0
                next_neko = 0
                cursor_x = 0
                cursor_y = 0
                set_neko()
                draw_neko()
                cvs.delete("TITLE")
                index = 2


"""
 落下
"""
def game_drop():
    # グローバル変数宣言
    global index
    if drop_neko() == False:
        index = 3
    draw_neko()


"""
 揃ったか
"""
def game_pairs():
    # グローバル変数宣言
    global index
    check_neko()
    draw_neko()
    index = 4


"""
 揃ったネコは消す
"""
def game_pair_delete():
    # グローバル変数宣言
    global index, timer, score, next_neko
    global hi_score, difficulty
    sc = sweep_neko()
    score = score + sc * difficulty * 2
    if score > hi_score:
        hi_score = score

    if sc > 0:
        index = 2
    else:
        if over_neko() == False:
            next_neko = random.randint(1, difficulty)
            index = 5
        else:
            index = 6
            timer = 0
    draw_neko()


"""
 マウス入力待ち
"""
def game_mouse_wait():
    # グローバル変数宣言
    global index, next_neko
    global cursor_x, cursor_y
    global mouse_x, mouse_y, mouse_c
    if 24 <= mouse_x and mouse_x < 24+72*8 and 24 <= mouse_y and mouse_y < 24+72*10:
        cursor_x = int((mouse_x-24)/72)
        cursor_y = int((mouse_y-24)/72)
        if mouse_c == 1:
            mouse_c = 0
            set_neko()
            neko[cursor_y][cursor_x] = next_neko
            next_neko = 0
            index = 2

    cvs.delete("CURSOR")
    cvs.create_image(cursor_x*72+60, cursor_y*72+60, image=cursor, tag="CURSOR")
    draw_neko()


"""
 ゲームオーバー
"""
def game_over():
    # グローバル変数宣言
    global index, timer
    timer = timer + 1
    if timer == 1:
        draw_txt("GAME OVER", 312, 348, 60, "red", "OVER")
    if timer == 50:
        cvs.delete("OVER")
        index = 0


# メイン関数
def game_main():
    # グローバル変数宣言
    global index
    global hi_score

    if index == 0:
        """ タイトルロゴの表示 """
        game_title_logo()
    elif index == 1:
        """ タイトル画面スタート待ち """
        game_title_start()
    elif index == 2:
        """ 落下 """
        game_drop()
    elif index == 3:
        """ 揃ったか """
        game_pairs()
    elif index == 4:
        """ 揃ったネコは消す """
        game_pair_delete()
    elif index == 5:
        """ マウス入力待ち """
        game_mouse_wait()
    elif index == 6:
        """ ゲームオーバー """
        game_over()

    # スコア表示を削除
    cvs.delete("INFO")
    # スコア表示
    draw_txt("SCORE" + str(score), 160, 60, 32, "blue", "INFO")
    draw_txt("HISCORE" + str(hi_score), 450, 60, 32, "yellow", "INFO")
    # 次回ネコ表示
    if next_neko > 0:
        cvs.create_image(752, 128, image=img_neko[next_neko], tag="INFO")
    # 0.1秒後にメイン関数実行
    root.after(100, game_main)


root = TKI.Tk()
# ウィンドウタイトル
root.title("落ちものパズル「ねこねこ」")
# ウィンドウサイズ変更不可
root.resizable(False, False)
# マウス移動指定
root.bind("<Motion>", mouse_move)
# マウスクリック指定
root.bind("<ButtonPress>", mouse_press)
# キャンバス設定
cvs = TKI.Canvas(root, width=912, height=768)
# キャンバス配置
cvs.pack()
# root.bind("<ButtonRelease>", mouse_release)

# 背景画像読み込み
bg = TKI.PhotoImage(file="neko_bg.png")
# カーソル画像読み込み
cursor = TKI.PhotoImage(file="neko_cursor.png")
img_neko = [
    None,
    TKI.PhotoImage(file="neko1.png"),
    TKI.PhotoImage(file="neko2.png"),
    TKI.PhotoImage(file="neko3.png"),
    TKI.PhotoImage(file="neko4.png"),
    TKI.PhotoImage(file="neko5.png"),
    TKI.PhotoImage(file="neko6.png"),
    TKI.PhotoImage(file="neko_niku.png")
]

# キャンバス上に背景設定
cvs.create_image(456, 384, image=bg)
# メイン関数
game_main()
# ウィンドウの表示
root.mainloop()

