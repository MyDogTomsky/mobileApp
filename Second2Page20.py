from kivy.app import App
from kivy.uix.boxlayout import BoxLayout #Kivy layout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen,ScreenManager
from Sec20Third import SecThird20Page
from Fourth4Page import FourthPage
from KJdessert3 import KorJpdesare
from KJside2 import KorJpssare
from KJmain0 import KorJpma0are
from KJmain1 import KorJpma1are
from kivy.uix.popup import Popup
import os


class kj2page(App):
   def build(self) :
     self.pageTurner = ScreenManager()
     self.pageSecond20 = SecondPage20(app=self)
     stwoscreen = Screen(name = 'stwoscreen')
     stwoscreen.add_widget(self.pageSecond20)
     self.pageTurner.add_widget(stwoscreen)

     self.pageSec20 = SecThird20Page(app=self)
     stwoinfoscreen = Screen(name = 'stwoinfoscreen')
     stwoinfoscreen.add_widget(self.pageSec20)
     self.pageTurner.add_widget(stwoinfoscreen)

     self.pageFourth = FourthPage(app=self)
     fourthscreen = Screen(name = 'fourthscreen')
     fourthscreen.add_widget(self.pageFourth)
     self.pageTurner.add_widget(fourthscreen)

#------------------------------------------- Data Filtering ---------------------
     
     self.pageEasia1 = KorJpdesare(app=self,fourthpage = self.pageFourth)
     korjpdesscreen = Screen(name = 'korjpdesscreen')
     korjpdesscreen.add_widget(self.pageEasia1)
     self.pageTurner.add_widget(korjpdesscreen)   

     self.pageEasia2 = KorJpssare(app=self, fourthpage = self.pageFourth)
     korjpsscreen = Screen(name = 'korjpsscreen')
     korjpsscreen.add_widget(self.pageEasia2)
     self.pageTurner.add_widget(korjpsscreen)  
     
     self.pageEasia3 = KorJpma0are(app=self, fourthpage = self.pageFourth)
     korjpm0screen = Screen(name = 'korjpm0screen')
     korjpm0screen.add_widget(self.pageEasia3)
     self.pageTurner.add_widget(korjpm0screen)

     self.pageEasia4 = KorJpma1are(app=self, fourthpage = self.pageFourth)
     korjpm1screen = Screen(name = 'korjpm1screen')
     korjpm1screen.add_widget(self.pageEasia4)
     self.pageTurner.add_widget(korjpm1screen)
      
     self.pageTurner.current = 'stwoscreen'

     return self.pageTurner 
     
   
   def goingnextpage(self,value):
     self.pageTurner.current = value

class SecondPage20(BoxLayout)   :
   def __init__(self,app,**kwargs):
      super(SecondPage20,self).__init__(**kwargs,orientation = 'vertical')
      self.kjsecis = app

      button20 = Button(
      font_size = 26, markup = True, background_color = '#603F83',
      text ='[color=#DF6589]Tip & Info[/color]' )
      button20.bind(on_release = lambda instance : self.kjsecis.goingnextpage('stwoinfoscreen'))

      self.add_widget(button20)
#-------------------------------------------------------------------------------
      inputLayout = BoxLayout(orientation = 'horizontal')
         
      button29 = Button(background_color = '#DF6589') 
      button292 = Button(background_color = '#DF6589') 
      inputHelper = TextInput(hint_text = 'Type the KEYWORD...!',halign='center',multiline = False )
      inputinner = BoxLayout(orientation = 'vertical')
      keywordinput = BoxLayout(orientation = 'horizontal')
     
      button21left = Image(source = 'images\cyberpunk.png',allow_stretch=True,keep_ratio=False,\
                           size_hint=(None, None),size=(100, 100))
      button21 = Button(font_size = 15, bold = True, markup = True, background_color = '#603F83',
                        text ='[color=#F5F5DC] Enter [/color]' )
      button21.bind(on_release=lambda wtfind: self.searching(inputHelper.text))
        
      keywordinput.add_widget(inputHelper)
      keywordinput.add_widget(button21)
      inputHelper.size_hint = (0.8,1.0)
      button21.size_hint = (0.2,1.0)
      inputinner.add_widget(button29)
      inputinner.add_widget(keywordinput)
      inputinner.add_widget(button292)
      button29.size_hint = (1.0,0.4)
      keywordinput.size_hint = (1.0,0.2)
      button292.size_hint = (1.0,0.4)
          
      inputLayout.add_widget(button21left)
      inputLayout.add_widget(inputinner)
        
      button21left.size_hint = (0.2,1.0)
      inputinner.size_hint = (0.8,1.0)

      self.add_widget(inputLayout)

      button22 = Button(font_size = 16, bold = True, markup = True, background_color = '#603F83',italic= True,\
             text = '[color=#F5F5DC] R e c o m m e n d [/color]')
        
      recommend = BoxLayout(orientation = 'horizontal')
      soupornot = BoxLayout(orientation = 'vertical')
      mainsoup = BoxLayout(orientation = 'horizontal')
      mealcomp = BoxLayout(orientation = 'vertical')
      button23 = Button(font_size  = 19,  markup = True, background_color = '#603F83',\
             text = '[color=#99F443] With Soup [/color]',halign = 'center' )
      button23.bind(on_release = lambda instance : self.kjsecis.goingnextpage('korjpm1screen'))
      button24 = Button(font_size = 19,  markup = True, background_color = '#603F83',\
             text = '[color=#99F443] Without Soup [/color]',halign = 'center' )
      button24.bind(on_release = lambda instance : self.kjsecis.goingnextpage('korjpm0screen'))
      button25 = Button(font_size = 19, bold = True, markup = True, background_color = '#603F83',\
             text = '[color=#F5F5DC] Side  Dish [/color]',halign = 'center' )
      button25.bind(on_release = lambda instance : self.kjsecis.goingnextpage('korjpsscreen'))
      button252 = Button(font_size = 20,  markup = True, background_color = '#99F443',\
             text = '[color=#F5F5DC] Dessert [/color]',halign = 'center' )
      button252.bind(on_release = lambda instance : self.kjsecis.goingnextpage('korjpdesscreen'))
      button232=Button(font_size = 22, bold = True, markup = True, background_color = '#99F443',\
             text = '[color=#F5F5DC]Main[/color]',halign = 'center')
      button232.bind(on_release = lambda instance : self.alert_popup())
        
      soupornot.add_widget(button23)
      soupornot.add_widget(button24)
      mainsoup.add_widget(button232)
      mainsoup.add_widget(soupornot)
        
      mealcomp.add_widget(mainsoup)
      mealcomp.add_widget(button25)
      mainsoup.size_hint = (1.0,0.8)
      button25.size_hint = (1.0,0.2)
        
      recommend.add_widget(mealcomp)
      recommend.add_widget(button252)
      mealcomp.size_hint = (0.75,1.0)
      button252.size_hint = (0.25,1.0)

      setlayout2 = BoxLayout(orientation = 'horizontal')
      button26 = Button(font_size = 18, markup = True, background_color = '#603F83',\
                text = '[color=#DF6589]Go\nBack![/color]',halign='center')
      setlayout2.add_widget(button26)
      button27 = Button(font_size = 18, markup = True, background_color = '#603F83',\
                text = '[color=#DF6589]Personal\n Setting [/color]',halign='center')
      button27.bind(on_release = lambda instance : self.kjsecis.goingnextpage('fourthscreen'))
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

   def goingtofirst(self,instance):
        self.kjsecis.goingnextpage('firstscreen')

   def alert_popup(self):
        showpopup = Popup(title = 'Which one ?', content=Label(text='[b]Soup\n  \nOR\n  \n Not ?[/b]',markup = True,halign = 'center'), size_hint=(None,None), \
                                size = (250,200),title_size = 13,title_align = 'center',\
                                separator_color = [50/255., 205/255., 50/255.,1],auto_dismiss=True)
        showpopup.open()     
    
if __name__ == '__main__':
    kj2page().run()