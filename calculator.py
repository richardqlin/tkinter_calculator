from tkinter import *

root =Tk()


scrollbar=Scrollbar(root)
listbox = Listbox(root,yscrollcommand = scrollbar.set)
check=0
#listbox.grid()
class customer_button:
    check = 0
    def __init__(self,name,row,col,span):
        self.name=name
        self.row= row
        self.col = col
        self.span = span
        self.flag=0
        self.check = 0

    def draw_button(self):
        b = Button(root, text = self.name,width=4, height=2,command=self.button_clicked)
        b.grid(row=self.row, column=self.col,columnspan=self.span)
        
    def button_clicked(self):
        global check
        #print(self.name)
        if self.name =='C':
            entry.delete(0,END)
        elif self.name == '=':
            check = 1
            g=entry.get()
            listbox.insert(END,g)
            g = eval(g)
            
            entry.delete(0, END)
            entry.insert(END,g)
            print('l',check)
            
        elif self.name=='back':
            g = entry.get()[:-1]
            entry.delete(0,END)
            entry.insert(0,g)
        elif self.name=='history' and self.flag==0:
            print('history')
            scrollbar.config(command=listbox.yview)
            listbox.grid(row=1,column=4,rowspan=5)
            self.flag=1
        elif self.name=='history' and self.flag==1:
            self.flag=0
            listbox.grid_remove()
        else:
            l=listbox.curselection()
           
##                while 1:
##                if len(l)>0:
##                    v = listbox.get(l)
##                    print(v)
##                
            print('h',check)
            if check == 1:
                print('hello')
                entry.delete(0,END)
                check = 0
                entry.insert(END,self.name)
            else:
                entry.insert(END,self.name)

def clear():
    listbox.delete(0, END)
    
            
button = customer_button('C',1,3,1)
button.draw_button()

button = customer_button('history',1,0,2)
button.draw_button()

button = customer_button('back',1,2,1)
button.draw_button()

for r in range(3):
    for c in range(3):
        button = customer_button(3*r+c+1,r+2,c,1)
        button.draw_button()
        
        

operation=['+','-','*','/']
n=2
for r in operation:
    button = customer_button(r,n,3,1)
    button.draw_button()
    n+=1

op = ['.','0','=']
n=0
for r in op:
    button = customer_button(r,5,n,1)
    button.draw_button()
    n+=1

entry = Entry(root, width=20, bd=5)
entry.grid(row=0,column=0, columnspan=3)


