from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
import sqlite3
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.label import Label
from kivy.clock import Clock
from Fourth4Page import FourthPage

class KorjpSide(App):
    def build(self) : 

        self.pageTurner = ScreenManager()
        self.pageFourth = FourthPage(app=self)
        fourthscreen = Screen(name='fourthscreen')
        fourthscreen.add_widget(self.pageFourth)
        self.pageTurner.add_widget(fourthscreen)

        self.pageEasia2 = KorJpssare(app=self, fourthpage = self.pageFourth)
        korjpsscreen = Screen(name = 'korjpsscreen')
        korjpsscreen.add_widget(self.pageEasia2)
        self.pageTurner.add_widget(korjpsscreen)

        self.pageTurner.current = 'korjpsscreen'
        return self.pageTurner
    
    def goingtofirst(self,going):
        self.pageTurner.current = going

    def goingnextpage(self,value):
        self.pageTurner.current = value

class KorJpssare(BoxLayout)   :
    def __init__(self,app,fourthpage, **kwargs):
        super(KorJpssare,self).__init__(**kwargs,orientation = 'vertical') 
        
        self.fourthpage = fourthpage
        self.sideis = app
        self.pageFourth = FourthPage(app = self.sideis)
        
        button201 = Button(text = '< Side Dish List >',font_size = 22, background_color = '#00ff7f',
                           color = '#F5F5DC', bold = True, halign = 'center', italic = True,size_hint = (1,0.07)) 
        
        self.add_widget(button201)
        
        content202 = Label(color = '#F5F5DC',bold = True, font_size = '10dp',markup = True)
        self.content202 = content202
        self.contentresult = GridLayout(cols = 1, spacing = 10, size_hint_y = None)       
        self.contentresult.bind(minimum_height = self.contentresult.setter('height'))      
        self.contentresult.add_widget(self.content202)
        vegcheck = BoxLayout(orientation = 'horizontal')
        vegornot = Button(text = 'Wanna Vegetarian? Just [b]CHECK![/b]', font_size = 18,markup = True, italic = True,size_hint=(0.8,1),background_color = '#F5F5F5')
        vegbutton= ToggleButton(text='VEG',group ='VEG',state = 'normal',size_hint = (0.2,1),font_size = 18,bold = True)
        vegbutton.bind(on_state = self.vegfilter)

        self.vegbutton = vegbutton

        vegcheck.add_widget(vegornot)
        vegcheck.add_widget(self.vegbutton)
        self.add_widget(vegcheck)
        
        button203 = Button(text = 'GOING! CLICK!',font_size = 19, background_color = 'red',\
                        markup = True, color = '#F5F5DC', bold = True, halign = 'center', italic = True,size_hint = (1,0.07)) 
        self.add_widget(button203)
        button203.bind(on_release=lambda instance :self.showInfo())

        
        boxcontent202 = ScrollView(do_scroll_y = True, always_overscroll = True)
        
        boxcontent202.add_widget(self.contentresult)
        self.add_widget(boxcontent202)
        bottomlayout = BoxLayout(orientation = 'horizontal')
        button26 = Button(
             font_size = 18, markup = True,text = '[color=#F5F5DC]Go\nBack![/color]',halign='center')
        button26.bind(on_release = lambda instance : self.sideis.goingnextpage('stwoscreen'))
        bottomlayout.add_widget(button26)
        button27 = Button(
             font_size = 18, bold = True, markup = True,text = '[color=#F5F5DC] Home [/color]',halign='center')
        button27.bind(on_release = lambda instance : self.sideis.goingtofirst('firstscreen'))

        bottomlayout.add_widget(button27)
        self.add_widget(bottomlayout)

        vegcheck.size_hint = (1,0.09)
        button201.size_hint = (1,0.12)
        button203.size_hint = (1,0.08)
        boxcontent202.size_hint = (1,0.58)
        bottomlayout.size_hint = (1,0.13)

    def vegfilter(self,instance):
        state = instance.state
        
        if state == 'down' : state = 'down'
        else : state = 'normal'
        
    
    def allergyexclude(self):
        return self.fourthpage.allergyIngred
        
    def bringInfo(self,instance) :
        
        conn = sqlite3.connect('foodinfo.db')
        cursor = conn.cursor()
        state = self.vegbutton.state
        allergyExclude = self.allergyexclude()
        excludePlural = ' AND '  .join([f'(Allergy NOT LIKE ?)' for _ in allergyExclude])
        excludeSetting = [f'%{allergy}%' for allergy in allergyExclude]
        self.contentresult.clear_widgets()
        # Name TEXT PRIMARY KEY NOT NULL, Allergy TEXT, Warmth TEXT

        result120 = []
        result121 = []
        result122 = []
        result123 = []
        result124 = []
        result125 = []
        result126 = []
        result127 = []

        if state == 'down' : #veg is
            if allergyExclude == [] :
                #query120 : FOR veg & Non-spicy & No allergy_dislike
                query120 = (f'SELECT Popularity,Name, Warmth FROM korjan_sidedish WHERE Veg = 1 AND Spicy = 0 ORDER BY Popularity ASC')      
                cursor.execute(query120)
                result120 = cursor.fetchall()
                #query121 : FOR veg & Yes Spicy & No allergy_dislike
                query121 = (f'SELECT Popularity,Name, Warmth FROM korjan_sidedish WHERE Veg = 1 AND Spicy = 1 ORDER BY Popularity ASC')
                cursor.execute(query121)
                result121 = cursor.fetchall()

            else :   
                #query122 : FOR veg & Non-spicy & exist.allergy_dislike       
                query122 = (f'SELECT Popularity,Name, Warmth FROM korjan_sidedish WHERE Veg = 1 AND Spicy = 0 AND ({excludePlural}) ORDER BY Popularity ASC')      
                cursor.execute(query122,excludeSetting)
                result122 = cursor.fetchall()
                #query123 : FOR veg & Yes spicy & exist.allergy_dislike       
                query123 = (f'SELECT Popularity,Name, Warmth FROM korjan_sidedish WHERE Veg = 1 AND Spicy = 1 AND ({excludePlural}) ORDER BY Popularity ASC')      
                cursor.execute(query123,excludeSetting)
                result123 = cursor.fetchall()

        elif state == 'normal' : #not veg        
            if allergyExclude == [] :
                #query124 : Not veg & Non-spicy & No allergy_dislike
                query124 = (f'SELECT Popularity,Name, Warmth FROM korjan_sidedish WHERE  Spicy = 0 ORDER BY Popularity ASC')      
                cursor.execute(query124)
                result124 = cursor.fetchall()
                #query125 : Not veg & Yes Spicy & No allergy_dislike
                query125 = (f'SELECT Popularity,Name, Warmth FROM korjan_sidedish WHERE  Spicy = 1 ORDER BY Popularity ASC')
                cursor.execute(query125)
                result125 = cursor.fetchall()

            else :   
                #query126 : Not veg & Non-spicy & exist.allergy_dislike       
                query126 = (f'SELECT Popularity,Name, Warmth FROM korjan_sidedish WHERE Spicy = 0 AND ({excludePlural}) ORDER BY Popularity ASC')      
                cursor.execute(query126,excludeSetting)
                result126 = cursor.fetchall()
                #query127 : Not veg & Yes spicy & exist.allergy_dislike       
                query127 = (f'SELECT Popularity,Name, Warmth FROM korjan_sidedish WHERE Spicy = 1 AND ({excludePlural}) ORDER BY Popularity ASC')      
                cursor.execute(query127,excludeSetting)
                result127 = cursor.fetchall()
        else : 
            result = ("Error, please retry again!") 
            result = cursor.fetchall()
            conn.close()
            return result
         
        conn.close() 
        outcome = "[b]HERE WE GO![/b]\nSee the [i]recommendation list[/i] by [color=#ed5cb0][u]Popularity[/u][/color>])\n"
        if result120 :
            outcome += "[color=#3983e3][b]Nah! SPICY! >>>>>  [/b][/color]\n"
            for i in result120 :
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#fab75f]Warmth[/color][color=#F5F5DC] : {2} \n[/color]" .format(i[0],i[1],i[2])             
        if result121 :
            outcome += "[color=#ed5cb0][b]Yes SPICY!! >>>>>  [/b][/color]\n"
            for i in result121 :
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#fab75f]Warmth[/color][color=#F5F5DC] : {2} \n[/color]" .format(i[0],i[1],i[2])
        if result122 :
            outcome += "[color=#3983e3][b]Nah! SPICY! >>>>>  [/b][/color]\n"
            for i in result122 :
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#fab75f]Warmth[/color][color=#F5F5DC] : {2} \n[/color]" .format(i[0],i[1],i[2])             
        if result123 :
            outcome += "[color=#ed5cb0][b]Yes SPICY!! >>>>>  [/b][/color]\n"
            for i in result123 :
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#fab75f]Warmth[/color][color=#F5F5DC] : {2} \n[/color]" .format(i[0],i[1],i[2])
        if result124 :
            outcome += "[color=#3983e3][b]Nah! SPICY! >>>>>  [/b][/color]\n"
            for i in result124 :
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#fab75f]Warmth[/color][color=#F5F5DC] : {2} \n[/color]" .format(i[0],i[1],i[2])             
        if result125 :
            outcome += "[color=#ed5cb0][b]Yes SPICY!! >>>>>  [/b][/color]\n"
            for i in result125 :
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#fab75f]Warmth[/color][color=#F5F5DC] : {2} \n[/color]" .format(i[0],i[1],i[2])
        if result126 :
            outcome += "[color=#3983e3][b]Nah! SPICY! >>>>>  [/b][/color]\n"
            for i in result126 :
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#fab75f]Warmth[/color][color=#F5F5DC] : {2} \n[/color]" .format(i[0],i[1],i[2])             
        if result127 :
            outcome += "[color=#ed5cb0][b]Yes SPICY!! >>>>>  [/b][/color]\n"
            for i in result127 :
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#fab75f]Warmth[/color][color=#F5F5DC] : {2} \n[/color]" .format(i[0],i[1],i[2])                                                                            
        
        for line in outcome.split('\n'):
            labelbox = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            label = Label(text = line, markup = True,color = '#F5F5DC',bold = True, font_size = '10dp', halign = 'auto',valign = 'center')
            labelbox.add_widget(label)
            self.contentresult.add_widget(labelbox)
     
    def showInfo(self):
        Clock.schedule_once(self.bringInfo,0.1)
        

if __name__ == '__main__':
    KorjpSide().run()