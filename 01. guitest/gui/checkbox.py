import tkinter as TKI
import tkinter.messagebox as MessageBox

# チェックの表示
def check():
    if cval.get() == True:
        MessageBox.showinfo("情報", "チェックされています")
        # print("チェックされています")
    else:
        MessageBox.askyesnocancel("情報", "チェックされていません")
        # print("チェックされていません")


"""
 メイン
"""
root = TKI.Tk()
root.title("チェックボックスを扱う")
root.geometry("400x200")

# BooleanVar()のオブジェクトを用意する
cval = TKI.BooleanVar()
cval.set(True)

# チェックボックスの部品作成
checkBox = TKI.Checkbutton(text = "チェックボックス", variable=cval, command=check)
checkBox.pack()

# ウィンドウの表示
root.mainloop()
