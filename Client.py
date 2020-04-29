from tkinter import Canvas,Button,Tk,PhotoImage,NW,Label,Frame
from time import sleep
# import Test_đi_tuan
from PIL import Image, ImageTk
class Windown(Frame):
    #contrustor
    def __init__(self, element,master=None,):
        Frame.__init__(self,master)
        self.master=master
        self.element=element
        self.hei_wid=400
        self.arr = [[0 for i in range(0,self.element)] for j in range(0,self.element)]
        self.ngua=None
        self.display()

    def display(self):
        Label(self.master,text="Ngua di tuan")
        self.can=Canvas(self.master,width=self.hei_wid,height=self.hei_wid)
        self.ve_ban_co()
        self.can.bind('<Button-1>',self.motion)
        self.can.pack()
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
        x=50*toa_doX
        y=50*toa_doY
        img= Image.open("Image\\ngua.png")
        # wid=hei=self.hei_wid/self.element
        img= img.resize((50, 50), Image.ANTIALIAS)
        img.save("Image\\nguax50.png")
        self.png = PhotoImage(file="Image\\nguax50.png")
        self.ngua=self.can.create_image(x,y,anchor=NW, image=self.png)
        self.can.update()
        pass    
app = Windown(8,Tk())
