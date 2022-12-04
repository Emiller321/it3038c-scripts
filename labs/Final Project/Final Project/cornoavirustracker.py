import requests     
from bs4 import BeautifulSoup
import plyer
import pandas as pd
from tkinter import *
from tkinter import messagebox,filedialog

def datacollected():
    def notification(title, message):
        plyer.notification.notify( 
        title= title,
        message= message,
        app_icon = 'coronaIcon.ico.ico', ###Brings up the icon I downloaded in the application
        timeout = 15      
        )

    ###URL where I am grabbing the data from
    url = "https://www.worldometers.info/coronavirus/" 
    res = requests.get(url)      
    soup = BeautifulSoup(res.content,'html.parser') 
    tbody = soup.find('tbody')
    abc = tbody.find_all('tr')

    ###If user does not input anything into the filles blank in app it will default to grabbing data from the whole world
    countrynotification = cntdata.get()
    if(countrynotification == " "):
        countrynotification = "world"

    ###Info I intend to grab and use from the URL
    countries , total_cases , new_cases , total_death , new_deaths, total_recovered,active_cases, total_tests, total_pop = [],[],[],[],[],[],[],[],[]
    header = ['countries' , 'total_cases' , 'new_cases' , 'total_death' , 'new_deaths', 'total_recovered','active_cases', 'total_tests', 'total_pop' ]
    for i in abc:
        id = i.find_all('td')
        if(id[1].text.strip() == countrynotification):
            totalcases1 = int(id[2].text.strip().replace(',',""))
            totaldeath = id[4].text.strip() 
            newcases = id[3].text.strip()
            newdeaths = id[5].text.strip()
            notification("Corona Virus Update of {}".format(countrynotification),
                        "Total Cases : {}\nTotal Deaths : {}\nNew Cases : {}\nNew Deaths : {}".format(totalcases1,totaldeath,newcases,newdeaths))
        countries.append(id[1].text.strip())
        total_cases.append(id[2].text.strip().replace(',',""))  
        new_cases.append(id[3].text.strip())
        new_deaths.append(id[5].text.strip())
        total_death.append(id[4].text.strip())
        total_recovered.append(id[6].text.strip())
        active_cases.append(id[7].text.strip())
        total_tests.append(id[8].text.strip())
        total_pop.append(id[9].text.strip())
    
    ###Dataframe used from pandas
    dataframe = pd.DataFrame(list(zip(countries , total_cases , new_cases , total_death ,new_deaths, total_recovered,active_cases, total_tests, total_pop)),columns=header)

    ###Sorting the format byfile type 
    sorts = dataframe.sort_values('total_cases',ascending = False)
    for a in flist:
        if (a == 'html'):
            path2 = '{}/coronadata.html'.format(path)
            sorts.to_html(r'{}'.format(path2))
           
        if (a == 'json'):
            path2 = '{}/coronadata.json'.format(path)
            sorts.to_json(r'{}'.format(path2))

        if (a == 'csv'):
            path2 = '{}/coronadata.csv'.format(path)
            sorts.to_csv(r'{}'.format(path2))

        if (a == 'xml'):
            path2 = '{}/coronadata.xml'.format(path)
            sorts.to_xml(r'{}'.format(path2))

        ###This notification will pop up once you choose a file type and save it on your computer
        if(len(flist) != 0):
            messagebox.showinfo("Notification","Corona Record has been saved too {}".format(path2),parent =app)

def downloaddata():
    global path
    if(len(flist) != 0):
        path = filedialog.askdirectory()
    else:
        pass
    datacollected()
    flist.clear()    
    Inhtml.configure(state = 'normal')
    Injson.configure(state = 'normal')
    Inexcel.configure(state = 'normal')
    Inxml.configure(state = 'normal')

def inhtmldownload():
    flist.append('html')
    Inhtml.configure(state = 'disabled')

def injsondownload():
    flist.append('json')
    Injson.configure(state = 'disabled')

def inexceldownload():
    flist.append('csv')
    Inexcel.configure(state = 'disabled')

def inxmldownload():
    flist.append('xml')
    Inxml.configure(state = 'disabled')

###Created the GUI of app
app = Tk()
app.title("Corona Virus Information")
app.geometry('1000x1000+200+80')
app.configure(bg='#ccff33')
app.iconbitmap('coronaIcon.ico.ico')  
flist = []
path = ''

### Made 3 Labels
mainlabel = Label(app,text="Corona Virus Live Tracker",font=("new roman",30,"italic bold"), bg = "#ccff33",width=33
                        ,fg = "black",bd=5)
mainlabel.place(x=0,y=0)


label1 = Label(app,text="Country Name",font=("new roman",20,"italic bold"), bg = "#ccff33")
label1.place(x=15,y=100)

label2 = Label(app,text="Download File in ",font=("new roman",20,"italic bold"), bg = "#ccff33")
label2.place(x=15,y=200)

###Made One Data Entry
cntdata = StringVar()
entry1 = Entry(app,textvariable = cntdata ,font = ("new roman",20,"italic bold"), relief = RIDGE,bd = 2 , width = 32)
entry1.place(x = 280, y = 100)

### Made 5 Buttons
Inhtml = Button(app,text = "HTML", bg = "#6699ff", font = ("new roman",15,"italic bold"),relief = RIDGE,activebackground = "#05945B",
                activeforeground = "white",bd = 7,width = 35,command = inhtmldownload)
Inhtml.place(x = 300, y = 200)

Injson = Button(app,text = "JSON", bg = "#6699ff", font = ("new roman",15,"italic bold"),relief = RIDGE,activebackground = "#05945B",
                activeforeground = "white",bd = 7,width = 35,command = injsondownload)
Injson.place(x = 300, y = 260)

Inexcel = Button(app,text = "EXCEL", bg = "#6699ff", font = ("new roman",15,"italic bold"),relief = RIDGE,activebackground = "#05945B",
                activeforeground = "white",bd = 7,width = 35,command = inexceldownload)
Inexcel.place(x = 300, y = 320)

Inxml = Button(app,text = "XML", bg = "#6699ff", font = ("new roman",15,"italic bold"),relief = RIDGE,activebackground = "#05945B",
                activeforeground = "white",bd = 7,width = 35,command = inxmldownload)
Inxml.place(x = 300, y = 380)

Submit = Button(app,text = "SUBMIT", bg = "#cc3300", font = ("new roman",15,"italic bold"),relief = RIDGE,activebackground = "#7B0519",
                activeforeground = "white",bd = 7,width = 35,command = downloaddata)
Submit.place(x = 300, y = 440)

###Will keep the page in a continuous loop until user exits the application
app.mainloop()