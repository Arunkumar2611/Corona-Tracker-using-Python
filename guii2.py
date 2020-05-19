import requests
import bs4
import tkinter as tk
from tkinter import *
import plyer
import time
import datetime

def get_html_data(url):
    data = requests.get(url)
    return data

def get_cororna_details_of_World():
    url = "https://www.worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").find_all("div", {"id": "maincounter-wrap"})
    # print(info_div)
    all_detail=""
    for block in info_div:
        text = block.find("h1").get_text()
        count = block.find("div", class_="maincounter-number").find("span").get_text()
        # print(text+" : "+count)
        all_detail = all_detail + text + "\n"+count+"\n\n"
    return all_detail










def get_cororna_details_of_India():
    url = "https://www.worldometers.info/coronavirus/country/india/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").find_all("div", {"id": "maincounter-wrap"})
    # print(info_div)
    all_detail = ""
    for block in info_div:
        text = block.find("h1").get_text()
        count = block.find("div", class_="maincounter-number").find("span").get_text()
        # print(text+" : "+count)
        all_detail = all_detail + text + "\n" + count + "\n\n"
    return all_detail



def get_cororna_details_of_China():
    url = "https://www.worldometers.info/coronavirus/country/china/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").find_all("div", {"id": "maincounter-wrap"})
    # print(info_div)
    all_detail = ""
    for block in info_div:
        text = block.find("h1").get_text()
        count = block.find("div", class_="maincounter-number").find("span").get_text()
        # print(text+" : "+count)
        all_detail = all_detail + text + "\n" + count + "\n\n"
    return all_detail


def get_cororna_details_of_japan():
    url = "https://www.worldometers.info/coronavirus/country/japan/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").find_all("div", {"id": "maincounter-wrap"})
    # print(info_div)
    all_detail = ""
    for block in info_div:
        text = block.find("h1").get_text()
        count = block.find("div", class_="maincounter-number").find("span").get_text()
        # print(text+" : "+count)
        all_detail = all_detail + text + "\n" + count + "\n\n"
    return all_detail


def get_cororna_details_of_russia():
    url = "https://www.worldometers.info/coronavirus/country/russia/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").find_all("div", {"id": "maincounter-wrap"})
    # print(info_div)
    all_detail = ""
    for block in info_div:
        text = block.find("h1").get_text()
        count = block.find("div", class_="maincounter-number").find("span").get_text()
        # print(text+" : "+count)
        all_detail = all_detail + text + "\n" + count + "\n\n"
    return all_detail



root = Tk()
root.geometry('800x600')
root.title('Corona Tracker Application')
root.configure(bg='cyan')
root.minsize(800, 600)
root.maxsize(800, 600)

banner = PhotoImage(file="corona.png")
bannerLable = Label(root, image=banner, bg="gainsboro")
bannerLable.pack(fill=X)

rootlabel = Label(root, text="Live Corona Tracker", bg="gainsboro", fg="green", pady=10, font=("sanserif", 20, "bold"))
rootlabel.pack(fill=X)

f1 = Frame(root, bg="grey", borderwidth=50)
f1.pack(side=LEFT, fill='y')
l = Label(f1, text="World corona Status", bg="grey", fg="black", pady=10, font=("sanserif", 20, "bold"))
l.pack(side="top")
Label(f1, text=get_cororna_details_of_World(), bg="grey", font=("Helvetica", 16)).pack()


label1 = tk.Label(master=f1, text="Countries", bg="grey", pady=2, padx=43, font=("sanserif", 20, "bold"))
label1.place(x=40, y=290)


l = Label(root, text="Countries corona Status", bg="cyan", fg="black", pady=10, font=("sanserif", 20, "bold"))
l.pack(side="top", padx=5, pady=48)


# drop down menu
def show():
    myLabel = Label(root, text=clicked.get()).pack()

option = [
    "India",
    "Russia",
    "China",
    "Japan"
]

clicked = StringVar()
clicked.set(option[0])
# print(clicked.get())

drop = OptionMenu(root, clicked, *option)
drop.config(width=15, font=('Helvetica', 12), bg="grey")
drop.place(x=110, y=450)




labelTest = tk.Label(text="", font=('Helvetica', 16), fg='red', bg='cyan')
labelTest.pack(side="top")

labelTesting = tk.Label(text="", font=('Helvetica', 16), fg='dark slate gray', bg='cyan')
labelTesting.pack(side="top")

def callback(*args):
    labelTest.configure(text="{}".format(clicked.get()))
    value = format(clicked.get())
    if value == "India":
        labelTesting.configure(text="\n{}".format(get_cororna_details_of_India()))

    if value == "China":
        labelTesting.configure(text="\n{}".format(get_cororna_details_of_China()))

    if value == "Japan":
        labelTesting.configure(text="\n{}".format(get_cororna_details_of_japan()))

    if value == "Russia":
        labelTesting.configure(text="\n{}".format(get_cororna_details_of_russia()))


clicked.trace("w", callback)

# mybutton = Button(f1, text="show selection", command=callback).pack()

root.mainloop()

