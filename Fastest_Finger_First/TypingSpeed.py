words = ['Grapes','Mango','Apple','Gun' , 'Fan' ,'Door' , 'TV' , 'Mobile' , 'Laptop']

def labelslider():
    global count, sliderWords
    text = 'Welcome to Fastest Finger First'
    if (count>=len(text)) :
        count = 0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    fontLable.configure(text=sliderWords)
    fontLable.after(150,labelslider)

def time () :
    global timeLeft,score,miss
    if (timeLeft >= 11) :
        pass
    else :
        timeLableCount.configure(fg='red')
    if (timeLeft>0):
        timeLeft -= 1
        timeLableCount.configure(text=timeLeft)
        timeLableCount.after(1000,time)
    else :
        gamePlayDetailLabel.configure(text='Hit = {} | Miss = {} | Total Score = {} '.format(score,miss,score-miss))
        rr = messagebox.askretrycancel('Notification','For Play Again press retry button')
        if (rr==True) :
            score = 0
            timeLeft = 60
            miss = 0
            timeLableCount.configure(text=timeLeft)
            wordLabel.configure(text=words[0])
            scoreLableCount.configure(text=score)


def startGame(event) :
    global score , miss
    if (timeLeft==60):
        time()
    gamePlayDetailLabel.configure(text='')
    if (wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLableCount.configure(text=score)

    else :
        miss += 1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)



from tkinter import *
import random
from tkinter import messagebox

######################################### Root Method
root = Tk()
root.geometry("800x600+400+100")
root.configure(bg='powder blue')
root.title('Fastest Finger first')
root.iconbitmap('fastestfingerfirsticon.ico')
################################## variables

score = 0
timeLeft = 60
count = 0
sliderWords = ''
miss = 0

################################ Label Methods

fontLable = Label(root,text='', font = ('airal',25,'italic bold'), bg = 'powder blue' , fg = 'red' , width=40 )
fontLable.place(x=10,y=10)

labelslider()
random.shuffle(words)

wordLabel = Label(root,text=words[0] , font = ('airal',40,'italic bold'),bg = 'powder blue')
wordLabel.place(x=350,y=200)

scoreLable = Label(root,text='Your Score:', font=('airal',25,'italic bold'), bg = 'powder blue' )
scoreLable.place(x=10,y=100)

scoreLableCount = Label(root,text=score, font=('airal',25,'italic bold'), bg = 'powder blue' , fg = 'blue' )
scoreLableCount.place(x=80,y=180)

timerLabel = Label(root,text='Time Left :', font=('airal',25,'italic bold'), bg = 'powder blue' )
timerLabel.place(x=600,y=100)

timeLableCount = Label(root,text=timeLeft, font=('airal',25,'italic bold'), bg = 'powder blue' , fg = 'blue' )
timeLableCount.place(x=680,y=180)

gamePlayDetailLabel = Label(root,text='Type Word and Hit Enter button',font= ('airal',30,'italic bold'),bg= 'powder blue',fg='dark grey')
gamePlayDetailLabel.place(x=120,y=450)

########################## Entry Method

wordEntry = Entry(root,font=('airal',25,'italic bold') , bd = 10 , justify='center' )
wordEntry.place(x=250,y=300)
wordEntry.focus_set()

########################

root.bind('<Return>',startGame)
root.mainloop()