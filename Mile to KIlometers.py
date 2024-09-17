import tkinter
def cacl():
    global km_value
    km_value = int(input.get()) * 1.609344
    km.config(text=f'is equal to           {round(km_value)}              km',font=('Arial',15,'normal'))
km_value = 0
window = tkinter.Tk()
window.title('Mile to Kilometer GUI')
window.minsize(width=400,height=100)
input = tkinter.Entry(width=13,font=10)
input.place(x=160,y=60)
miles = tkinter.Label(text='Miles',font=('Arial',15,'normal'))
miles.place(x=290,y=60)
km = tkinter.Label(text=f'is equal to           {km_value}              km',font=('Arial',15,'normal'))
km.place(x=50,y=90)
button = tkinter.Button(text='Calculate!',command=cacl)
button.place(x=185,y=120)
tkinter.mainloop()
