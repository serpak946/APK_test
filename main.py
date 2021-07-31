from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
import requests
from bs4 import BeautifulSoup




class MyApp(App):
    RUP1=0
    USD1=0
    RUB1=0
    MDL1=0
    UAH1=0
    EUR1=0

    def RUPCH(self, instance, text):
        global RUP1, k
        try:
            if text=='': text='0'
            RUP1=float(text)
            self.code()
        except ValueError:
            RUP1=0
            k=5
            self.code()

    def USDCH(self, instance, text):
        global USD1, k
        try:
            if text=='': text='0'
            USD1=float(text)
            self.code()
        except ValueError:
            USD1=0
            k=5
            self.code()

    def RUBCH(self, instance, text):
        global RUB1, k
        try:
            if text=='': text='0'
            RUB1=float(text)
            self.code()
        except ValueError:
            RUB1=0
            k=5
            self.code()

    def MDLCH(self, instance, text):
        global MDL1, k
        try:
            if text=='': text='0'
            MDL1=float(text)
            self.code()
        except ValueError:
            MDL1=0
            k=5
            self.code()

    def UAHCH(self, instance, text):
        global UAH1, k
        try:
            if text=='': text='0'
            UAH1=float(text)
            self.code()
        except ValueError:
            UAH1=0
            k=5
            self.code()

    def EURCH(self, instance, text):
        global EUR1, k
        try:
            if text=='': text='0'
            EUR1=float(text)
            self.code()
        except ValueError:
            k=5
            EUR1=0
            self.code()

    def build(self):
        global RUPL, USDL, RUBL, MDLL, UAHL, EURL
        wn=BoxLayout(orientation='vertical')
        wn.padding = 15
        wn.spacing = 5
        Window.clearcolor = (0.1254901960784314, 0.3254901960784314, 0.4549019607843137, 1)
        self.RUPT=TextInput(hint_text='RUP', multiline=False)
        self.RUPT.input_type = 'number'
        self.RUPT.foreground_color = (0.83,0.96,0.81,1)
        self.RUPT.background_color =(0.1092,0.4482,0.4426,1)
        wn.add_widget(self.RUPT)
        self.USDT=TextInput(hint_text='USD', multiline=False)
        self.USDT.input_type = 'number'
        self.USDT.foreground_color = (0.83,0.96,0.81,1)
        self.USDT.background_color =(0.1092,0.4482,0.4426,1)
        wn.add_widget(self.USDT)
        self.RUBT = TextInput(hint_text='RUB', multiline=False)
        self.RUBT.input_type = 'number'
        self.RUBT.foreground_color = (0.83,0.96,0.81,1)
        self.RUBT.background_color =(0.1092,0.4482,0.4426,1)
        wn.add_widget(self.RUBT)
        self.MDLT = TextInput(hint_text='MDL', multiline=False)
        self.MDLT.input_type = 'number'
        self.MDLT.foreground_color = (0.83,0.96,0.81,1)
        self.MDLT.background_color =(0.1092,0.4482,0.4426,1)
        wn.add_widget(self.MDLT)
        self.UAHT = TextInput(hint_text='UAH', multiline=False)
        self.UAHT.input_type = 'number'
        self.UAHT.foreground_color = (0.83,0.96,0.81,1)
        self.UAHT.background_color =(0.1092,0.4482,0.4426,1)
        wn.add_widget(self.UAHT)
        self.EURT = TextInput(hint_text='EUR', multiline=False)
        self.EURT.input_type = 'number'
        self.EURT.foreground_color = (0.83,0.96,0.81,1)
        self.EURT.background_color =(0.1092,0.4482,0.4426,1)
        wn.add_widget(self.EURT)
        self.RUPT.bind(text=self.RUPCH)
        self.USDT.bind(text=self.USDCH)
        self.RUBT.bind(text=self.RUBCH)
        self.MDLT.bind(text=self.MDLCH)
        self.UAHT.bind(text=self.UAHCH)
        self.EURT.bind(text=self.EURCH)
        self.text=Label(text='Сумма')
        self.text.font_size = 40
        self.text.color = (0.83,0.96,0.81,1)
        wn.add_widget(self.text)
        self.RUPL=Label(text='RUP = 0',halign="left", valign="middle")
        self.RUPL.bind(size=self.RUPL.setter('text_size'))
        self.RUPL.font_size = 25
        self.RUPL.color = (0.83,0.96,0.81,1)
        wn.add_widget(self.RUPL)
        self.USDL=Label(text='USD = 0',halign="left", valign="middle")
        self.USDL.bind(size=self.USDL.setter('text_size'))
        self.USDL.font_size = 25
        self.USDL.color = (0.83,0.96,0.81,1)
        wn.add_widget(self.USDL)
        self.RUBL=Label(text='RUB = 0',halign="left", valign="middle")
        self.RUBL.bind(size=self.RUBL.setter('text_size'))
        self.RUBL.font_size = 25
        self.RUBL.color = (0.83,0.96,0.81,1)
        wn.add_widget(self.RUBL)
        self.MDLL=Label(text='MDL = 0',halign="left", valign="middle")
        self.MDLL.bind(size=self.MDLL.setter('text_size'))
        self.MDLL.font_size = 25
        self.MDLL.color = (0.83,0.96,0.81,1)
        wn.add_widget(self.MDLL)
        self.UAHL=Label(text='UAH = 0',halign="left", valign="middle")
        self.UAHL.bind(size=self.UAHL.setter('text_size'))
        self.UAHL.font_size = 25
        self.UAHL.color = (0.83,0.96,0.81,1)
        wn.add_widget(self.UAHL)
        self.EURL=Label(text='EUR = 0',halign="left", valign="middle")
        self.EURL.bind(size=self.EURL.setter('text_size'))
        self.EURL.font_size = 25
        self.EURL.color = (0.83,0.96,0.81,1)
        wn.add_widget(self.EURL)



        return wn

    def code(self):
        global k
        if k<6:
            k+=1
            self.RUPL.text = 'RUP = 0.0'
            self.USDL.text = 'USD = 0.0'
            self.RUBL.text = 'RUB = 0.0'
            self.UAHL.text = 'UAH = 0.0'
            self.MDLL.text = 'MDL = 0.0'
            self.EURL.text = 'EUR = 0.0'
        else:
            SUMRUP = RUP1 + (USD1 * a8) + (RUB1 * a2) + (MDL1*a19) + (UAH1 * a3) + (EUR1*a17)
            SUMRUB = RUB1 + (RUP1 / a1) + (USD1 * a9) + (EUR1 * a15) + ((MDL1*a19)/a1) + ((UAH1*a3)/a1)
            SUMUSD = USD1 + (RUP1 / a7) + (RUB1 / a10) + (EUR1 * a13) + ((MDL1*a19)/a7) + ((UAH1*a3)/a7)
            SUMUAH = UAH1 + ((RUP1 + (USD1 * a8) + (RUB1 * a2) + (MDL1 * a19) + (EUR1 * a17)) / a4)
            SUMMDL = MDL1 + ((RUP1 + (USD1 * a8) + (RUB1 * a2) + (UAH1 * a3) + (EUR1 * a17)) / a5)
            SUMEUR = EUR1 + (RUP1 / a18) + (RUB1 / a16) + (USD1 / a14) + ((MDL1 * a19) / a18) + ((UAH1 * a3) / a18)
            self.RUPL.text = 'RUP = '+str(round(SUMRUP, 2))
            self.USDL.text = 'USD = ' + str(round(SUMUSD, 2))
            self.RUBL.text = 'RUB = ' + str(round(SUMRUB, 2))
            self.UAHL.text = 'UAH = ' + str(round(SUMUAH, 2))
            self.MDLL.text = 'MDL = ' + str(round(SUMMDL, 2))
            self.EURL.text = 'EUR = ' + str(round(SUMEUR, 2))


URL = 'https://www.agroprombank.com/info/rates.html'
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
           "Accept-Encoding": "*",
           "Connection": "keep-alive"
           }


def get_html(url, params=None):
    '''Заходим на сайт'''
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    """"Из всего кода отделяем стоимость и берём 55 и 56 строчку, где находится RUB/RUP"""
    global pok
    global prod
    global pok1
    global prod1
    global prod2
    global items
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('td', class_='td')
    pok = (items[55].get_text())
    pok1 = float(pok)
    prod = (items[56].get_text())
    prod1 = float(prod)


def parse():
    """Проверяем, подключились ли мы к сайту"""
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


parse()
# print(items)
a1 = (items[56].get_text())
a2 = (items[55].get_text())
a3 = (items[52].get_text())
a4 = (items[53].get_text())
a5 = (items[50].get_text())
a6 = (items[49].get_text())
a7 = (items[38].get_text())
a8 = (items[37].get_text())
a9 = (items[34].get_text())
a10 = (items[35].get_text())
a11 = (items[32].get_text())
a12 = (items[31].get_text())
a13 = (items[40].get_text())
a14 = (items[41].get_text())
a15 = (items[43].get_text())
a16 = (items[44].get_text())
a17 = (items[46].get_text())
a18 = (items[47].get_text())
a19 = (items[49].get_text())
a20 = (items[50].get_text())

# print(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)

a1=float(a1)
a2=float(a2)
a3=float(a3)
a4=float(a4)
a5=float(a5)
a6=float(a6)
a7=float(a7)
a8=float(a8)
a9=float(a9)
a10=float(a10)
a11=float(a11)
a12=float(a12)
a13=float(a13)
a14=float(a14)
a15=float(a15)
a16=float(a16)
a17=float(a17)
a18=float(a18)
a19=float(a19)
a20=float(a20)

k=0

MyApp().run()
