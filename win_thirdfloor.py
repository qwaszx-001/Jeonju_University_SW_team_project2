from tkinter import *

descriptions = {
    "기독교자료실":'\n\n 기독교자료실 - Christian Archive \n\n'
    "기독교 및 종교 관련 모든 유형의 자료(200번대)가 비치된 자료실이야.\n\n\n",
    "고서실":'\n\n 고서실 - Old Books Archive \n\n'
    "고문헌자료실이고 원하는 자료검색 후 사서에게 의뢰하여 열람이 가능해!\n 하지만 대출은 불가능하니 유의하도록 해.\n\n\n",
    "Kids English Zone":'\n\n Kids English Zone \n\n'
    "지역주민을 위한 어린이영어도서자료가 구비되어 있어!\n\n\n",
    "구름다리":'\n\n 구름다리 - Skybridge \n\n'
    "기독교 자료실 및 서양서자료실을 미디어밸리와 이어주는 연결통로야.\n 가끔 행사가 있을 때 다양한 관련 전시가 진행되기도 해!\n\n\n",
    "국내·외 연속간행물(기간호) 및 학위논문":'\n\n 학술지 및 학위논문 - Academic Journals & Theses \n\n'
    "국내·외 발간 연속간행물(학술지, 논문집 등) 자료들의 열람이 가능해!\n\n\n",
    "학위논문":'\n\n 학위논문 - Dissertations \n\n'
    "전주대학교 석·박사 학위논문 자료를 찾아볼 수 있어!\n\n\n",
    "국내·외 연속간행물(최신호)":'\n\n 연속간행물(최신호) - Magazines \n\n'
    "국내·외 발간 연속간행물(교양잡지,학술지 등) 및 최신자료들을 가장 쉽게 접해 볼 수 있어!\n\n\n",
    "하늘정원":'\n\n 하늘정원 - Heaven Garden \n\n'
    "야외수업 및 휴식공간, 영화상영, 음악회 등 정기적인 문화행사가 진행되는 곳이야!\n\n\n",
    "서양서자료실":'\n\n 서양서자료실 - Western Archive \n\n'
    "영어, 독어, 불어 등 다양한 외국원서 자료들을 열람할 수 있어!\n\n\n",
    "참고자료실":'\n\n 참고자료실 - References \n\n'
    "사전류, 연감, 연보, 각종 통계, 규격, 법령집 등의 자료를 열람할 수 있어!\n\n\n",
    "E-learning존":'\n\n E-learning존 - E-learning Zone \n\n'
    "PC존에서 비대면 수업을 들을 수 있는 곳이야.\n 어플에서 예약 후 사용이 가능해!\n\n\n",
    "미디어밸리":'\n\n 미디어밸리 - Media Valley \n\n'
    "DVD감상석(2인, 4인, 6인)에서 친구들과 언제든 DVD를 시청할 수 있어!\n\n\n",
    "그래픽노블존":'\n\n 그래픽노블존 - Graphic Novels Zone \n\n'
    "마블,DC,스타워즈 등 만화 원서의 번역본을 무료로 감상할 수 있어!\n\n\n",
    "HATCH Lounge":'\n\n HATCH Lounge \n\n'
    "VR게임, 3D프린터, VOD서비스, 누워서 휴식이 가능한 공간들로 구성되어 있어!\n\n\n",
    "소극장":'\n\n 소극장 - Little Theater \n\n'
    "매 달 영화상영 진행 및 다양한 행사 진행 등\n 여러 문화생활을 즐길 수 있어!\n\n\n",
    "미디어자료실":'\n\n 미디어자료실 - Media Archive \n\n'
    "DVD를 대여해서 전주대학교 학생이라면\n 누구든지 자유로운 영화관람이 가능해!\n\n\n",
    "GX룸":'\n\n GX룸 - Group Exercise Room \n\n'
    "종종 다양한 문화행사가 진행되는 곳이야!\n\n\n",
    "원문검색 PC":'\n\n 원문검색 PC - PC for Retrieving Original Texts \n\n'
    "국회도서관 원문검색이 가능한 전용 PC들이 구비되어 있어!\n\n\n"
}
#descriptions를 사용하여 ("제목":"설명") 형식으로 제목과 title 이름이 같을 때 설명을 불러온다

#======================================3층 화면
def thirdfloor_page_open():
    from win_show_Lib import show_window 
    #win_show_Lib 모듈의 show_window함수 호출
    win = Tk()
    win.geometry("1000x552")
    win.resizable(False, False)
    bgImg = PhotoImage(file="3.png")
    lab1 = Label(win, image=bgImg)
    lab1.place(x=0, y=0)
    win.title("전주대 애플리케이션")
    Header = Label(win, text="3층에 오신것을\n 환영합니다!", font=(
        "굴림체", 24), fg="black", bg="white")
    Header.place(x=100, y=70)

    #버튼 구현을 위해 이미지 리스트화
    img1 = [PhotoImage(file='GX룸버튼.png'), PhotoImage(file='하늘정원버튼.png'), PhotoImage(file='연속간행물(기간호)버튼.png'), PhotoImage(file='해치라운지버튼.png'), 
            PhotoImage(file='연속간행물버튼(최신호).png'), PhotoImage(file='고서실버튼.png'), PhotoImage(file='구름다리버튼.png'), PhotoImage(file='그래픽노블버튼.png'), 
            PhotoImage(file='기독교자료실버튼.png'), PhotoImage(file='미디어자료실버튼.png'), PhotoImage(file='서양서버튼.png'), PhotoImage(file='소극장버튼.png'),
            PhotoImage(file='미디어밸리버튼.png'), PhotoImage(file='원문검색버튼.png'), PhotoImage(file='이러닝존버튼.png'), PhotoImage(file='참고자료실버튼.png'), PhotoImage(file='키즈영어존버튼.png')]
    # 제이제이 이미지 띄우기
    img2 = PhotoImage(file='제이제이.png')
    Jay = Label(win, image=img2)
    Jay.place(x=90, y=135)

    # show_window(win, title, description,  imgName, floor)
    #            (창,   제목,      설명,      이미지 이름,  층)
    #lamda함수를 이용하여 버튼이 눌렸을 때 descriptions에 있는 설명과 이미지 이름을 가져오고 if 조건문에 성립하는 결과값을 가져온다.
    Button(win, image=img1[0], command=lambda: show_window(win, "GX룸", descriptions["GX룸"], "GX", "Third")).place(x=254, y=440)
    Button(win, image=img1[2], command=lambda: show_window(win, "국내·외 연속간행물(기간호) 및 학위논문", descriptions["국내·외 연속간행물(기간호) 및 학위논문"], "기간호_학위논문", "Third")).place(x=620, y=217)
    Button(win, image=img1[3], command=lambda: show_window(win, "HATCH Lounge", descriptions["HATCH Lounge"], "해치라운지3", "Third")).place(x=384, y=461)
    Button(win, image=img1[4], command=lambda: show_window(win, "국내·외 연속간행물(최신호)", descriptions["국내·외 연속간행물(최신호)"], "국내연속간행물", "Third")).place(x=584, y=297)
    Button(win, image=img1[1], command=lambda: show_window(win, "하늘정원", descriptions["하늘정원"], "하늘정원", "Third")).place(x=648, y=320)
    Button(win, image=img1[5], command=lambda: show_window(win, "고서실", descriptions["고서실"], "고서실", "Third")).place(x=502, y=149)
    Button(win, image=img1[6], command=lambda: show_window(win, "구름다리", descriptions["구름다리"], "구름다리", "Third")).place(x=550, y=218)
    Button(win, image=img1[7], command=lambda: show_window(win, "그래픽노블존", descriptions["그래픽노블존"], "그래픽노블존", "Third")).place(x=384, y=420)
    Button(win, image=img1[8], command=lambda: show_window(win, "기독교자료실", descriptions["기독교자료실"], "기독교3", "Third")).place(x=578, y=86)
    Button(win, image=img1[9], command=lambda: show_window(win, "미디어자료실", descriptions["미디어자료실"], "미디어자료실", "Third")).place(x=298, y=447)
    Button(win, image=img1[10], command=lambda: show_window(win, "서양서자료실", descriptions["서양서자료실"], "서양서3", "Third")).place(x=753, y=369)
    Button(win, image=img1[11], command=lambda: show_window(win, "소극장", descriptions["소극장"], "소극장_앞", "Third")).place(x=336, y=464)
    Button(win, image=img1[12], command=lambda: show_window(win, "미디어밸리", descriptions["미디어밸리"], "미디어밸리", "Third")).place(x=425, y=409)
    Button(win, image=img1[13], command=lambda: show_window(win, "원문검색 PC", descriptions["원문검색 PC"], "원문검색2", "Third")).place(x=596, y=263)
    Button(win, image=img1[14], command=lambda: show_window(win, "E-learning존", descriptions["E-learning존"], "이러닝존", "Third")).place(x=464, y=353)
    Button(win, image=img1[15], command=lambda: show_window(win, "참고자료실", descriptions["참고자료실"], "참고자료", "Third")).place(x=571, y=377)
    Button(win, image=img1[16], command=lambda: show_window(win, "Kids English Zone", descriptions["Kids English Zone"], "EngKids", "Third")).place(x=427, y=167)

    
    #command를 사용해 Back버튼을 누를 시 selectfloor 호출하여 win창을 닫고 win_selectfloor 모듈의 select 함수 호출
    def selectfloor():
        win.destroy()
        from win_selectfloor import select
        select()
    Button(win, text="Back", font=("굴림체",20), command=selectfloor).pack(side="bottom",padx=10,pady=20)


    win.mainloop()