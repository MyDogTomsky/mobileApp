from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
import sqlite3
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.label import Label
from kivy.clock import Clock
from Fourth4Page import FourthPage

class WestFood(App):
    def build(self) : 

        self.pageTurner = ScreenManager()
        self.pageFourth = FourthPage(app=self)
        fourthscreen = Screen(name = 'fourthscreen')
        fourthscreen.add_widget(self.pageFourth)
        self.pageTurner.add_widget(fourthscreen)

        self.pageWest1 = Weststartersare(app=self, fourthpage = self.pageFourth)
        weststarterscreen = Screen(name = 'weststarterscreen')
        weststarterscreen.add_widget(self.pageWest1)
        self.pageTurner.add_widget(weststarterscreen)

        self.pageTurner.current = 'weststarterscreen'

        return self.pageTurner
    
    def goingtofirst(self,going):
        self.pageTurner.current = going

    def goingnextpage(self,value):
        self.pageTurner.current = value

class Weststartersare(BoxLayout)   :
    def __init__(self,app,fourthpage, **kwargs):
        super(Weststartersare,self).__init__(**kwargs,orientation = 'vertical') 

        self.starteris = app
        self.fourthpage = fourthpage
        button201 = Button(text = '< Starter List >',font_size = 22, background_color = '#00ff7f',
                           color = '#F5F5DC', bold = True, halign = 'center', italic = True,size_hint = (1,0.07)) 
        
        self.add_widget(button201)
        vegcheck = BoxLayout(orientation = 'horizontal')
        vegornot = Button(text = 'Wanna Vegetarian? Just [b]CHECK![/b]',markup = True,font_size = 18, italic = True,size_hint=(0.8,1),background_color = '#F5F5F5')
        vegbutton= ToggleButton(text='VEG',group ='VEG',state = 'normal',size_hint = (0.2,1),font_size = 18,bold = True)
        vegbutton.bind(on_state = self.vegfilter)

        self.vegbutton = vegbutton

        vegcheck.add_widget(vegornot)
        vegcheck.add_widget(self.vegbutton)
        self.add_widget(vegcheck)
        
        button203 = Button(text = 'GOING! CLICK!',font_size = 19, background_color = 'red',\
                        color = '#F5F5DC', bold = True, halign = 'center', italic = True,size_hint = (1,0.07)) 
        self.add_widget(button203)
        button203.bind(on_release=lambda instance :self.showInfo(instance))

        self.contentresult = GridLayout(cols = 1, spacing = 10, size_hint_y = None)       
        self.contentresult.bind(minimum_height = self.contentresult.setter('height'))            
        boxcontent202 = ScrollView(do_scroll_y = True, always_overscroll = True)
        boxcontent202.add_widget(self.contentresult)
        
        self.add_widget(boxcontent202)
        bottomlayout = BoxLayout(orientation = 'horizontal')
        button26 = Button(
             font_size = 18, markup = True,text = '[color=#F5F5DC]Go\nBack![/color]',halign='center')
        button26.bind(on_release = lambda instance : self.starteris.goingnextpage('secondscreen'))
        bottomlayout.add_widget(button26)
        button27 = Button(
             font_size = 18, bold = True, markup = True,text = '[color=#F5F5DC] Home [/color]',halign='center')
        button27.bind(on_release = lambda instance : self.starteris.goingtofirst('firstscreen'))
        bottomlayout.add_widget(button27)
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
        excludeNum = ', ' .join('?'*len(allergyExclude))
        if state == 'down'  : 
            query1 = (f'SELECT Popularity,Name, Warmth FROM west_starter WHERE Veg == 1 AND (Allergy NOT IN ({excludeNum}) OR Allergy IS NULL) ORDER BY Popularity ASC')      
            cursor.execute(query1, allergyExclude)

        elif state == 'normal' :
            query2 = (f'SELECT Popularity,Name, Warmth,ProteinName FROM west_starter WHERE (Allergy NOT IN ({excludeNum}) OR Allergy IS NULL) ORDER BY Popularity ASC')        
            cursor.execute(query2,allergyExclude)

        else : 
            result = ("Error, please retry again!") 
            conn.close()
            return result

        result = cursor.fetchall()
        conn.close()
        outcome = "[b]HERE WE GO![/b]\nSee the [i]recommendation list[/i] by [color=#ed5cb0][u]Popularity[/u][color=#<color>])\n"
        for i in result :
            outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#fab75f]Warmth[/color][color=#F5F5DC] : {2} \n[/color]" .format(i[0],i[1],i[2])             
        
        for line in outcome.split('\n'):
            labelbox = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            label = Label(text = line, markup = True,color = '#F5F5DC',bold = True, font_size = '10dp', halign = 'left',valign = 'middle')
            labelbox.add_widget(label)
            self.contentresult.add_widget(labelbox)
        
     
    def showInfo(self,instance):
        Clock.schedule_once(self.bringInfo,0.1)
        

if __name__ == '__main__':
    WestFood().run()