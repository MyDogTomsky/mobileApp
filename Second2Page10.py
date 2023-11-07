from kivy.app import App
from kivy.uix.boxlayout import BoxLayout #Kivy layout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager,Screen
from Sec10Third import SecThird10Page
from Fourth4Page import FourthPage
from Wstarter1 import Weststartersare
from Wmain2 import Westmainsare
from Wdessert3 import Westdessertsare
from kivy.uix.popup import Popup
import os

class eu2page(App):
    def build(self) : 
        self.pageTurner = ScreenManager()
        self.pageSecond10 = SecondPage10(app=self)
        secondscreen = Screen(name = 'secondscreen')
        secondscreen.add_widget(self.pageSecond10)
        self.pageTurner.add_widget(secondscreen)

        self.pageSec10 = SecThird10Page(app=self)
        secondinfoscreen = Screen(name = 'secondinfoscreen')
        secondinfoscreen.add_widget(self.pageSec10)
        self.pageTurner.add_widget(secondinfoscreen)

        self.pageFourth = FourthPage(app=self)
        fourthscreen = Screen(name = 'fourthscreen')
        fourthscreen.add_widget(self.pageFourth)
        self.pageTurner.add_widget(fourthscreen)

#------------------------------------------- Data Filtering ---------------------
        self.pageWest1 = Weststartersare(app=self,fourthpage=self.pageFourth)
        weststarterscreen = Screen(name = 'weststarterscreen')
        weststarterscreen.add_widget(self.pageWest1)
        self.pageTurner.add_widget(weststarterscreen)

        self.pageWest2 = Westmainsare(app=self,fourthpage = self.pageFourth)
        westmainscreen = Screen(name = 'westmainscreen')
        westmainscreen.add_widget(self.pageWest2)
        self.pageTurner.add_widget(westmainscreen)

        self.pageWest3 = Westdessertsare(app=self,fourthpage = self.pageFourth)
        westdessertscreen = Screen(name = 'westdessertscreen')
        westdessertscreen.add_widget(self.pageWest3)
        self.pageTurner.add_widget(westdessertscreen)
          

        self.pageTurner.current = 'secondscreen'  
        return self.pageTurner
    
    def goingnextpage(self,value):
        self.pageTurner.current = value
    

class SecondPage10(BoxLayout)   :
    def __init__(self,app, **kwargs):
        super(SecondPage10,self).__init__(**kwargs,orientation = 'vertical')

        self.wsecis = app 
        button20 = Button(
            font_size = 26, markup = True, background_color = '#8BD8BD',
            text ='[color=#F5F5DC]Tip & Info[/color]' )
        button20.bind(on_release = lambda instance : self.wsecis.goingnextpage('secondinfoscreen'))

        self.add_widget(button20)
        #-------------------------------------------------------------------------------
        inputLayout = BoxLayout(orientation = 'horizontal')
         
        button29 = Button(background_color = '#EC4D36') 
        button30 = Button(background_color = '#EC4D36') 

        inputHelper = TextInput(hint_text = 'Type the KEYWORD...!',halign='center',multiline = False)
        inputinner = BoxLayout(orientation = 'vertical')
        keywordinput = BoxLayout(orientation = 'horizontal')
        
        button21left = Image(source = 'images\globallens.png',allow_stretch=True,keep_ratio=False,size_hint=(None, None),size=(100, 100))
        button21 = Button(
             font_size = 15, bold = True, markup = True, background_color = '#8BD8BD',
             text ='[color=#F5F5DC] Enter [/color]' )
        button21.bind(on_release=lambda instance: self.searching(inputHelper.text))
        
        keywordinput.add_widget(inputHelper)
        keywordinput.add_widget(button21)
        inputHelper.size_hint = (0.8,1.0)
        button21.size_hint = (0.2,1.0)
        inputinner.add_widget(button29)
        inputinner.add_widget(keywordinput)
        inputinner.add_widget(button30)
        button29.size_hint = (1.0,0.4)
        keywordinput.size_hint = (1.0,0.2)
        button30.size_hint = (1.0,0.4)
          
        inputLayout.add_widget(button21left)
        inputLayout.add_widget(inputinner)
        
        button21left.size_hint = (0.2,1.0)
        inputinner.size_hint = (0.8,1.0)

        self.add_widget(inputLayout)

        button22 = Button(
             font_size = 16, bold = True, markup = True, background_color = '#8BD8BD',italic = True,\
             text = '[color=#F5F5DC] R e c o m m e n d [/color]')
        
        recommend = BoxLayout(orientation = 'horizontal')
        button23 = Button(
             font_size  = 25,  markup = True, background_color = '#EC4D36',\
             text = '[color=#F5F5DC] Starter [/color]' )
        button23.bind(on_release = lambda instance : self.wsecis.goingnextpage('weststarterscreen'))
        button24 = Button(
             font_size = 25,  markup = True, background_color = '#EC4D36',\
             text = '[color=#F5F5DC] Main [/color]' )
        button24.bind(on_release = lambda instance : self.wsecis.goingnextpage('westmainscreen'))
        button25 = Button(
             font_size = 25,  markup = True, background_color = '#EC4D36',\
             text = '[color=#F5F5DC] Dessert [/color]' )
        button25.bind(on_release = lambda instance : self.wsecis.goingnextpage('westdessertscreen'))
        recommend.add_widget(button23)
        recommend.add_widget(button24)
        recommend.add_widget(button25)

        setlayout2 = BoxLayout(orientation = 'horizontal')
        button26 = Button(
             font_size = 18, markup = True, background_color = '#8BD8BD',\
                text = '[color=#F5F5DC]Go\nBack![/color]',halign='center')
        setlayout2.add_widget(button26)
        button27 = Button(
             font_size = 18, markup = True, background_color = '#8BD8BD',\
                text = '[color=#F5F5DC]Personal\n Setting [/color]',halign='center')
        button27.bind(on_release = lambda instance : self.wsecis.goingnextpage('fourthscreen'))
        setlayout2.add_widget(button27)

        button26.bind(on_release = self.goingtofirst)
        self.add_widget(button22)
        self.add_widget(recommend)
        self.add_widget(setlayout2)

        button20.size_hint = (1.0,0.14)
        inputLayout.size_hint = (1.0,0.27)
        button22.size_hint = (1.0,0.08)
        recommend.size_hint = (1.0,0.38)
        setlayout2.size_hint = (1.0,0.13)


    def goingtofirst(self,instance):
        self.wsecis.goingnextpage('firstscreen')
    
    def searching(self,text) : 
         print("{0} SEARCHING..." .format(text))
         # ★☆★☆ Unit Test For DEVELOPER ------- Whether searching Function Working or NOT ★☆★☆★☆
         image_path = 'images/' +text+ '.jpg'
         noimage = 'images/questionyellow.jpg'

         if os.path.exists(image_path):
              resultImage = Image(source = image_path, size_hint_y = None,height = 200)
              showpopup = Popup(content = resultImage, title = 'This Menu Is ...', size_hint=(None,None), \
                                size = (300,300),title_color = '#F5F5DC',title_size = 16,auto_dismiss=True,\
                                separator_color = [85/255., 107/255., 47/255.,1],title_align = 'center')
              showpopup.open()
         else:
              noimage = Image(source = noimage,size_hint_y = None,height = 200)
              showpopup = Popup(content = noimage,title = 'Sorry, No Image on our DB', size_hint=(None,None),\
                                 size = (300,300),title_color = '#F5F5DC',title_size = 16,auto_dismiss=True,\
                                 separator_color = [85/255., 107/255., 47/255.,1],title_align = 'center')
              showpopup.open()
                  

if __name__ == '__main__':
    eu2page().run()