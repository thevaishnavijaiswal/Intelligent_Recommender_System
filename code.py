from matplotlib import pyplot as plt
from numpy import *
from bs4 import BeautifulSoup
import urllib
import json
import ssl
import re
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Ignore SSL Certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#GRAPHICAL input
window = Tk()
window.title("Welcome to SJ Search Engine")
window.geometry('1200x800')

def graphical(frame2):
    frame2.destroy();
    #frame2.pack_forget()
    frame3=Frame(window,bg='pink',padx=100,pady=50)
    frame3.pack()
   
    for i in range(0,len(y)):
        y[i]=y[i].replace('₹','')
        y[i]=y[i].replace(',','')
        y[i]= int(y[i])
   

    for i in range(0,len(y1)):
        y1[i]= float(y1[i])

    x= arange(10)  

    fig = Figure(figsize=(4,4))
    pr = fig.add_subplot(111)
    pr.bar(x,y,color='red')
    pr.set_title ("Price Comparison", fontsize=16)
    pr.set_ylabel("PRICE", fontsize=14)
    pr.set_xlabel("RANKING OF PRODUCTS", fontsize=14)
   
    canvas = FigureCanvasTkAgg(fig, master=frame3)
    canvas.get_tk_widget().grid(row=1,column=1)
    canvas.draw()
   
    fig2 = Figure(figsize=(4,4))
    ra = fig2.add_subplot(111)
    ra.bar(x,y1,color='blue')
    ra.set_title ("Rating Comparison", fontsize=16)
    ra.set_ylabel("RATING", fontsize=14)
    ra.set_xlabel("RANKING OF PRODUCTS", fontsize=14)

    canvas = FigureCanvasTkAgg(fig2, master=frame3)
    canvas.get_tk_widget().grid(row=1,column=2)
    canvas.draw()
   
    sp6=Label(frame3,text="   ",bg="pink")
    sp6.grid(row=2)
           
    btn3 = Button(frame3, text="BACK",bg="green", command= lambda :details(frame3))
    btn3.grid(row=3,columnspan=3)

   
       
def details(frame3):
    frame3.destroy()
    frame2=Frame(window,bg='pink',width=120,padx=100,pady=50)
    frame2.pack()

    l1=Label(frame2,text="PRODUCT NAME & DESCRIPTION",font=("Times new roman", 15),bg="pink")
    l2=Label(frame2,text="PRICE",font=("Times new roman", 15),bg="pink")
    l3=Label(frame2,text="RATINGS",font=("Times new roman", 15),bg="pink")

    l1.grid(row=0, column=0)
    l2.grid(row=0, column=1)
    l3.grid(row=0, column=2)

    sp1=Label(frame2,text="   ",bg="pink")
    sp1.grid(row=1)

    height = 10
    width = 3
    x1=[]
    for i in range(height): #Rows
        x1.append([])
        for j in range(width): #Columns
            a=StringVar()
            a.set("")
            x1[i].append(a)
            if(j==0):
                b = Entry(frame2,width=50, textvariable=x1[i][j])
                b.grid(row=i+2, column=j)
            else:
                b = Entry(frame2, textvariable=x1[i][j])
                b.grid(row=i+2, column=j)

    for j in range(height):
        x1[j][0].set(name[j])

    for j in range(height):
        x1[j][1].set(y[j])
           
    for j in range(height):
        x1[j][2].set(y1[j])
       
    sp5=Label(frame2,text="   ",bg="pink")
    sp5.grid(row=12)
           
    btn2 = Button(frame2, text="graphical results",bg="green", command= lambda: graphical(frame2))
    btn2.grid(row=13, columnspan=3)

def li():
   
    # Ask Prouct to Search
    #product = input("Enter Product For Search: ")
    product=entry.get()
    product.replace(' ','+')
    print("product : ",product)

    # Try to fetch data
    try:
        print("Trying to fetch data...")

        # Fetch data
        fhand = urllib.request.urlopen('https://www.flipkart.com/search?q='+product, context=ctx).read()

        # Transform our code in well understand format
        soup = BeautifulSoup(fhand, 'html.parser')

        #Extract Price
        price=soup.find_all('div', attrs={"class" : "_1vC4OE"})
        #Extract Price
        rate=soup.find_all('div', attrs={"class" : "hGSR34"})

        # Extracting the Script
        final=soup.find('script', type="application/ld+json")

        print("Recommended Products on",product.replace('+',' '))
       
        # Parsing Code into json structure and iterrate through each item found
        for i,item in enumerate(json.loads(final.text)['itemListElement']):
            print(i+1,item['name'], price[i].text, rate[i].text)
            name.append(item['name'])
            y.append(price[i].text)
            y1.append(rate[i].text)
   
        details(Frame())

           
    except:
        print("Error in fetching the data. Try Again!")


frame=Frame(window,bg='yellow',width=120,padx=100,pady=50)
frame.pack()

head=Label(frame,text="RECOMMENDER")
head.config(font=("Times new roman", 44))
head.grid(row=1)

sp1=Label(frame,text="   ",bg="yellow")
sp1.grid(row=2)

txt=StringVar()
entry=Entry(frame,width=90,textvariable=txt)
entry.grid(row=3)

sp2=Label(frame,text="   ",bg="yellow")
sp2.grid(row=4)

name=list()
y=list()
y1=list()



btn = Button(frame, text="SEARCH",bg="green", command=li)
btn.grid(row=5)


   
window.mainloop()
