import random
import tkinter as tk
from PIL import Image, ImageTk

PLAY_OPTIONS = {1: "가위", 2: "바위", 3: "보"}

root = tk.Tk()
root.title("가위바위보")
root.geometry("300x500")

random_img = ImageTk.PhotoImage(Image.open("mO3ouHJ2BjWxmYyRyb36ER85dZyedrAGMdGzDkX9oU55FDEXJQJ9ozt8WPRWwGmDBn5HOqZxAkZOS9_RGNf34A.png").resize((300, 300)))
scissors_img = ImageTk.PhotoImage(Image.open("thumb_d_D5F5D7D0282C09168B45BD59E9C7A506.png").resize((300, 300)))
rock_img = ImageTk.PhotoImage(Image.open("Rock-PNG-Transparent-Image.png").resize((300, 300)))
paper_img = ImageTk.PhotoImage(Image.open("49452836-furoshiki-wrapping-goods.jpg").resize((300, 300)))

images = {
    1: scissors_img,
    2: rock_img,
    3: paper_img
}

label = tk.Label(root, image=random_img)
label.pack()
label2 = tk.Label(root, text="내 선택을 골라줘!")
label2.pack()


def on_click(user_choice):
    comp_choice = random.randint(1, 3)
    label.config(image=images[comp_choice])

    if user_choice == comp_choice:
        result = "무승부"
    elif (user_choice - comp_choice) % 3 == 1:
        result = "승리"
    else:
        result = "패배"
    label2.config(text=f"결과: {result} (컴퓨터: {PLAY_OPTIONS[comp_choice]})")


btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
for num, text in PLAY_OPTIONS.items():
    tk.Button(btn_frame, text=text, command=lambda n=num: on_click(n)).pack(side=tk.LEFT, padx=5)

root.mainloop()
