from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import tkinter as tk

window = tk.Tk()

window.title("Duyurular")

window.geometry("900x550")
T1 = tk.Text(window, height = 11, width = 250)
T2 = tk.Text(window, height = 11, width = 250)
T3 = tk.Text(window, height = 11, width = 250)


url = "https://bm.erciyes.edu.tr/?Duyurular"
sayfa = urllib.request.urlopen(url)
soup = BeautifulSoup(sayfa, "html.parser")
ana = soup.find('body')
alt=ana.findAll('h5',attrs={"class":"entry-title text-white text-uppercase m-0 mt-5"})
list = []
for i in range(10):
    title = alt[i].text
    list.append(title)

url_a = "https://obisis.erciyes.edu.tr/"
sayfa_a = urllib.request.urlopen(url_a)
soup_a = BeautifulSoup(sayfa_a, "lxml")# html.parser only finds one text between tags for this spesific page both "lxml" and "html5lib" parsers could be used. Warning "html5lib" parser does not support Turkish characters.

ana_a = soup_a.find("table",attrs={"id":"ctl03_dlDuyuru"})
alt_a=ana_a.findAll("span",attrs={"class": "NormalBlue"})
list_a = []

for x in range(10):
    title_a = alt_a[x].text
    list_a.append(title_a)


list_a = [s.strip('\r\n        ') for s in list_a]
url_muh = "https://mf.erciyes.edu.tr/?Duyurular"
sayfa_muh = urllib.request.urlopen(url_muh)
soup_muh = BeautifulSoup(sayfa_muh, "html.parser")
ana_muh = soup_muh.find('div',attrs={"class":"tab-pane fade in active","id":"Guncel_Duyurular"})
alt_muh=ana_muh.findAll('h5',attrs={"class":"entry-title text-white text-uppercase m-0 mt-5"})
list_muh = []

for j in range(10):
    title_muh = alt_muh[j].text
    list_muh.append(title_muh)

T1.insert(tk.INSERT,"-------------------- BILGISAYAR MUHENDISLIGI --------------------\n\n")
T2.insert(tk.INSERT,"-------------------- OBISIS --------------------\n\n")
T3.insert(tk.INSERT,"-------------------- MUHENDISLIK FAKULTESİ --------------------\n\n")
for a in range(10):
    if a==0:
        T1.insert(tk.INSERT,"-->"+ list[a]+"\n\n")
        T2.insert(tk.INSERT,"-->"+ list_a[a]+"\n\n")
        T3.insert(tk.INSERT,"-->"+ list_muh[a]+"\n\n")

    else:
        T1.insert(tk.END, "-->" + list[a] + "\n")
        T2.insert(tk.END, "-->" + list_a[a] + "\n")
        T3.insert(tk.END, "-->" + list_muh[a] + "\n")
T1.pack()
T2.pack()
T3.pack()
window.mainloop()

