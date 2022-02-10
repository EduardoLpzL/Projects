from re import I
from tkinter import *
import parser
from math import factorial

#Let's make a window for our calculator
root = Tk() #Base of the graphic interface also called root
root.title('Calculadora') #titulo de la ventana
#root.iconphoto(True, PhotoImage(file='ani.png')) #Window icon

#Creating Funcionalities
# i keeps tack of the current position on the input text field
i = 0 
#Recieves the digit as parameter and diplays it on the input field
def get_variables(num):
    """Recieves the digit as parameter, The digit is inserte to the input field 
        eith .insert() method with parameters i and num"""
    global i 
    display.insert(i,num)
    i+=1


def get_operation(operator):
    """Recieves the operator as parameter which is then inserted to the text field
        at the ith position"""
    global i 
    length = len(operator)
    display.insert(i, operator)
    i+=length

def clear_all():
    '''Remove all characters int he text field'''
    display.delete(0,END)

def undo():
    '''Use th get() method to fetch the string present on the input field
        Then slices out the last character'''
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,'Error')

def calculate():
    '''We use parse module expr() to scan the string and then use eval to evaluate'''
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all
        display.insert(0, "Error")



"""Designing de buttons"""
# Adding the input field
display = Entry(root) #creates a textbox
display.grid(row=1, columnspan=6, sticky=N+S+E+W)

#Add buttons to the calculator
Button(root, text='1', command=lambda:get_variables(1)).grid(row=2, column=0, sticky=N+S+E+W)
Button(root, text='2', command=lambda:get_variables(2)).grid(row=2, column=1, sticky=N+S+E+W)
Button(root, text='3', command=lambda:get_variables(3)).grid(row=2, column=2, sticky=N+S+E+W)

Button(root, text='4', command=lambda:get_variables(4)).grid(row=3, column=0, sticky=N+S+E+W)
Button(root, text='5', command=lambda:get_variables(5)).grid(row=3, column=1, sticky=N+S+E+W)
Button(root, text='6', command=lambda:get_variables(6)).grid(row=3, column=2, sticky=N+S+E+W)

Button(root, text='7', command=lambda:get_variables(7)).grid(row=4, column=0, sticky=N+S+E+W)
Button(root, text='8', command=lambda:get_variables(8)).grid(row=4, column=1, sticky=N+S+E+W)
Button(root, text='9', command=lambda:get_variables(9)).grid(row=4, column=2, sticky=N+S+E+W)

Button(root, text='AC', command=lambda:clear_all()).grid(row=5, column=0, sticky=N+S+E+W)
Button(root, text='0', command=lambda:get_variables(0)).grid(row=5, column=1, sticky=N+S+E+W)
Button(root, text='.', command=lambda:get_variables('.')).grid(row=5, column=2, sticky=N+S+E+W)

Button(root, text='+', command=lambda:get_operation('+')).grid(row=2, column=3, sticky=N+S+E+W)
Button(root, text='-', command=lambda:get_operation('-')).grid(row=3, column=3, sticky=N+S+E+W)
Button(root, text='*', command=lambda:get_operation('*')).grid(row=4, column=3, sticky=N+S+E+W)
Button(root, text='/', command=lambda:get_operation('/')).grid(row=5, column=3, sticky=N+S+E+W)

# adding new operations
Button(root,text="pi",command= lambda :get_operation("*3.14")).grid(row=2,column=4, sticky=N+S+E+W)
Button(root,text="%",command= lambda :get_operation("%")).grid(row=3,column=4, sticky=N+S+E+W)
Button(root,text="(",command= lambda :get_operation("(")).grid(row=4,column=4, sticky=N+S+E+W)
Button(root,text="exp",command= lambda :get_operation("**")).grid(row=5,column=4, sticky=N+S+E+W)
 
Button(root,text="<-",command= lambda :undo()).grid(row=2,column=5, sticky=N+S+E+W)
Button(root,text="x!", command= lambda: fact()).grid(row=3,column=5, sticky=N+S+E+W)
Button(root,text=")",command= lambda :get_operation(")")).grid(row=4,column=5, sticky=N+S+E+W)
Button(root,text="^2",command= lambda :get_operation("**2")).grid(row=5,column=5, sticky=N+S+E+W)
Button(root,text="^2",command= lambda :get_operation("**2")).grid(row=5,column=5, sticky=N+S+E+W)
Button(root,text="=",command= lambda :calculate()).grid(columnspan=6, sticky=N+S+E+W)

root.mainloop() # Application loop. It is like a while True it alwyas goes at the end of the code