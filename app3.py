from tkinter import *

window = Tk()
window.title("Test Report")
window.geometry("3000x2000")

list_of_btu = list()

class button_text_unit:   
    def __init__(self,window,x,y,label_text="",unit_text="unit"):
        self.x = x
        self.y = y
        self.b = Checkbutton(window, text = label_text,command=self.enable,font=("Helvetica", 16),fg="grey")
        self.txt = Entry(window, bd=5,state= DISABLED)
        self.unit = Label(window, text=unit_text,font=("Helvetica",16),fg="grey")
        
        self.b.place(x = self.x, y =self.y)
        self.txt.place(x = self.x +500, y = self.y)
        self.unit.place(x = self.x + 700, y = self.y)
        
    def enable(self):
        if self.txt["state"] == "disabled":
            self.txt.configure(state = 'normal')
            self.b["fg"] = "black"
            self.unit["fg"] = "black"
            list_of_btu.append(self)
        else:
            self.txt.configure(state = 'disabled')
            self.b["fg"] = "grey"
            self.unit["fg"] = "grey"
            list_of_btu.remove(self)

   
heading = Label(window, text="Test Report",font=("Helvetica", 30),fg="black")
heading.place(x = 500,y = 0)

t1 = Label(window, text = "Parameter",font=("Helvetica", 16),fg="black")
t2 = Label(window, text = "Result",font=("Helvetica", 16),fg="black")
t3 = Label(window, text = "Unit",font=("Helvetica", 16),fg="black")
t1.place(x=15,y=65)
t2.place(x=515,y=65)
t3.place(x=715,y=65)


btu1 = button_text_unit(window,15,100,label_text = "pH",unit_text="---")
btu2 = button_text_unit(window,15,140,label_text= "Colour( pt. Co. Scale)",unit_text="---")
btu3 = button_text_unit(window,15,180,label_text= "Temperature",unit_text="°C")
btu4 = button_text_unit(window,15,220,label_text= "Total Suspended Solids",unit_text="mg/L")
btu5 = button_text_unit(window,15,260,label_text= "Total Dissolved Solids",unit_text="mg/L")
btu6 = button_text_unit(window,15,300,label_text= "Oil & Grease",unit_text="mg/L")
btu7 = button_text_unit(window,15,340,label_text= "Ammonical    Nitrogen    as NH3-N",unit_text="mg/L")
btu8 = button_text_unit(window,15,380,label_text= "Bio Chemical Oxygen Demand@27 °C for 3Days",unit_text="mg/L")
btu9 = button_text_unit(window,15,420,label_text= "Sulphate as SO4",unit_text="mg/L")
btu10 = button_text_unit(window,15,460,label_text="Chemical Oxygen Demand",unit_text="mg/L")
btu11 = button_text_unit(window,15,500,label_text="Phenolic Compound",unit_text="mg/L")



def generate_report():
    new_window = Toplevel(window)
    new_window.geometry("1000x700")

    l1 = Label(new_window, text = "Parameter",font=("Helvetica", 16),fg="black")
    l2 = Label(new_window, text = "Result",font=("Helvetica", 16),fg="black")
    l3 = Label(new_window, text = "Unit",font=("Helvetica", 16),fg="black")
    l1.place(x=15,y=65)
    l2.place(x=515,y=65)
    l3.place(x=715,y=65)
    for i in range(len(list_of_btu)):
        c1 = Label(new_window, text = list_of_btu[i].b["text"],font=("Helvetica", 16),fg="black")
        c1.place(x = 15, y = 120 + i*50)
        c2 = Label(new_window, text = list_of_btu[i].txt.get(),font=("Helvetica", 16),fg="black")
        c2.place(x = 515, y = 120 + i*50)
        c3 = Label(new_window,text = list_of_btu[i].unit["text"],font=("Helvetica", 16),fg="black")
        c3.place(x = 715, y = 120 + i*50)
        


submit = Button(window,text="Submit", padx = 20,pady = 5,font=("Helvetica",16),bg="red",command=generate_report)
submit.place(x=550,y=550)



window.mainloop()
