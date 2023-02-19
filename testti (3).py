from tkinter import *
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup
from customtkinter import *
from tkinter import ttk
import webbrowser

def rech(param):
    page = requests.get(
        "https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q="+param)
    soup = BeautifulSoup(page.content, 'html.parser')
    X = soup.find_all("div", {"class": "css-1gatmva e1v1l3u10"})
    jobs = []
    for i in X:
        # image=i.find("img")
        divat = i.find('div').find_all("div")
        title = divat[0].find("h2").text
        URL=divat[0].find("h2").find("a")["href"]
        desc = divat[1].text

        # print(image)
        jobs.append(job(title, desc,URL))
    return jobs


class job:
    def __init__(self, title, desc,URL) -> None:
        self.title = title
        self.desc = desc
        self.URL= URL



rech("Android")
set_appearance_mode("Dark")
root = CTk()
root.geometry("1000x700")
root.resizable(False, False)
valeur = StringVar()
valeur.set("Welcome TO WUZZUF")
h = Frame(root, background="#222222")
my_img = ImageTk.PhotoImage(Image.open("w.png").resize((50, 50)))
l1 = CTkLabel(
    h, image=my_img, text="", bg_color='transparent').pack(side='left')
header = CTkLabel(h, text="", textvariable=valeur, font=(
    'times', 21, 'bold'), bg_color='#222222')
inputsearch = CTkEntry(
    root, placeholder_text="Search here")
h.pack(fill="x")
btnsearch = CTkButton(
    root, text="Search", command=lambda: recherche())
header.pack()

CTkLabel(root, text="", bg_color='transparent').pack()
inputsearch.pack(fill='x')
CTkLabel(root, text="", bg_color='transparent').pack()
btnsearch.pack()
f = Frame(root)
f.pack()


def recherche():
    global f
    global valeur
    f.pack_forget()
    f = CTkScrollableFrame(root)
    f.pack(fill="both")
    jobs = rech(inputsearch.get())
    valeur.set(inputsearch.get())
    inputsearch.delete('0', END)

    for i in jobs:
        x = Frame(f, background="#2e76a6", bg="#2e76a6" )
        Label(x, text=i.title, background="#2e76a6").pack(fill="x")
        Label(x, text=i.desc, background="#2e76a6").pack(fill="x")
        CTkButton(x,command=lambda:webbrowser.get("windows-default").open("http:\\www.wuzzuf.net"+i.URL),text="see more and apply").pack()
        ttk.Separator(f, orient='horizontal').pack(fill="x")
        x.pack(fill="x")
        


root.mainloop()
