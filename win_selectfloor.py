from tkinter import*
from win_firstfloor import firstfloor_page_open
from win_secondfloor import secondfloor_page_open
from win_thirdfloor import thirdfloor_page_open
#================================================층 고르는 화면
def select():
    win = Tk()
    win.resizable(width=0, height=0)
    img2 = PhotoImage(file = "a.png")
    lab2 = Label(win, image=img2)
    lab2.pack()
    win.title("전주대 애플리케이션")

    Header = Label(win, text="층을 선택해주세요", font=("굴림체", 30), fg="black",bg="white")
    Header.place(x=220, y=70)

    def firstfloor():
        win.destroy()
        firstfloor_page_open()

    #command를 사용해 firstfloor 호출하여 win창을 닫고 win_firstfloor 모듈의 firstfloor_page_open 함수 호출
    first = Button(win, text="1층", font=(None,15), fg="black",bg="yellow",command=firstfloor) 
    first.place(x=60, y=350)
    First = Label(win, text = "보존서고,주차장", font = ("굴림체",15), fg="black", bg="white")
    First.place(x=122,y=350)

    def secondfloor():
        win.destroy()
        secondfloor_page_open()

    #command를 사용해 secondfloor 호출하여 win창을 닫고 win_secondfloor 모듈의 secondfloor_page_open 함수 호출
    second = Button(win, text="2층", font=(None,15), fg="black",bg="yellow",command=secondfloor)#도서관 2층 화면으로 이동
    second.place(x=60, y=250)
    Second = Label(win, text = "유피아, 도서관자치위원회실, 자유열람실, 노트북존, 대출실, \nJJ권장도서, 베스트셀러/산착도서, 강의지정도서, 일반자료실, 스터디룸, \n관장실 및 회의실, 학술정보운영실, PC존", font = ("굴림체",15), fg="black",bg="white")
    Second.place(x=124,y=250)

    def thirdfloor():
        win.destroy()
        thirdfloor_page_open()
        
    #command를 사용해 thirdfloor 호출하여 win창을 닫고 winthirdtfloor 모듈의 thirdfloor_page_open 함수 호출
    third = Button(win, text="3층", font=(None, 15), fg="black",bg="yellow",command=thirdfloor)#도서관 3층 화면으로 이동
    third.place(x=60, y=150)
    Third = Label(win, justify="left",text="기독교 자료실, 고서실, 특수자료실, Kids English Zone, 구름다리, \n원문검색PC,국내·외 연속간행물, 학위논문, 서양서자료실, 참고자료실, \n미디어밸리,그래픽노블존, HATCH Lounge, 하늘정원, 소극장, 미디어자료실, GX룸", font=("굴림체",15), fg="black", bg="white")
    Third.place(x=124,y=150)

    def Back():
        win.destroy()
        from win_main import showMain
        showMain()
    #command를 사용해 Back버튼을 누를 시 Back 호출하여 win창을 닫고 win_main 모듈의 showMain 함수 호출
    Button(win, text="Back",font=("굴림체",20), command=Back).pack(side="bottom")

    win.mainloop()