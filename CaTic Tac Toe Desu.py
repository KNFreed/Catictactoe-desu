#########################################
# Author : Frédéric Spataro             #
# OS Windows 10, Python 3.7.1 32 bits   #
# Titre : CaTic Tac Toe Desu v1.0       #
#########################################

#########################################
# Let's import the libraries

from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from random import choice
from winsound import *

#########################################
# Let's define the variables

window = Tk()
window.title('CaTic Tac Toe Desu')
window.geometry("721x1000")
img = ImageTk.PhotoImage(file="./stuff/fond.png")
img_label = Label(window, image=img)
img_label.place(x=0, y=0, relwidth=1, relheight=1)
multijoueur = ImageTk.PhotoImage(file="./stuff/2joueurs.png")
solo = ImageTk.PhotoImage(file="./stuff/1joueur.png")
retourj = ImageTk.PhotoImage(file="./stuff/retour.png")
quitter = ImageTk.PhotoImage(file="./stuff/quitter.png")
infoc = ImageTk.PhotoImage(file="./stuff/info.png")
me = ImageTk.PhotoImage(file="./stuff/me.png")
retourme = ImageTk.PhotoImage(file="./stuff/retourme.png")
jouer = ImageTk.PhotoImage(file='./stuff/jouer.png')
grille=[]
tour=True
v1=0
v2=0
v4=0

#########################################
# More definitions

def menu():
     def jeu():
          def multijouer():
               PlaySound('./stuff/game.wav', SND_FILENAME)
               button4.destroy()
               button5.destroy()
               button6.destroy()
               def jeua2():
                    def toursj(buttons):
                         global tour
                         global v1
                         global v2
                         if buttons["text"] == " " and tour == True:
                             buttons["text"] = "X"
                             tour = False
                         elif buttons["text"] == " " and tour == False:
                              buttons["text"] = "O"
                              tour = True
                         else:
                              messagebox.showinfo("Case already filled","Case already filled, please choose another one.")


                         if(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'or
                              button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'or
                              button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'or
                              button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'or
                              button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'or
                              button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'or
                              button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'or
                              button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
                              v1=v1+1
                              reponse = messagebox.askyesno("End","Player 1 won. Do you want to play again?\nScore:\nPlayer 1: {}\nPlayer 2: {}".format(v1,v2))
                              if reponse == True:
                                   jeua2()
                              else:
                                   v1=0
                                   v2=0
                                   quitterm()

                         elif(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or
                              button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O'or
                              button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'or
                              button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'or
                              button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'or
                              button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'or
                              button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'or
                              button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
                              v2=v2+1
                              reponse = messagebox.askyesno("End","Player 2 won. Do you want to play again?\nScore:\nPlayer 1: {}\nPlayer 2: {}".format(v1,v2))
                              if reponse == True:
                                   jeua2()
                              else:
                                   v1=0
                                   v2=0
                                   quitterm()
                         elif (button1['text'] != ' ' and button2['text'] != ' ' and button3['text'] != ' ' and button4['text'] != ' ' and button5['text'] != ' ' and button6['text'] != ' ' and button7['text'] != ' ' and button8['text'] != ' ' and button9['text'] != ' '):
                              reponse = messagebox.askyesno("End","Tie, no one won. Do you want to play again?\nScore:\nPlayer 1: {}\nPlayer 2: {}".format(v1,v2))
                              if reponse == True:
                                   jeua2()
                              else:
                                   v1=0
                                   v2=0
                                   quitterm()



                    buttons=StringVar()

                    button1 = Button(window,text=" ",font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button1))
                    button1.grid(row=1,column=0,sticky = S+N+E+W)

                    button2 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button2))
                    button2.grid(row=1,column=1,sticky = S+N+E+W)

                    button3 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button3))
                    button3.grid(row=1,column=2,sticky = S+N+E+W)

                    button4 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button4))
                    button4.grid(row=2,column=0,sticky = S+N+E+W)

                    button5 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button5))
                    button5.grid(row=2,column=1,sticky = S+N+E+W)

                    button6 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button6))
                    button6.grid(row=2,column=2,sticky = S+N+E+W)

                    button7 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button7))
                    button7.grid(row=3,column=0,sticky = S+N+E+W)

                    button8 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button8))
                    button8.grid(row=3,column=1,sticky = S+N+E+W)

                    button9 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button9))
                    button9.grid(row=3,column=2,sticky = S+N+E+W)
                    def quitterm():
                         global v1
                         global v2
                         v1=0
                         v2=0
                         button1.destroy()
                         button2.destroy()
                         button3.destroy()
                         button4.destroy()
                         button5.destroy()
                         button6.destroy()
                         button7.destroy()
                         button8.destroy()
                         button9.destroy()
                         button10.destroy()
                         menu()
                    button10 = Button(window, image=retourj, command=quitterm, bd=0, highlightthickness=0)
                    button10.place(relx=0.5, rely=1.0, anchor=S)
                    
               jeua2()
          def toutseul():
               PlaySound('./stuff/game.wav', SND_FILENAME)
               button4.destroy()
               button5.destroy()
               button6.destroy()
               v1=0
               v2=0
               v4=0
               v6=0
               def jeusolo():
                    def toursj(buttons):
                         global v1
                         global v4
                         global v6
                         v3 = v1
                         v5 = v4
                         def verifjoueur():
                              global v1
                              global v2
                              global v4
                              if(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'or
                                   button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'or
                                   button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'or
                                   button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'or
                                   button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'or
                                   button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'or
                                   button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'or
                                   button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
                                   v1=v1+1
                                   PlaySound('./stuff/victoire.wav', SND_FILENAME)
                                   reponse = messagebox.askyesno("End","You won. Do you want to play again?\nScore:\nPlayer 1: {}\nPlayer 2: {}".format(v1,v2))
                                   if reponse == True:
                                        jeusolo()
                                   else:
                                        v1=0
                                        v2=0
                                        v4=0
                                        quitterm()

                              elif (button1['text'] != ' ' and button2['text'] != ' ' and button3['text'] != ' ' and button4['text'] != ' ' and button5['text'] != ' ' and button6['text'] != ' ' and button7['text'] != ' ' and button8['text'] != ' ' and button9['text'] != ' '):
                                   v4 =v4+1
                                   reponse = messagebox.askyesno("End","Tie, no one won. Do you want to play again?\nScore:\nPlayer 1: {}\nBot: {}".format(v1,v2))
                                   if reponse == True:
                                        jeusolo()
                                   else:
                                        v1=0
                                        v2=0
                                        v4=0
                                        quitterm()
                         def verifbot():
                              global v1
                              global v2
                              if(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or
                                   button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O'or
                                   button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'or
                                   button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'or
                                   button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'or
                                   button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'or
                                   button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'or
                                   button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
                                   v2=v2+1
                                   reponse = messagebox.askyesno("End","Bot won. Do you want to play again ?\nScore:\nPlayer 1: {}\nBot: {}".format(v1,v2))
                                   if reponse == True:
                                        jeusolo()
                                   else:
                                        v1=0
                                        v2=0
                                        v4=0
                                        quitterm()

                         def bot():
                              #atq lines
                              if button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == ' ':
                                   button3['text'] = 'O'
                              elif button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == ' ':
                                   button6['text'] = 'O'
                              elif button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == ' ':
                                   button9['text'] = 'O'
                              #atq columns
                              elif button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == ' ':
                                   button7['text'] = 'O'
                              elif button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == ' ':
                                   button8['text'] = 'O'
                              elif button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == ' ':
                                   button9['text'] = 'O'
                              #atq diagonals
                              elif button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == ' ':
                                   button9['text'] = 'O'
                              elif button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == ' ':
                                   button7['text'] = 'O'
                              #atq invdiag
                              elif button9['text'] == 'O' and button5['text'] == 'O' and button1['text'] == ' ':
                                   button1['text'] = 'O'
                              elif button7['text'] == 'O' and button5['text'] == 'O' and button3['text'] == ' ':
                                   button3['text'] = 'O'
                              #atq invcol
                              elif button7['text'] == 'O' and button4['text'] == 'O' and button1['text'] == ' ':
                                   button1['text'] = 'O'
                              elif button8['text'] == 'O' and button5['text'] == 'O' and button2['text'] == ' ':
                                   button2['text'] = 'O'
                              elif button9['text'] == 'O' and button6['text'] == 'O' and button3['text'] == ' ':
                                   button3['text'] = 'O'
                              #atq invli
                              elif button3['text'] == 'O' and button2['text'] == 'O' and button1['text'] == ' ':
                                   button1['text'] = 'O'
                              elif button6['text'] == 'O' and button5['text'] == 'O' and button4['text'] == ' ':
                                   button4['text'] = 'O'
                              elif button9['text'] == 'O' and button8['text'] == 'O' and button7['text'] == ' ':
                                   button7['text'] = 'O'
                              #atq li2
                              elif button1['text'] == 'O' and button3['text'] == 'O' and button2['text'] == ' ':
                                   button2['text'] = 'O'
                              elif button4['text'] == 'O' and button6['text'] == 'O' and button5['text'] == ' ':
                                   button5['text'] = 'O'
                              elif button7['text'] == 'XO' and button9['text'] == 'O' and button8['text'] == ' ':
                                   button8['text'] = 'O'
                              #atq col2
                              elif button1['text'] == 'O' and button7['text'] == 'O' and button4['text'] == ' ':
                                   button4['text'] = 'O'
                              elif button2['text'] == 'O' and button8['text'] == 'O' and button5['text'] == ' ':
                                   button5['text'] = 'O'
                              elif button3['text'] == 'O' and button9['text'] == 'O' and button6['text'] == ' ':
                                   button6['text'] = 'O'
                              #atq diag2
                              elif button1['text'] == 'O' and button9['text'] == 'O' and button5['text'] == ' ':
                                   button5['text'] = 'O'
                              elif button3['text'] == 'O' and button7['text'] == 'O' and button5['text'] == ' ':
                                   button5['text'] = 'O'
                              #block li
                              elif button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == ' ':
                                   button3['text'] = 'O'
                              elif button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == ' ':
                                   button6['text'] = 'O'
                              elif button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == ' ':
                                   button9['text'] = 'O'
                              #blocl col
                              elif button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == ' ':
                                   button7['text'] = 'O'
                              elif button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == ' ':
                                   button8['text'] = 'O'
                              elif button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == ' ':
                                   button9['text'] = 'O'
                              #block diag
                              elif button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == ' ':
                                   button9['text'] = 'O'
                              elif button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == ' ':
                                   button7['text'] = 'O'
                              #block invdiag
                              elif button9['text'] == 'X' and button5['text'] == 'X' and button1['text'] == ' ':
                                   button1['text'] = 'O'
                              elif button7['text'] == 'X' and button5['text'] == 'X' and button3['text'] == ' ':
                                   button3['text'] = 'O'
                              #block invcol
                              elif button7['text'] == 'X' and button4['text'] == 'X' and button1['text'] == ' ':
                                   button1['text'] = 'O'
                              elif button8['text'] == 'X' and button5['text'] == 'X' and button2['text'] == ' ':
                                   button2['text'] = 'O'
                              elif button9['text'] == 'X' and button6['text'] == 'X' and button3['text'] == ' ':
                                   button3['text'] = 'O'
                              #block invli
                              elif button3['text'] == 'X' and button2['text'] == 'X' and button1['text'] == ' ':
                                   button1['text'] = 'O'
                              elif button6['text'] == 'X' and button5['text'] == 'X' and button4['text'] == ' ':
                                   button4['text'] = 'O'
                              elif button9['text'] == 'X' and button8['text'] == 'X' and button7['text'] == ' ':
                                   button7['text'] = 'O'
                              #block li2
                              elif button1['text'] == 'X' and button3['text'] == 'X' and button2['text'] == ' ':
                                   button2['text'] = 'O'
                              elif button4['text'] == 'X' and button6['text'] == 'X' and button5['text'] == ' ':
                                   button5['text'] = 'O'
                              elif button7['text'] == 'X' and button9['text'] == 'X' and button8['text'] == ' ':
                                   button8['text'] = 'O'
                              #block col2
                              elif button1['text'] == 'X' and button7['text'] == 'X' and button4['text'] == ' ':
                                   button4['text'] = 'O'
                              elif button2['text'] == 'X' and button8['text'] == 'X' and button5['text'] == ' ':
                                   button5['text'] = 'O'
                              elif button3['text'] == 'X' and button9['text'] == 'X' and button6['text'] == ' ':
                                   button6['text'] = 'O'
                              #block diag2
                              elif button1['text'] == 'X' and button9['text'] == 'X' and button5['text'] == ' ':
                                   button5['text'] = 'O'
                              elif button3['text'] == 'X' and button7['text'] == 'X' and button5['text'] == ' ':
                                   button5['text'] = 'O'
                              #bloquer at start
                              elif button5['text'] == ' ' and (button1['text'] == 'X' or button3['text'] == 'X' or button7['text'] == 'X' or button9['text'] == 'X'):
                                   button5['text'] = 'O'
                              else:
                                   def chasard():
                                        R = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
                                        hasard = choice(R)
                                        if hasard['text'] == ' ':
                                             hasard['text'] = 'O'
                                        else:
                                             chasard()
                                   chasard()
                         def jjeu():
                              global v6
                              if buttons["text"] == " ":
                                  buttons["text"] = "X"
                                  v6=0
                              else:
                                   messagebox.showinfo("Case already filled","Case already filled, please choose another one.")
                                   v6=1
                         jjeu()
                         verifjoueur()
                         if v3 == v1 and v4 == v5 and v6==0:
                              bot()
                              verifbot()
                         
                    buttons=StringVar()

                    button1 = Button(window,text=" ",font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button1))
                    button1.grid(row=1,column=0,sticky = S+N+E+W)

                    button2 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button2))
                    button2.grid(row=1,column=1,sticky = S+N+E+W)

                    button3 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button3))
                    button3.grid(row=1,column=2,sticky = S+N+E+W)

                    button4 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button4))
                    button4.grid(row=2,column=0,sticky = S+N+E+W)

                    button5 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button5))
                    button5.grid(row=2,column=1,sticky = S+N+E+W)

                    button6 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button6))
                    button6.grid(row=2,column=2,sticky = S+N+E+W)

                    button7 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button7))
                    button7.grid(row=3,column=0,sticky = S+N+E+W)

                    button8 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button8))
                    button8.grid(row=3,column=1,sticky = S+N+E+W)

                    button9 = Button(window,text=' ',font=('Times 20 bold'),bg='white',fg='black',height=4,width=8,command=lambda:toursj(button9))
                    button9.grid(row=3,column=2,sticky = S+N+E+W)
                    def quitterm():
                         global v1
                         global v2
                         v1=0
                         v2=0
                         button1.destroy()
                         button2.destroy()
                         button3.destroy()
                         button4.destroy()
                         button5.destroy()
                         button6.destroy()
                         button7.destroy()
                         button8.destroy()
                         button9.destroy()
                         button10.destroy()
                         menu()
                    button10 = Button(window, image=retourj, command=quitterm, bd=0, highlightthickness=0)
                    button10.place(relx=0.5, rely=1.0, anchor=S)

               jeusolo()
          def retour():
               button4.destroy()
               button5.destroy()
               button6.destroy()
               menu()
          button1.destroy()
          button2.destroy()
          button3.destroy()
          button4 = Button(window, image=solo, command=toutseul, bd=0, highlightthickness=0)
          button4.place(relx=0.5, rely=0.675, anchor="center")
          button5 = Button(window, image=retourj, command=retour, bd=0, highlightthickness=0)
          button5.place(relx=0.5, rely=1.0, anchor=S)
          button6 = Button(window, image=multijoueur, command=multijouer, bd=0, highlightthickness=0)
          button6.place(relx=0.5, rely=0.0, anchor=N)
     def info():
          def retour():
               button4.destroy()
               button5.destroy()
               menu()
          button1.destroy()
          button2.destroy()
          button3.destroy()
          button4 = Button(window, image=me, bd=0, highlightthickness=0)
          button4.place(relx=0.5, rely=0.0, anchor=N)
          button5 = Button(window, image=retourme, command=retour, bd=0, highlightthickness=0)
          button5.place(relx=0.5, rely=1.0, anchor=S)
          PlaySound('./stuff/nya.wav', SND_FILENAME)
     button1 = Button(window, image=jouer, command=jeu, bd=0, highlightthickness=0)
     button1.place(relx=0.5, rely=0.0, anchor=N)
     button2 = Button(window, image=quitter, command=window.destroy, bd=0, highlightthickness=0)
     button2.place(relx=0.5, rely=1.0, anchor=S)
     button3 = Button(window, image=infoc, command=info, bd=0, highlightthickness=0)
     button3.place(relx=1.0, rely=0, anchor=NE)

##############################################
# Let the game begin.

menu()
window.mainloop()
      

      
      
                       

          
     
     
