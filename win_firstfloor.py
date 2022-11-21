from tkinter import *

descriptions = {
    "주차장": '\n\n 주차장 - Parking Lots \n\n'
    "● C03 구역 앞 엘리베이터를 타고\n 2층으로 오면 출입구가 있어.\n" '\n'
    "● D90 구역 앞 계단으로 3층까지 올라오면\n 도서관 3층 출입구가 있어.\n" '\n'
    "● D79 구역 쪽에 있는 엘리베이터를 타고\n 3층으로 오면 도서관 3층 출입구가 있어.\n\n\n",
    
    "보존서고": '\n\n 보존서고 - Preseved Library \n\n'
    "출판년이 오래된 자료, 개정판이 나온 구판,\n"
    "대출빈도가 낮은 도서 등 이용이 저조한 도서를 보관하는 곳이야.\n"
    "폐가제 운영이라 함부로 들어갈 순 없어!\n\n\n"
}
#descriptions를 사용하여 ("제목":"설명") 형식으로 제목과 title 이름이 같을 때 설명을 불러온다

#======================================1층 화면
def firstfloor_page_open():
    from win_show_Lib import show_window
    #win_show_Lib 모듈의 show_window함수 호출
    win = Tk()
    win.geometry("1000x552")
    win.resizable(False, False)
    img1 = PhotoImage(file="1.png")
    lab1 = Label(win, image=img1)
    lab1.place(x=0, y=0)
    win.title("전주대 애플리케이션")
    Header = Label(win, text="1층에 오신것을\n 환영합니다!", font=(
        "굴림체", 24), fg="black", bg="white")
    Header.place(x=100, y=70)

    # 버튼 구현을 위해 이미지 리스트화
    img2 = [PhotoImage(file="보존서고.png"), PhotoImage(file="주차장.png")]

    img3 = PhotoImage(file='제트.png')
    Zet = Label(win, image=img3)
    Zet.place(x=840, y=320)

    # show_window(win, title, description,  imgName, floor)
    #            (창,   제목,    설명,     이미지 이름,  층)
    #lamda함수를 이용하여 버튼이 눌렸을 때 descriptions에 있는 설명과 이미지 이름을 가져오고 if 조건문에 성립하는 결과값을 가져온다.
    Button(win, image=img2[0], command=lambda: show_window(win, "보존서고", descriptions["보존서고"], "보존서고이미지", "First")).place(x=675, y=170)
    Button(win, image=img2[1], command=lambda: show_window(win, "주차장", descriptions["주차장"], "지하주차장2", "First")).place(x=230, y=270)

    #command를 사용해 Back버튼을 누를시 selectfloor 호출하여 win창을 닫고 win_selectfloor 모듈의 select 함수 호출
    def selectfloor():
        win.destroy()
        from win_selectfloor import select
        select()
    Button(win, text="Back", font=("굴림체",20), command=selectfloor).pack(side="bottom",padx=10,pady=20)

    win.mainloop()