from tkinter import Canvas,Button,Tk,PhotoImage,NW,Label,Frame,LEFT,RIGHT,BOTTOM,ALL
from time import sleep
from kight_tours_warnsdorffs import *
# import Test_đi_tuan
from PIL import Image, ImageTk
class Windown(Frame):
    #contrustor
    def __init__(self, element,master=None,):
        Frame.__init__(self,master)
        self.master=master
        self.element=element
        self.hei_wid=400
        self.dem=1
        self.at_dg_chay=False
        self.arr = [[0 for i in range(0,self.element)] for j in range(0,self.element)]
        self.ngua=None
        self.present=None
        self.path=[]
        self.display()

    def display(self):
        Label(self.master,text="Ngua di tuan")
        self.can=Canvas(self.master,width=self.hei_wid,height=self.hei_wid)
        self.ve_ban_co()
        self.can.bind('<Button-1>',self.motion)
        self.can.pack()
        Button(self.master,text="next-move",command=self.next_move).pack(side=LEFT)
        Button(self.master,text="skip-move",command=self.skip_move).pack(side=RIGHT)
        Button(self.master,text="reset-move",command=self.reset_move).pack(side=BOTTOM)
        self.master.mainloop()
        pass
    #Event when I click mouse right
    def motion(self,event):
        if  self.ngua==None:
            tempa=400/8
            dema=0
            demb=0
            tempb=400/8
            a=event.x
            b=event.y
            #Find position the kight's
            while (tempa-a<0 or tempa-a>400/8) and tempa>=0 and tempa<=400 :
                # print("tempa-a:",tempa-a)
                dema=dema+1
                tempa+=400/8
            while (tempb-b<0 or tempb-b>400/8) and tempb>=0 and tempb<=400 :
                # print("tempb-b:",tempb-b)
                demb=demb+1
                tempb+=400/8 
            self.tao_ngua(dema,demb)
        pass
    #Computer draw  chess
    def ve_ban_co(self):
        y=0
        for i in range(0,self.element):
            x=0
            x1=x+self.hei_wid/self.element
            y1=y+self.hei_wid/self.element
            for j in range(0,self.element):
                if self.element%2==0:
                    a=i*self.element+j+i
                else: 
                    a=i*self.element+j
                if((a)%2==0):
                    self.arr[i][j]=self.can.create_rectangle(x,y,x1,y1,fill='white')
                else:
                    self.arr[i][j]=self.can.create_rectangle(x,y,x1,y1,fill='black')
                x=x+self.hei_wid/self.element
                x1=x+self.hei_wid/self.element   
            y=y+self.hei_wid/self.element 
        pass
    #Creat the knight's when you click mouse left
    def tao_ngua(self,toa_doX,toa_doY):
        self.at_dg_chay=True
        x=50*toa_doX
        y=50*toa_doY
        self.present=(toa_doX,toa_doY)
        # initialize tour kight's
        self.kt=Chess_board(8,8)
        self.kt.tour(1,(toa_doX,toa_doY))
        self.path=self.kt.get_path()
        self.path=self.path[1:64]
        # call file IMG 
        img= Image.open("Image\\ngua.png")
        # wid=hei=self.hei_wid/self.element
        # resize Image
        img= img.resize((50, 50), Image.ANTIALIAS)
        img.save("Image\\nguax50.png")
        self.png = PhotoImage(file="Image\\nguax50.png")
        self.ngua=self.can.create_image(x,y,anchor=NW, image=self.png)
        self.can.create_text(x+25,y+25,text=self.dem,fill="blue")
        self.dem+=1
        self.can.update()
        # for a in self.path:
            # sleep(0.05)
            # self.can.delete(self.ngua)
            # self.can.update()
            # sleep(0.05)
            # self.ngua=self.can.create_image(a[0]*50,a[1]*50,anchor=NW, image=self.png)
            # self.can.create_text(a[0]*50+25,a[1]*50+25,text=self.dem,fill="blue")
            # self.dem+=1
            # self.can.update()

    def next_move(self):
        if self.at_dg_chay:
            a=self.path[0]
            if(self.present[1]*8+self.present[0]+self.present[1])%2==0:
                color_cell="black"
            else:
                color_cell="white"
            arr=self.kt.Check_nextmove(self.present,self.dem)
            for i in arr:
                self.can.itemconfig(self.arr[i[1]][i[0]],fill="red")
                self.can.update()
            sleep(0.5)
            self.can.itemconfig(self.arr[a[1]][a[0]],fill="#51BCA7")
            self.can.update()
            sleep(0.5)
            for i in arr:
                self.can.itemconfig(self.arr[i[1]][i[0]],fill=color_cell)
                self.can.update()
            sleep(0.5)
            self.can.delete(self.ngua)  
            self.can.update()
            sleep(0.05)
            self.ngua=self.can.create_image(a[0]*50,a[1]*50,anchor=NW, image=self.png)
            self.can.create_text(a[0]*50+25,a[1]*50+25,text=self.dem,fill="blue")
            self.dem+=1
            self.can.update()
            self.present=a
            self.path=self.path[1:]

    def skip_move(self):
        self.at_dg_chay=False
        for a in self.path:
            sleep(0.5)
            self.can.delete(self.ngua)
            self.can.update()
            sleep(0.5)
            self.ngua=self.can.create_image(a[0]*50,a[1]*50,anchor=NW, image=self.png)
            self.can.create_text(a[0]*50+25,a[1]*50+25,text=self.dem,fill="blue") 
            self.dem+=1
            self.can.update()
    
    def reset_move(self):
        self.at_dg_chay=False
        self.can.delete(ALL)
        self.ngua=None
        self.arr=None
        self.arr = [[0 for i in range(0,self.element)] for j in range(0,self.element)]
        self.ve_ban_co()
        self.dem=1

app = Windown(8,Tk())
