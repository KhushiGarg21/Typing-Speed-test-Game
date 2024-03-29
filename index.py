import tkinter as tk
import random
import time
from tkinter import messagebox
from tkinter import *
top=tk.Tk()
top.geometry('1366x768')
top.configure(bg='powderblue')
top.title("Typing speed test game0.")
top.minsize(width=300, height=200)

score=0
miss=0
#close button
closeButton = tk.Button(top, text='close', width='7', height='1',command=top.destroy)
closeButton.pack(anchor=tk.NE)

#frames
frame0 = tk.Frame(top,height='40', width='60')
frame0.configure(bg='powderblue')
frame0.pack(anchor=tk.N)

frame1 = tk.Frame(top, height='40',width='60')
frame1.configure(bg='powderblue')
frame1.pack(anchor=tk.N)

frame2 = tk.Frame(top, height='40',width='60')
frame2.configure(bg='powderblue')
frame2.pack(anchor=tk.N)

#words for label matching
words = ['Water', 'is','the' ,'most' ,'important' ,'and' ,'valuable', 'natural', 'resource', 'on' ,'Earth']

def startGame(event):
   global score,miss
   if(wordentry.get() == wordlabel['text']):
      score += 1
      scorelabelcount.configure(text=score)
      print("score:",score)
   else:
      miss += 1
      misslabelcount.configure(text=miss)
      print('miss:',miss)
   if miss>=10:
      rr2 = messagebox.askretrycancel('Notification', 'very bad!')

   random.shuffle(words)
   wordlabel.configure(text=words[0])
   print(wordentry.get())
   wordentry.delete(0,END)

# create a list of different colors
colors = ["red","orange","yellow","green","indigo","hotpink"]
#color changer for font welcome
def color_changer():
   # choose and configure random color to the label text
   fg = random.choice(colors)
   fontlabel.config(fg=fg)

   # call the color_changer() method after 200 micro seconds
   fontlabel.after(200, color_changer)

   # create a list of different texts
   labels = ["Welcome to typing speed test game"]
   # choose and configure random text to the label
   text = random.choice(labels)
   fontlabel.config(text=text)

fontlabel = tk.Label(frame0, font=('ariel', 30, 'bold'), bg="powderblue")
fontlabel.pack()
color_changer()

#Functions Defining
count = 180
run = False
#level 1 btn timer code
def var_name(mark):
   def value():
      if run:
         global count
         # Just beore starting
         if count == -1:
            show = "Starting"
         elif count1 == 0:
            rr = messagebox.askretrycancel('Notification', 'For play Again Hit retry button and do following \n 1.press Stop \n 2.press Reset')
         else:
            show = str(count)
         mark['text'] = show
         #Increment the count after
         #every 1 second
         mark.after(1000, value)
         count -= 1
   value()

#level1 start
def Start(mark):
   global run
   run = True
   var_name(mark)
   lvl1_button['state'] = 'disabled'
   lvl2_button['state'] = 'disabled'
   lvl3_button['state'] = 'disabled'
   stop['state'] = 'normal'
   reset['state'] = 'normal'

#level 2 timer code
count1 = 120
run = False
def var_name1(mark):
   def value1():
      if run:
         global count1
         # Just beore starting
         if count1 == -1:
            show = "Starting"
         elif count1 == 0:
            rr = messagebox.askretrycancel('Notification', 'For play Again Hit retry button and do following \n\n 1.press Stop \n 2.press Reset')

         else:
            show = str(count1)
         mark['text'] = show
         #Increment the count after
         #every 1 second
         mark.after(1000, value1)
         count1 -= 1
   value1()

#lvl2 start
def Start1(mark):
   global run
   run = True
   var_name1(mark)
   lvl1_button['state'] = 'disabled'
   lvl2_button['state'] = 'disabled'
   lvl3_button['state'] = 'disabled'
   stop['state'] = 'normal'
   reset['state'] = 'normal'

#level 3 timer code
count2 = 60
run = False
def var_name2(mark):
   def value2():
      if run:
         global count2
         # Just beore starting
         if count2 == -1:
            show = "Starting"
         elif count1 == 0:
            rr = messagebox.askretrycancel('Notification', 'For play Again Hit retry button and do following \n 1.press Stop \n 2.press Reset')
         else:
            show = str(count2)
         mark['text'] = show
         #Increment the count after
         #every 1 second
         mark.after(1000, value2)
         count2 -= 1
   value2()

#level 3 start
def Start2(mark):
   global run
   run = True
   var_name2(mark)
   lvl1_button['state'] = 'disabled'
   lvl2_button['state'] = 'disabled'
   lvl3_button['state'] = 'disabled'
   stop['state'] = 'normal'
   reset['state'] = 'normal'
#timer code end for all level buttons--*--

# While stopped
def Stop():
   global run
   stop['state'] = 'disabled'
   reset['state'] = 'normal'
   lvl1_button['state'] = 'normal'
   lvl2_button['state'] = 'normal'
   lvl3_button['state'] = 'normal'
   run = False
# For Reset
def Reset(label):
   global count
   count = 180
   if run == False:
      reset['state'] = 'disabled'
      mark['text'] = 'Welcome'
      lvl1_button['state'] = 'normal'
      lvl2_button['state'] = 'normal'
      lvl3_button['state'] = 'normal'
   else:
      mark['text'] = 'Start'

   global count1
   count1 = 120
   if run == False:
      reset['state'] = 'disabled'
      mark['text'] = 'Welcome'
      lvl1_button['state'] = 'normal'
      lvl2_button['state'] = 'normal'
      lvl3_button['state'] = 'normal'
   else:
      mark['text'] = 'Start'

   global count2
   count2 = 60
   if run == False:
      reset['state'] = 'disabled'
      mark['text'] = 'Choose your difficulty'
      lvl1_button['state'] = 'normal'
      lvl2_button['state'] = 'normal'
      lvl3_button['state'] = 'normal'
   else:
      mark['text'] = 'Start'

#label for welcome
mark = tk.Label(frame1, text="Choose your difficulty", fg="blue", font="Times 25 bold",bg="powderblue")
mark.pack()

#stop and reset buttons
stop = tk.Button(frame1, text='Stop', width=25, state='disabled', command=Stop)
reset = tk.Button(frame1, text='Reset',width=25, state='disabled', command=lambda: Reset(mark))
stop.pack()
reset.pack()

#level Buttons
lvl1_button = tk.Button(frame1, text='EASY',width='7', height='1',command=lambda: Start(mark))
lvl1_button.pack()
lvl2_button = tk.Button(frame1, text='MEDIUM',width='7', height='1',command=lambda: Start1(mark))
lvl2_button.pack()
lvl3_button = tk.Button(frame1, text='HARD',width='7', height='1',command=lambda: Start2(mark))
lvl3_button.pack()
null_label=tk.Label(frame2,bg="powderblue")
null_label.pack()

#word label
random.shuffle(words)
wordlabel=tk.Label(frame2,text=words[0], width=70, height=12, font=('airal',13,'italic bold'))
wordlabel.pack()

#score label
scorelabel = tk.Label(top,text="Your Score :", font=('airal',20,'italic bold'),bg='powderblue')
scorelabel.place(x=50, y=200)
scorelabelcount = tk.Label(top,text=score, font=('airal',20,'italic bold'),bg='powderblue')
scorelabelcount.place(x=100, y=250)

#miss score
misslabel = tk.Label(top,text="Total wrong words :", font=('airal',20,'italic bold'),bg='powderblue')
misslabel.place(x=1000, y=200)
misslabelcount = tk.Label(top,text=miss, font=('airal',20,'italic bold'),bg='powderblue')
misslabelcount.place(x=1100, y=250)

null_label=tk.Label(frame2,bg="powderblue")
null_label.pack()

#word entry option
wordentry = tk.Entry(frame2,font=('arial', 16, 'italic bold'), width='60' )
wordentry.focus_set()
wordentry.pack()
top.bind('<Return>',startGame)
null_label=tk.Label(frame2,bg="powderblue")
null_label.pack()

#gameplaydetail_label
gamelabel=tk.Label(frame2,text="Type word and hit enter button",font=('arial',20,'italic bold'), bg="powderblue",fg="darkred")
gamelabel.pack()
null_label=tk.Label(frame2,bg="powderblue")
null_label.pack()

top.mainloop()
