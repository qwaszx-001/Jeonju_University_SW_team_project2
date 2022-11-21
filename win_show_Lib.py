from tkinter import *

#=====================================설명듣기 버튼을 누를 시 나오는 화면
def show_Contents(title, description):
    """
    title과 description 매개변수를 사용하여
    (title + ' 설명')이라는 제목을 가진 창을 생성하고
    생성된 창에는 description으로 불러온 정보를 출력
    """
    win = Tk()
    win.resizable(False, False)
    win.title(f"{title} 설명")
    content = Label(win, text=description,
                    font=("굴림체", 15), fg="white", bg="dark green")
    content.pack()
    win.mainloop()


def show_window(win, title, description, imgName, floor):
    """
    title, description, imgName, floor 매개변수를 사용하여
    (title + ' 설명')이라는 메인 글을 만든다
    imgName.png를 사용하여 이미지이름.png를 불러온다
    floor는 if문을 사용하여 조건문이 성립할 때 각각 first, second, third에 나타나는 이미지와 불러오는 함수를 생성한다.
    """
    win.destroy()
    win = Tk()
    win.geometry("1000x600")
    win.resizable(False, False)
    win.title(title)

    img = PhotoImage(file=f"{imgName}.png")
    lab = Label(win, image=img)
    lab.place(x=0, y=0)

    Label(win, text=f"{title}에 온걸 환영해!\n 설명을 원한다면 설명듣기 버튼을 눌러봐!", font=("굴림체",20)).pack(side="top",padx=10,pady=20)

    def Back(floor):
        win.destroy()
        if floor == "First":
            from win_firstfloor import firstfloor_page_open
            firstfloor_page_open()
        elif floor == "Second":
            from win_secondfloor import secondfloor_page_open
            secondfloor_page_open()
        elif floor == "Third":
            from win_thirdfloor import thirdfloor_page_open
            thirdfloor_page_open()

    
    if floor == "First":
        img1=PhotoImage(file="제트.png")
        lab1=Label(win,image=img1)
        lab1.place(x=813,y=320)
    elif floor == "Second":
        img1=PhotoImage(file="벼리.png")
        lab1=Label(win,image=img1)
        lab1.place(x=800,y=328)
    elif floor == "Third":
        img1=PhotoImage(file="제이제이.png")
        lab1=Label(win,image=img1)
        lab1.place(x=800,y=320)
    
    '''
    lamda함수를 이용하여 설명듣기 버튼이 눌렸을 때 show_Contents의 title과 description에 저장된 내용들을 불러온다
    lamda함수를 이용하여 Back 버튼이 눌렸을 때 함수 Back(floor)을 불러와 층을 고르는 화면으로 이동된다.
    '''
    Button(win, text="설명듣기", font=("굴림체", 20), command=lambda: show_Contents(title, description)).place(x=830, y=540)
    Button(win, text="Back", font=("굴림체",20),command=lambda: Back(floor)).pack(side="bottom",padx=10,pady=20)

    win.mainloop()