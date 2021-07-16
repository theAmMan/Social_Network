from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

class user:
    def __init__(self,z):
        z=z[1:len(z)-2]
        x = z.split()
        self.contact=[]
        self.id = x[0].strip(':')
        for k in range(1,len(x)):
            if x[k][len(x[k])-1]==',':
                x[k]=x[k].strip(',')
            self.contact.append(x[k])
        
            
class group:
    def __init__(self,z):
        z=z[1:len(z)-2]
        x=z.split()
        self.memb = []
        self.id = x[0].strip(':')
        for k in range(1,len(x)):
            if x[k][len(x[k])-1]==',':
                x[k]=x[k].strip(',')
            self.memb.append(x[k])
        
        
                    
class TLFrame(Frame):
    def __init__(self,master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.grid(row=1, column=0)
        master.grid_columnconfigure(0,weight=1)
        master.grid_rowconfigure(0,weight=1)
        self.lb = Label(self,text="Messages ")
        self.lb.grid(row=0,column=0,sticky=S+N+E+W)
        self.textbox = Text(self,width=50,height=15,padx=3,pady=3,bd=1)
        self.textbox.grid(row=1,column=0,sticky=S+N+E+W)
        self.img = []

    def msg(self):
        self.textbox.delete(1.0,END)
        file=open("messages.txt",'a')
        file.close()
        file=open("messages.txt",'r')
        for z in file:
            flag=0
            for i in range(0,len(crgrp)):
                if z.find("Group "+crgrp[i].id)==0:
                    flag=1
                    self.textbox.insert(END,"*Group "+crgrp[i].id+"*")
            if(z.find(usrnm+"<>")==0 or flag==1):
                if(z.find("IMG_SRC:")==z.find(": ")+2):
                    x=z.split()
                    self.textbox.insert(END,x[1][x[1].find("<>")+2::]+" ")
                    self.textbox.insert(END,x[2])
                    self.img.append(ImageTk.PhotoImage(Image.open(x[len(x)-1])))
                    self.textbox.window_create(END, window = Label(self.textbox, image = self.img[len(self.img)-1]))
                    self.textbox.insert(END,'\n')
                    
                else:    
                    self.textbox.insert(END,z[z.find("<>")+2::])            
            
        file.close()
        
class TRFrame(Frame):
    def __init__(self,master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.grid(row=1, column=1)
        master.grid_columnconfigure(1,weight=1)
        master.grid_rowconfigure(0,weight=1)
        self.lb = Label(self,text="All Contacts ")
        self.lb.grid(row=0,column=0,sticky=S+N+E+W)
        self.tb= Text(self,width=30,height=15,padx=3,pady=3,bd=1)
        self.tb.grid(row=1,column=0,sticky=S+N+E+W)
        self.tb.insert(END,"Select User")
        
class BLFrame(Frame):
    def __init__(self,master=NONE):
        Frame.__init__(self, master,bg="#efefef")
        self.master = master
        self.grid(row=2, column=0)
        master.grid_columnconfigure(0,weight=1)
        master.grid_rowconfigure(1,weight=1)
        self.tb=Text(self,width=50,height=10,padx=3,pady=3,bd=3)
        self.tb.grid(row=1,column=0,columnspan=2,sticky=S+N+E+W)
        self.lab1 = Label(self,text="Select Recipient and type your message below: ")
        self.lab1.grid(row=0,column=0)  
        self.OPT = ["Select User"]
        self.var = StringVar(master)
        self.var.set(self.OPT[0])
        self.men = OptionMenu(self,self.var,*self.OPT)
        self.men.grid(row=0,column=1,padx = 25,pady=0)
        self.button = Button(self,text="Post",command=self.post,height=1,padx=15,pady=3)
        self.button.grid(row=2, column=0)
        self.sbut = Button(self,text="Select Image",command=self.open,height=1,padx=15,pady=3)
        self.sbut.grid(row=2, column=1)
    
    def open(self):
        fname=filedialog.askopenfilename()
        if len(fname)>0:
            self.tb.insert(END,"\nIMG_SRC: "+fname)    
        
    def post(self):
        rec = self.var.get()
        file=open("messages.txt","a")
        pst=self.tb.get(1.0,END)
        pst.strip('\n')
        s=pst.split('\n')
        for z in range(0,len(s)):
            if len(s[z])>0:
                file.write("\n"+rec+"<>")    
                file.write(usrnm+": "+s[z])
        self.tb.delete(1.0, END)
        file.close()
        
class BRFrame(Frame):
    def __init__(self,master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.grid(row=2, column=1)
        master.grid_columnconfigure(1,weight=1)
        master.grid_rowconfigure(1,weight=1)
        self.lb = Label(self,text="Groups ")
        self.lb.grid(row=0,column=0,sticky=S+N+E+W)
        self.tb= Text(self,width=30,height=11,padx=3,pady=3,bd=1)
        self.tb.grid(row=1,column=0,sticky=S+N+E+W)
        self.tb.insert(END,"Select User")
        
                
class BFrame(Frame):
    def __init__(self,master=NONE):
        Frame.__init__(self, master,bg="#efefef")
        self.master = master
        self.grid(row=0, columnspan=2,sticky=S+N+E+W)
        self.lab1 = Label(self,text="Select User: ",padx=10,pady=5)
        self.lab1.grid(row=0,column=0)  
        OPT = []
        self.var = StringVar(master)
        for i in range(0,len(usr)):
            OPT.append("User "+usr[i].id)
        self.var.set(OPT[0])
        self.men = OptionMenu(self,self.var,*OPT)
        self.men.grid(row=0,column=1,columnspan=2,padx = 25,pady=10)
        self.button = Button(self,text="OK",command=ok,height=1,padx=15,pady=3)
        self.button.grid(row=0, column=3)  
        
    
                
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        master.geometry("700x550")
        self.tlframe = TLFrame(master)
        self.trframe = TRFrame(master)
        self.blframe = BLFrame(master)
        self.brframe = BRFrame(master)
        self.bframe = BFrame(master)
        master.wm_title("Social Network")
        self.grid(row=0,column=0)
        
            
def ok():
    global usrnm,crusr,crgrp
    crgrp.clear()
    usrnm=app.bframe.var.get()
    app.trframe.tb.delete(1.0,END)
    for i in range(0,len(usr)):
        if(usrnm.find(usr[i].id)!=-1):
            crusr=usr[i]
            for j  in range(0,len(usr[i].contact)):
                app.trframe.tb.insert(END,"User "+usr[i].contact[j]+"\n")
            break
    app.brframe.tb.delete(1.0,END)
    for i in range(0,len(grp)):
        for j in range(0,len(grp[i].memb)):
            if(usrnm.find(grp[i].memb[j])!=-1):
                crgrp.append(grp[i])
                app.brframe.tb.insert(END,"Group "+grp[i].id+"\n")
                break
    app.tlframe.msg()  
    app.blframe.OPT = []
    for i in range(0,len(crusr.contact)):
        app.blframe.OPT.append("User "+crusr.contact[i])
    for i in range(0,len(crgrp)):
        app.blframe.OPT.append("Group "+crgrp[i].id)    
    app.blframe.var.set(app.blframe.OPT[0])
    app.blframe.men = OptionMenu(app.blframe,app.blframe.var,*app.blframe.OPT)
    app.blframe.men.grid(row=0,column=1,padx = 25,pady=3)  
          

file=open("social_network.txt")
usr=[]
grp=[]
crgrp=[]
flag=0
for each in file:
    if(flag==2):
        grp.append(group(each))
    if(each.find("#groups")==0):
        flag=2    
    if(flag==1):    
        usr.append(user(each))
    if(each.find("#users")==0):
        flag=1
        
crusr=usr[0] 
usrnm = "User "+usr[0].id   
file.close()
root = Tk()
app = Window(root)

root.mainloop()