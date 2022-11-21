from tkinter import *

#========================메인 화면
def showMain():
    win1 = Tk()
    win1.geometry("768x512")
    win1.resizable(False,False)
    win1.title("전주대 애플리케이션")

    backGround = PhotoImage(file="b.png")
    bg = Canvas(win1, bg="white", width=768, height=512)
    bg.create_image(0, 0, anchor=NW, image=backGround)
    bg.place(x=0, y=0)

    Header = Label(win1, text="J e o n j u   U n i v e r s i t y   L i b r a r y", font=("굴림체", 25))
    Header.place(x=171, y=81) 

    Title = Label(win1, text="전 주 대 학 교 도 서 관", font=("굴림체", 40))
    Title.place(x=200, y=120)

    def selectfloor():
        win1.destroy()
        from win_selectfloor import select
        select()
    Start = Button(win1, text="시작", font=(None, 20), command=selectfloor) #시작 버튼 누를 시 층 고르는 화면으로 이동
    Start.place(x=330, y=370)

    def win_end():
        win1.destroy()
        
    Exit = Button(win1, text="종료", font=(None, 20), command=win_end) 
    Exit.place(x=330, y=410)

    win1.mainloop()

if __name__ == "__main__":
    showMain()