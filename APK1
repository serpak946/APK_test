from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import sys
import time
import requests
from bs4 import BeautifulSoup
import os



class MyApp(App):
    RUP1=0
    USD1=0
    RUB1=0
    MDL1=0
    UAH1=0
    EUR1=0

    def RUPCH(self, instance, text):
        global RUP1
        try:
            if text=='': text='0'
            RUP1=float(text)
            self.code()
        except ValueError:
            RUP1=0
            self.code()

    def USDCH(self, instance, text):
        global USD1
        try:
            if text=='': text='0'
            USD1=float(text)
            self.code()
        except ValueError:
            USD1=0
            self.code()

    def RUBCH(self, instance, text):
        global RUB1
        try:
            if text=='': text='0'
            RUB1=float(text)
            self.code()
        except ValueError:
            RUB1=0
            self.code()

    def MDLCH(self, instance, text):
        global MDL1
        try:
            if text=='': text='0'
            MDL1=float(text)
            self.code()
        except ValueError:
            MDL1=0
            self.code()

    def UAHCH(self, instance, text):
        global UAH1
        try:
            if text=='': text='0'
            UAH1=float(text)
            self.code()
        except ValueError:
            UAH1=0
            self.code()

    def EURCH(self, instance, text):
        global EUR1
        try:
            if text=='': text='0'
            EUR1=float(text)
            self.code()
        except ValueError:
            EUR1=0
            self.code()

    def build(self):
        global RUPL, USDL, RUBL, MDLL, UAHL, EURL
        wn=BoxLayout(orientation='vertical')
        self.RUPT=TextInput(hint_text='RUP', multiline=False)
        self.RUPT.input_type = 'number'
        wn.add_widget(self.RUPT)
        self.USDT=TextInput(hint_text='USD', multiline=False)
        self.USDT.input_type = 'number'
        wn.add_widget(self.USDT)
        self.RUBT = TextInput(hint_text='RUB', multiline=False)
        self.RUBT.input_type = 'number'
        wn.add_widget(self.RUBT)
        self.MDLT = TextInput(hint_text='MDL', multiline=False)
        self.MDLT.input_type = 'number'
        wn.add_widget(self.MDLT)
        self.UAHT = TextInput(hint_text='UAH', multiline=False)
        self.UAHT.input_type = 'number'
        wn.add_widget(self.UAHT)
        self.EURT = TextInput(hint_text='EUR', multiline=False)
        self.EURT.input_type = 'number'
        wn.add_widget(self.EURT)
        self.RUPT.bind(text=self.RUPCH)
        self.USDT.bind(text=self.USDCH)
        self.RUBT.bind(text=self.RUBCH)
        self.MDLT.bind(text=self.MDLCH)
        self.UAHT.bind(text=self.UAHCH)
        self.EURT.bind(text=self.EURCH)
        self.RUPL=Label(text='RUP = 0',halign="left", valign="middle")
        self.RUPL.bind(size=self.RUPL.setter('text_size'))
        wn.add_widget(self.RUPL)
        self.USDL=Label(text='USD = 0',halign="left", valign="middle")
        self.USDL.bind(size=self.USDL.setter('text_size'))
        wn.add_widget(self.USDL)
        self.RUBL=Label(text='RUB = 0',halign="left", valign="middle")
        self.RUBL.bind(size=self.RUBL.setter('text_size'))
        wn.add_widget(self.RUBL)
        self.MDLL=Label(text='MDL = 0',halign="left", valign="middle")
        self.MDLL.bind(size=self.MDLL.setter('text_size'))
        wn.add_widget(self.MDLL)
        self.UAHL=Label(text='UAH = 0',halign="left", valign="middle")
        self.UAHL.bind(size=self.UAHL.setter('text_size'))
        wn.add_widget(self.UAHL)
        self.EURL=Label(text='EUR = 0',halign="left", valign="middle")
        self.EURL.bind(size=self.EURL.setter('text_size'))
        wn.add_widget(self.EURL)



        return wn

    def code(self):
        global k
        if k<6:
            k+=1
        else:
            SUMRUP = RUP1 + (USD1 * a8) + (RUB1 * a2)
            SUMRUB = RUB1 + (RUP1 / a1) + (USD1 * a9)
            SUMUSD = USD1 + (RUP1 / a7) + (RUB1 / a10)
            self.RUPL.text = 'RUP = '+str(round(SUMRUP, 2))
            self.USDL.text = 'USD = ' + str(round(SUMUSD, 2))
            self.RUBL.text = 'RUB = ' + str(round(SUMRUB, 2))


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

# print(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)

a4 = float(a4)
a1 = float(a1)
a2 = float(a2)
a7 = float(a7)
a8 = float(a8)
a9 = float(a9)
a10 = float(a10)
a5 = float(a5)

k=0

MyApp().run()
