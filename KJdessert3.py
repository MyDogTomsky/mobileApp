from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
import sqlite3
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.clock import Clock
from Fourth4Page import FourthPage
from kivy.uix.screenmanager import Screen,ScreenManager

class KorjpDessert(App):
    def build(self) : 

        self.pageTurner = ScreenManager()

        self.pageFourth = FourthPage(app=self)
        fourthscreen = Screen(name='fourthscreen')
        fourthscreen.add_widget(self.pageFourth)
        self.pageTurner.add_widget(fourthscreen)

        self.pageEasia1 = KorJpdesare(app=self,fourthpage = self.pageFourth)
        korjpdesscreen = Screen(name = 'korjpdesscreen')
        korjpdesscreen.add_widget(self.pageEasia1)
        self.pageTurner.add_widget(korjpdesscreen)
        
        self.pageTurner.current = 'korjpdesscreen'
        return self.pageTurner
    
    def goingtofirst(self,going):
        self.pageTurner.current = going

    def goingnextpage(self,value):
        self.pageTurner.current = value

class KorJpdesare(BoxLayout)   :
    def __init__(self,app,fourthpage, **kwargs):
        super(KorJpdesare,self).__init__(**kwargs,orientation = 'vertical') 

        self.fourthpage = fourthpage
        self.dessertis = app
        button201 = Button(text = '< Dessert List >',font_size = 22, background_color = '#00ff7f',
                           color = '#F5F5DC', bold = True, halign = 'center', italic = True,size_hint = (1,0.07)) 
        
        self.add_widget(button201)
                           
        vegcheck = BoxLayout(orientation = 'horizontal')
        vegornot = Button(text = 'Wanna Vegetarian? JUST CLICK!',font_size = 18,markup = True, italic = True,size_hint=(0.8,1),background_color = '#F5F5F5')
        vegbutton= ToggleButton(text='VEG',group ='VEG',state = 'normal',size_hint = (0.2,1),font_size = 18,bold = True)
        vegbutton.bind(on_state = self.vegfilter)

        self.vegbutton = vegbutton

        vegcheck.add_widget(vegornot)
        vegcheck.add_widget(self.vegbutton)
        self.add_widget(vegcheck)
        
        button203 = Button(text = 'GOING! CLICK!',font_size = 19, background_color = 'red',\
                        markup = True, color = '#F5F5DC', bold = True, halign = 'center', italic = True,size_hint = (1,0.07)) 
        self.add_widget(button203)
        button203.bind(on_release=lambda instance :self.showInfo(instance))

        self.contentresult = GridLayout(cols = 1, spacing = 10, size_hint_y = None)       
        self.contentresult.bind(minimum_height = self.contentresult.setter('height')) 
        boxcontent202 = ScrollView(do_scroll_y = True, always_overscroll = True)
        boxcontent202.add_widget(self.contentresult)
        
        self.add_widget(boxcontent202)
        bottomlayout = BoxLayout(orientation = 'horizontal')
        button263 = Button(
             font_size = 18, markup = True,text = '[color=#F5F5DC]Go\nBack![/color]',halign='center')
        button263.bind(on_release = lambda instance : self.dessertis.goingnextpage('stwoscreen'))
        bottomlayout.add_widget(button263)
        button273 = Button(
             font_size = 18, bold = True, markup = True,text = '[color=#F5F5DC] Home [/color]',halign='center')
        button273.bind(on_release = lambda instance : self.dessertis.goingtofirst('firstscreen'))

        bottomlayout.add_widget(button273)
        self.add_widget(bottomlayout)

        vegcheck.size_hint = (1,0.09)
        button201.size_hint = (1,0.12)
        button203.size_hint = (1,0.08)
        boxcontent202.size_hint = (1,0.58)
        bottomlayout.size_hint = (1,0.13)

    def vegfilter(self,instance):
        state = instance.state
        state = 'down' if state == 'down' else 'normal'
        
    
    def allergyexclude(self):
        
        return self.fourthpage.allergyIngred
        
    def bringInfo(self,instance) :
        
        conn = sqlite3.connect('foodinfo.db')
        cursor = conn.cursor()
        state = self.vegbutton.state
        allergyExclude = self.allergyexclude()
        excludePlural = ' AND '  .join([f'(Allergy NOT LIKE ?)' for _ in allergyExclude])
        excludeSetting = [f'%{allergy}%' for allergy in allergyExclude]
        # Name TEXT PRIMARY KEY NOT NULL, Allergy TEXT, Type TEXT

        result03 = []
        result030 = []

        if (state == 'down' or state =='normal') : 
            if allergyExclude == [] :
                query030 = (f'SELECT Popularity,Name, Warmth FROM korjan_dessert  ORDER BY Popularity ASC')      
                cursor.execute(query030)
                result030 = cursor.fetchall()

            else :         
                query03 = (f'SELECT Popularity,Name, Warmth FROM korjan_dessert WHERE ({excludePlural}) ORDER BY Popularity ASC')      
                cursor.execute(query03,excludeSetting)
                result03 = cursor.fetchall()
        else : 
            result = ("Error, please retry again!") 
            conn.close()
            return result

        result = cursor.fetchall()
        conn.close()
        outcome = "[b]HERE WE GO![/b]\nSee the [i]recommendation list[/i] by [color=#ed5cb0][u]Popularity[/u][color=#<color>])\n"
        if result03 :
            for i in result03 :
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#fab75f]Warmth[/color][color=#F5F5DC] : {2} \n[/color]" .format(i[0],i[1],i[2])             
        if result030 :
            for i in result030 :
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#fab75f]Warmth[/color][color=#F5F5DC] : {2} \n[/color]" .format(i[0],i[1],i[2])             
        for line in outcome.split('\n'):
            labelbox = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            label = Label(text = line, markup = True,color = '#F5F5DC',bold = True, font_size = '10dp', halign = 'left',valign = 'middle')
            labelbox.add_widget(label)
            self.contentresult.add_widget(labelbox)
     
    def showInfo(self,instance):
        Clock.schedule_once(self.bringInfo,0.1)
        

if __name__ == '__main__':
    KorjpDessert().run()