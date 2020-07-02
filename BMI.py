from tkinter import*

root = Tk()
root.geometry("1350x650+0+0")
root.resizable(0,0)
root.title('BMI Calculator')

def BMI_Cal():
    BHeight = float(var1.get())
    BWeight = float(var.get())
    BMI = str("%.2f" %(BWeight /(BHeight * BHeight)))
    lb1BMIResult.config(text = BMI)
       

var = DoubleVar()
var1 = DoubleVar()
var2 = DoubleVar()


Tops = Frame(root, width = 1350, height = 50, bd = 8, relief = 'raise')
Tops.pack(side = TOP)


f1 = Frame(root, width = 600, height = 600, bd = 8, relief = 'raise')
f1.pack(side = LEFT)


f2 = Frame(root, width = 300, height = 700, bd = 8, relief = 'raise')
f2.pack(side = RIGHT)


f1a = Frame(f1, width = 600, height = 200, bd = 20, relief = 'raise')
f1a.pack(side = TOP)


f1b = Frame(f1, width = 600, height = 600, bd = 20, relief = 'raise')
f1b.pack(side = TOP)


lblTitle = Label(Tops, text = "       Body Mass Index       ", padx = 16, pady = 16, bd = 16,
                 fg = "#000000", font = ('arial', 54, 'bold'),
                 bg = 'sky blue', relief = 'raise', width = 32, height = 1)
lblTitle.pack()

lblweight = Label(f1a, text = "Select Weight in Kilograms", font = ('arial', 20, 'bold'), bd = 20).grid(row = 0, column = 0)
Bodyweight = Scale(f1a, variable = var, from_= 1, to = 500, length = 880, tickinterval = 30, orient = HORIZONTAL)
Bodyweight.grid(row = 1, column = 0)

lblheight = Label(f1b, text = "Enter Height in Meter Square", font = ('arial', 20, 'bold'), bd = 20).grid(row = 0, column = 0)
txtheight = Entry(f1b, textvariable = var1, font = ('arial', 16, 'bold'), bd = 16, width = 22, justify = 'center')
txtheight.grid(row = 1, column = 0)

lb1BMIResult = Label(f1b,  padx = 16, pady = 16, bd = 16,
                 fg = "#000000", font = ('arial', 30, 'bold'),
                 bg = 'sky blue', relief = 'sunk', width = 34, height = 1)
lb1BMIResult.grid(row = 2, column = 0)

lb1BMITable = Label(f2, font = ('arial', 20, 'bold'), text = 'BMI Table').grid(row = 0 , column = 0)
txtlb1BMITable = Text(f2, height = 12, width = 38, bd = 16, font = ('arial', 12, 'bold'))
txtlb1BMITable.grid(row = 1, column = 0)

txtlb1BMITable.insert(END, 'Meaning\t\t'+ "BMI \n\n")
txtlb1BMITable.insert(END, 'Normal weight \t\t'+ "19-24, 9\n\n")
txtlb1BMITable.insert(END, 'Overweight \t\t'+ "25-29, 9\n\n")
txtlb1BMITable.insert(END, 'Obesity level I \t\t'+ "30-34, 9\n\n")
txtlb1BMITable.insert(END, 'Obesity level II \t\t'+ "35-39, 9\n\n")
txtlb1BMITable.insert(END, 'Obesity level III \t\t'+ ">= 40\n\n")

btnBMI = Button(f2, text ="Click to \nCheck your \nBMI", padx = 8, pady = 8, bd = 12, width = 21,
                font = ('arial', 20, 'bold'), height = 3, command = BMI_Cal)
btnBMI.grid(row = 2, column = 0)


root.mainloop()
