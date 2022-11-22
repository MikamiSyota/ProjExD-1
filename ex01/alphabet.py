import random
import datetime
taisyou = 0
kesson = 0

def setup():#対象文字数、欠損文字数の決定を行う
    global taisyou, kesson
    #taisyou = random.randint(1,26) #対象文字数をランダムに決定する場合に使用
    taisyou = 8
    #kesson = random.randint(0, taisyou) #欠損文字数をらんだむに決定する場合に使用
    kesson = 2
    
def syutudai():#問題を出題する
    all = [chr(ord("A")+i) for i in range(26)] #すべてのアルファベットを含むリスト
    x = random.sample(all, taisyou)   #allリストから対象文字数の数だけ抜き出したリスト     
    print("対象文字列")
    print_list(x)
    print()
    print("表示文字列")
    y = random.sample(x, taisyou-kesson)#対象文字数のリストから表示する文字を抜き出したリスト
    print_list(y)
    print()
    return x,y

def kaitou():#欠損文字数の回答を受け付ける
    ans = int(input("欠損文字はいくつあるでしょうか？"))
    if ans == kesson:
        print("正解です。それでは、具体的に欠損文字を１つずつ入力してください。")
        return 
    else:
        print("不正解です。またチャレンジしてください。")
        return False

def moji_kaitou(mondai):#欠損文字の回答を受け付ける
    for i in range(kesson):
        you = input(f"{i+1}個目の文字を入力してください：")
        if you not in mondai[1] and you in mondai[0]:
            mondai[0].pop(mondai[0].index(you))
        else:
            print("不正解です。またチャレンジしてください")
            return True
        
    print("正解です")
    return False
    
def print_list(h_list):#リストを１列に表示する関数
    for i in range(len(h_list)):
        print(h_list[i], end=" ")

if __name__ == "__main__":
    st = datetime.datetime.now()
    setup()
    while True:#正答の場合While文を抜ける
        mondai = syutudai()
        if kaitou() == False:
            break
        if moji_kaitou(mondai) == False:
            break
    ed = datetime.datetime.now()
    print(f"回答時間：{(ed-st).seconds}秒でした")