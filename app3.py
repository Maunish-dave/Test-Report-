from tkinter import *
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

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

        self.option_list = [
            "IS 3025 (Part-11) –1983/Reaffirmed 2017",
            "APHA 23RDEdition, 2017,Method2120-C",
            "APHA 23RD Edition, 2017,Method 2550 B",
            "IS 3025 (Part 17):1984/ Reaffirmed 2017",
            "IS 3025 (Part 16):1984/ Reaffirmed 2017",
            "APHA 23RDEdition, 2017,Method -5520 B",
            "IS 3025 (Part 34):1988/ Reaffirmed 2014",
            "IS 3025 (Part 44):1993/ Reaffirmed 2014",
            "APHA 23RDEdition, 2017,Method 4500-SO42-E",
            "IS 3025 (Part 32):1988/Reaffirmed 2014",
            "IS 3025 (Part 58):2006/ Reaffirmed 2017",
            "APHA 23RDEdition, 2017, Method 5530-D",
            ]
        self.option_variable = StringVar(window)
        self.option_variable.set(self.option_list[0])
        self.opt = OptionMenu(window,self.option_variable,*self.option_list)
        self.opt.config(width = 40,font=('Helvetica',12),state=DISABLED)
        self.opt.place(x = self.x + 800, y = self.y)
        
    def enable(self):
        if self.txt["state"] == "disabled":
            self.txt.configure(state = 'normal')
            self.b["fg"] = "black"
            self.unit["fg"] = "black"
            self.opt.configure(state="normal")
            list_of_btu.append(self)
        else:
            self.txt.configure(state = 'disabled')
            self.b["fg"] = "grey"
            self.unit["fg"] = "grey"
            self.opt.configure(state="normal")
            list_of_btu.remove(self)

   
heading = Label(window, text="Test Report",font=("Helvetica", 30),fg="black")
heading.place(x = 500,y = 0)

t1 = Label(window, text = "Parameter",font=("Helvetica", 16),fg="black")
t2 = Label(window, text = "Result",font=("Helvetica", 16),fg="black")
t3 = Label(window, text = "Unit",font=("Helvetica", 16),fg="black")
t4 = Label(window, text = "Test Method",font=("Helvetica", 16),fg="black")

t1.place(x=15,y=65)
t2.place(x=515,y=65)
t3.place(x=715,y=65)
t4.place(x=815,y = 65)


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
    l4 = Label(new_window, text = "Test Method",font=("Helvetica", 16),fg="black")
        
    l1.place(x=15,y=65)
    l2.place(x=515,y=65)
    l3.place(x=715,y=65)
    l4.place(x =815,y=65)

    data = [["Parameters","Results","Unit","Test Method"]]
    for i in range(len(list_of_btu)):
        c1 = Label(new_window, text = list_of_btu[i].b["text"],font=("Helvetica", 16),fg="black")
        c1.place(x = 15, y = 120 + i*40)
        c2 = Label(new_window, text = list_of_btu[i].txt.get(),font=("Helvetica", 16),fg="black")
        c2.place(x = 515, y = 120 + i*40)
        c3 = Label(new_window,text = list_of_btu[i].unit["text"],font=("Helvetica", 16),fg="black")
        c3.place(x = 715, y = 120 + i*40)
        c4 = Label(new_window,text = list_of_btu[i].option_variable.get(),font=("Helvetica", 16),fg="black")
        c4.place(x = 815, y = 120 + i*40)


        l = [c1["text"],c2["text"],c3["text"],c4["text"]]

        data.append(l)
        
    def generate_pdf(name):
        elements = list()
        doc = SimpleDocTemplate(f"{name}.pdf", pagesize=letter)
        t = Table(data)
        elements.append(t)
        doc.build(elements)
    
    lbl = Label(new_window, text="PDF Name : ",font=("Helvetica",12),fg="grey")
    ent = Entry(new_window, bd=5, text="report pdf")
    btn = Button(new_window,text="Generate Pdf",padx = 40,font=("Helvetica",16),bg="red",command= lambda :generate_pdf(ent.get()))

    lbl.place(x=350,y=600)
    ent.place(x=450,y=600,height=40)
    btn.place(x=600,y = 600)
    

submit = Button(window,text="Submit", padx = 20,pady = 5,font=("Helvetica",16),bg="red",command=generate_report)
submit.place(x=550,y=550)


window.mainloop()
