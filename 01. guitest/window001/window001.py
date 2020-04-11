# tkinterモジュールのインポート
import tkinter
import tkinter.font as fonts

"""
関数 ボタンクリック
"""
def click_btn():
    button["text"] = "クリックしました"


"""
ウインドウオブジェクト作成
"""
root = tkinter.Tk()
# ウインドウタイトル設定
root.title("初めてのウインド")
# ウインドウサイズ設定
root.geometry("800x600")
"""
キャンバスの部品作成
"""
canvas = tkinter.Canvas(root, width=600, height=600, bg="skyblue")
# ウィンドウにキャンバスの配置
canvas.pack()
"""
画像ファイルの読み込み
"""
picture = tkinter.PhotoImage(file="iroha.png")
# 画像の中心位置で画像を描画
canvas.create_image(300, 300, image=picture)
"""
ラベルの部品作成
"""
label = tkinter.Label(root, text="ラベルの文字列", font=("System", 24))
# ラベルの配置
label.place(x=200, y=100)
"""
ボタンの部品作成
"""
button = tkinter.Button(root, text="ボタンの文字列", font=("Times New Roman", 24), command=click_btn)
# ボタンの配置
button.place(x=200, y=250)

"""
 メイン関数
"""
def main():
    # 使用できるフォントをコンソールへ表示
    print(fonts.families())
    """
    ウインドウの表示
    """
    root.mainloop()


if __name__ == '__main__':
    main()
