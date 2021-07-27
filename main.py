from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window




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

if __name__ == '__main__':
    k=0
    MyApp().run()
