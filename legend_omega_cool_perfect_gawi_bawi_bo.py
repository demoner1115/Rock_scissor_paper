import random
import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("가위바위보")
root.geometry("300x500")

# 이미지 로딩 및 리사이즈
random_image = ImageTk.PhotoImage(Image.open("mO3ouHJ2BjWxmYyRyb36ER85dZyedrAGMdGzDkX9oU55FDEXJQJ9ozt8WPRWwGmDBn5HOqZxAkZOS9_RGNf34A.png").resize((300, 300)))
first_image = ImageTk.PhotoImage(Image.open("thumb_d_D5F5D7D0282C09168B45BD59E9C7A506.png").resize((300, 300)))
second_image = ImageTk.PhotoImage(Image.open("Rock-PNG-Transparent-Image.png").resize((300, 300)))
third_image = ImageTk.PhotoImage(Image.open("49452836-furoshiki-wrapping-goods.jpg").resize((300, 300)))

# 라벨 1개만 만들기 (이미지 출력용)
label = tk.Label(root, image=random_image)
label.pack()

# 텍스트 라벨
label2 = tk.Label(root, text="랜덤뽑기")
label2.pack()

choose = 0
# 이미지 변경 함수
rrandom = random.randint(1, 3)
if rrandom == 1:
    choose = 1
elif rrandom == 2:
    choose = 2
elif rrandom == 3:
    choose = 3

# 버튼 함수
def click_btn1():
    if choose == 1:
        label.config(image=first_image)
        label2.config(text="무승부")
    elif choose == 3:
        label.config(image=third_image)
        label2.config(text="승리")
    else:
        label.config(image=second_image)
        label2.config(text="패배")
def click_btn2():
    if choose == 2:
        label.config(image=second_image)
        label2.config(text="무승부")
    elif choose == 1:
        label.config(image=first_image)
        label2.config(text="승리")
    else:
        label.config(image=third_image)
        label2.config(text="패배")

def click_btn3():
    if choose == 3:
        label.config(image=third_image)
        label2.config(text="무승부")
    elif choose == 2:
        label.config(image=second_image)
        label2.config(text="승리")
    else:
        label.config(image=first_image)
        label2.config(text="패배")

# 버튼 생성 및 배치
btn1 = tk.Button(root, text="가위", command=click_btn1)
btn2 = tk.Button(root, text="바위", command=click_btn2)
btn3 = tk.Button(root, text="보", command=click_btn3)

btn1.pack(pady=5)
btn2.pack(pady=5)
btn3.pack(pady=5)

root.mainloop()
