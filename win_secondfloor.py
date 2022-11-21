from tkinter import *

descriptions = {
    "자유열람실1": '\n\n 자유열람실1 - Free Reading Room 1\n\n'
    '오픈형 열람테이블240석과 캐럴형 1인테이블 98석이 배치 되어\n 학생들이 자유롭게 공부할 수 있는 열람실이야!\n\n\n',
    "자유열람실2": '\n\n 자유열람실2 - Free Reading Room 2\n\n'
    '오픈형 열람테이블 254석, 캐럴형1인테이블 78석이 배치된\n 자유로운 독서와 공부가 가능한 열람실이야!\n\n\n',
    "노트북존": '\n\n 노트북존 - Labtop Available Zone\n\n'
    "무선랜과 전원이 구비 된 노트북 전용열람실142석이 있는 노트북 열람실이야!\n\n\n",
    "유피아": '\n\n 유피아(로비) - Upia(Lobby)\n\n'
    "휴식공간이면서 무선충전데스크, 전광판, 수퍼스타존 등\n 다양한 역할을 하고 있는 도서관의 로비야!\n\n\n",
    "대출실": '\n\n 대출실 - Check-out Center\n\n'
    "대출과 반납, 자료이용안내 등을 알려주는 카운터야.\n 도서관에 대해 궁금한 게 있다면 이 곳을 찾아 와!\n\n\n",
    "학술정보운영실": '\n\n 학술정보운영실 - Academic Information Management Office \n\n'
    "다양한 학술 정보들을 관리하는 사무실이야!\n\n\n",
    "회의실": '\n\n 회의실 - Conference Room\n\n'
    "관장실과 회의실이 있고 회의를 할 수 있는 곳이야!\n\n\n",
    "스터디룸": '\n\n 스터디룸 - Group Study Rooms\n\n'
    "스터디룸(5개),화이트보드 TV 및 화상회의 카메라가 있고\n 노트북 대여도 가능해서 친구들과 함께 공부할 수 있는 곳이야!\n\n\n",
    "베스트셀러/신착도서": '\n\n 베스트셀러/신착도서 - Bestseller/Brand-new Books\n\n'
    "신간도서 및 베스트셀러를 쉽고 빠르게 볼 수 있는 곳이야!\n\n\n",
    "강의지정도서": '\n\n 강의지정도서 - Lecture References\n\n'
    "학기별로 수업에 사용되고 있는 강의교재 및 참고문헌을 빌릴 수 있는 곳이야!\n \n\n\n",
    "PC존": '\n\n PC존 - PC Zone\n\n'
    "어플로 예약 후 컴퓨터를 사용할 수 있는 PC존이야!\n\n\n",
    "JJ권장도서": '\n\n JJ권장도서 - JJ Recommanded Books\n\n'
    "교양추천 100선, 학과추천 482선 등\n 학교에서 추천하는 권장도서를 볼 수 있는 곳이야! \n\n\n",
    "사회과학": '\n\n 사회과학 - Social Science\n\n'
    "사회과학(000~500번대)에 관련된 자료를 볼 수 있는 사회과학자료실이야!\n\n\n",
    "어문학": '\n\n 어문학 - Linguistics & Literatures\n\n'
    "어문학(600~900번대)에 관련된 자료를 볼 수 있는 어문학자료실이야!\n\n\n"
}
#descriptions를 사용하여 ("제목":"설명") 형식으로 제목과 title 이름이 같을 때 설명을 불러온다


#======================================2층 화면
def secondfloor_page_open():
    from win_show_Lib import show_window
    #win_show_Lib 모듈의 show_window함수 호출
    win = Tk()
    win.geometry("1000x552")
    win.resizable(False, False)
    img = PhotoImage(file="2.png")
    lab = Label(win, image=img)
    lab.place(x=0, y=0)
    win.title("전주대 애플리케이션")
    Header = Label(win, text="2층에 오신것을\n 환영합니다!", font=(
        "굴림체", 24), fg="black", bg="white")
    Header.place(x=100, y=70)

    #버튼 구현을 위해 이미지 리스트화
    img1 = [PhotoImage(file="자유열람실1.png"), PhotoImage(file="자유열람실2.png"), PhotoImage(file="노트북존.png"), PhotoImage(file="유피아.png"),
            PhotoImage(file="대출실.png"), PhotoImage(file="학술정보운영실.png"), PhotoImage(file="회의실.png"), PhotoImage(file="스터디룸.png"), PhotoImage(file="베스트셀러버튼.png"),
            PhotoImage(file="강의지정도서.png"), PhotoImage(file="PC존2.png"), PhotoImage(file="JJ권장도서.png"), PhotoImage(file="사회과학.png"), PhotoImage(file="어문학.png")]

    img2 = PhotoImage(file='벼리.png')
    Star = Label(win, image=img2)
    Star.place(x=90, y=135)

    # show_window(win, title, description,  imgName, floor)
    #            (창,   제목,      설명,      이미지 이름,  층)
    #lamda함수를 이용하여 버튼이 눌렸을 때 descriptions에 있는 설명과 이미지 이름을 가져오고 if 조건문에 성립하는 결과값을 가져온다.
    Button(win, image=img1[0], command=lambda: show_window(win, "자유열람실1", descriptions["자유열람실1"], "열람실2이미지", "Second")).place(x=500, y=420)
    Button(win, image=img1[1], command=lambda: show_window(win, "자유열람실2", descriptions["자유열람실2"], "열람실2이미지", "Second")).place(x=290, y=470)
    Button(win, image=img1[2], command=lambda: show_window(win, "노트북존", descriptions["노트북존"], "노트북존이미지", "Second")).place(x=410, y=360)
    Button(win, image=img1[3], command=lambda: show_window(win, "유피아(로비)", descriptions["유피아"], "유피아이미지", "Second")).place(x=570, y=320)
    Button(win, image=img1[4], command=lambda: show_window(win, "대출실", descriptions["대출실"], "대출실이미지", "Second")).place(x=620, y=291)
    Button(win, image=img1[5], command=lambda: show_window(win, "학술정보운영실", descriptions["학술정보운영실"], "학술정보운영실이미지", "Second")).place(x=550, y=240)
    Button(win, image=img1[6], command=lambda: show_window(win, "회의실", descriptions["회의실"], "회의실이미지", "Second")).place(x=590, y=205)
    Button(win, image=img1[7], command=lambda: show_window(win, "스터디룸", descriptions["스터디룸"], "스터디룸이미지", "Second")).place(x=623, y=175)
    Button(win, image=img1[8], command=lambda: show_window(win, "베스트셀러/신착도서", descriptions["베스트셀러/신착도서"], "베스트셀러", "Second")).place(x=615, y=250)
    Button(win, image=img1[9], command=lambda: show_window(win, "강의지정도서", descriptions["강의지정도서"], "강의지정도서이미지", "Second")).place(x=650, y=230)
    Button(win, image=img1[10], command=lambda: show_window(win, "PC존", descriptions["PC존"], "PC존이미지", "Second")).place(x=670, y=270)
    Button(win, image=img1[11], command=lambda: show_window(win, "JJ권장도서", descriptions["JJ권장도서"], "권장도서", "Second")).place(x=695, y=315)
    Button(win, image=img1[12], command=lambda: show_window(win, "사회과학", descriptions["사회과학"], "입구자료실", "Second")).place(x=710, y=205)
    Button(win, image=img1[13], command=lambda: show_window(win, "어문학", descriptions["어문학"], "자료실3", "Second")).place(x=615, y=46)

    
    #command를 이용하여 win창을 닫고 win_selectfloor 모듈의 select 함수 호출
    def selectfloor():
        win.destroy()
        from win_selectfloor import select
        select()
    Button(win, text="Back",font=("굴림체",20), command=selectfloor).pack(side="bottom",padx=10,pady=20)

    win.mainloop()