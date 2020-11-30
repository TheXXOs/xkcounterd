import tkinter as tk
import requests
from bs4 import BeautifulSoup
from PIL import ImageTk,Image
from io import BytesIO

def comicImg(cNum=""):
    URL = "https://xkcd.com/"+str(cNum)+"/"
    soup = BeautifulSoup(requests.get(URL).content, 'html.parser')
    imgLink = "https:"+soup.find(id='comic').findChildren()[0]["src"]
    imgResp = requests.get(imgLink)
    img = Image.open(BytesIO(imgResp.content))
    return img

def comicTitle(cNum=""):
    URL = "https://xkcd.com/"+str(cNum)+"/"
    soup = BeautifulSoup(requests.get(URL).content, 'html.parser')
    title = soup.find(id="ctitle").text
    return title

def comicAlt(cNum=""):
    URL = "https://xkcd.com/"+str(cNum)+"/"
    soup = BeautifulSoup(requests.get(URL).content, 'html.parser')
    alttext = soup.find(id='comic').findChildren()[0]["title"]
    return alttext

def createPopup(cNum=""):
    popup = tk.Tk()
    popup.title("Is \""+comicTitle(cNum)+"\" correct?")
    popup.iconbitmap("xkcd.ico")
    altLabel = tk.Label(text="Alt text: "+comicAlt(cNum))
    altLabel.pack()
    ipng = comicImg(cNum)
    width, height = ipng.size
    canvas = tk.Canvas(popup,width=width+2,height=height+2)
    canvas.pack()
    popup.geometry(str(width+4)+"x"+str(height+26))
    img = ImageTk.PhotoImage(ipng)
    canvas.create_image(2,2,anchor="nw",image=img)
    popup.mainloop()
createPopup(100)
