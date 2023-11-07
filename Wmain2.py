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

class WestFood(App):
    def build(self) : 

        self.pageTurner = ScreenManager()
        self.pageFourth = FourthPage(app=self)
        fourthscreen = Screen(name='fourthscreen')
        fourthscreen.add_widget(self.pageFourth)
        self.pageTurner.add_widget(fourthscreen)

        self.pageWest2 = Westmainsare(app=self, fourthpage = self.pageFourth)
        westmainscreen = Screen(name = 'westmainscreen')
        westmainscreen.add_widget(self.pageWest2)
        self.pageTurner.add_widget(westmainscreen)

        self.pageTurner.current = 'westmainscreen'
        return self.pageTurner
    
    def goingtofirst(self,going):
        self.pageTurner.current = going

    def goingnextpage(self,value):
        self.pageTurner.current = value

class Westmainsare(BoxLayout)   :
    def __init__(self,app,fourthpage, **kwargs):
        super(Westmainsare,self).__init__(**kwargs,orientation = 'vertical') 
        self.fourthpage = fourthpage
        self.mainis = app
        self.pageFourth = FourthPage(app = self.mainis)
        
        button201 = Button(text = '< Main List >',font_size = 22, background_color = '#00ff7f',
                           color = '#F5F5DC', bold = True, halign = 'center', italic = True,size_hint = (1,0.07)) 
        
        self.add_widget(button201)
        
        self.contentresult = GridLayout(cols = 1, spacing = 10, size_hint_y = None)       
        self.contentresult.bind(minimum_height = self.contentresult.setter('height'))            
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
        button26.bind(on_release = lambda instance : self.mainis.goingnextpage('secondscreen'))
        bottomlayout.add_widget(button26)
        button27 = Button(
             font_size = 18, bold = True, markup = True,text = '[color=#F5F5DC] Home [/color]',halign='center')
        button27.bind(on_release = lambda instance : self.mainis.goingtofirst('firstscreen'))

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
        print(allergyExclude) 
        #test checking the allergy list out
        self.contentresult.clear_widgets()

        excludePlural = " AND " .join([f'(Allergy NOT LIKE ?)' for _ in allergyExclude])
        excludeSetting = [f'%{allergy}%' for allergy in allergyExclude]

        #(Name,Veg,MeatSeafood,Pasta,Allergy,Popularity,ProteinName)
        result1 = []
        result10 = []
        result2 = []
        result20 = []
        result3 = []
        result30 = []
        result4 = []
        result40 = []


        if state == 'down' : #veg is
            if allergyExclude == [] :
                query10 = (f'SELECT Popularity, Name FROM west_main WHERE Veg = 1 ORDER BY Popularity ASC')
                cursor.execute(query10)
                result10 = cursor.fetchall()
            else : 
                query1 = (f'SELECT Popularity, Name FROM west_main WHERE Veg = 1 AND (Allergy IS NULL OR {excludePlural}) ORDER BY Popularity ASC')
                cursor.execute(query1,excludeSetting)
                result1 = cursor.fetchall()

        elif state == 'normal' :

            if allergyExclude == []: 
                query20 = (f'SELECT Popularity, Name, ProteinName FROM west_main WHERE  PASTA = 1 ORDER BY Popularity ASC') 
                cursor.execute(query20)
                result20 = cursor.fetchall()
        
                query30 = (f'SELECT Popularity, Name, ProteinName FROM west_main WHERE  PASTA = 0 AND MeatSeafood = "Meat" ORDER BY Popularity ASC') 
                cursor.execute(query30)
                result30 = cursor.fetchall()

                query40 = (f'SELECT Popularity, Name, ProteinName FROM west_main WHERE  PASTA = 0 AND MeatSeafood = "Seafood"  ORDER BY Popularity ASC') 
                cursor.execute(query40)
                result40 = cursor.fetchall()

            else:
                query2 = (f'SELECT Popularity, Name, ProteinName FROM west_main WHERE (Allergy IS NULL OR {excludePlural}) AND PASTA = 1 ORDER BY Popularity ASC') 
                cursor.execute(query2, excludeSetting)
                result2 = cursor.fetchall()
        
                query3 = (f'SELECT Popularity, Name, ProteinName FROM west_main WHERE (Allergy IS NULL OR {excludePlural}) AND PASTA = 0 AND MeatSeafood = "Meat" ORDER BY Popularity ASC') 
                cursor.execute(query3, excludeSetting)
                result3 = cursor.fetchall()

                query4 = (f'SELECT Popularity, Name, ProteinName FROM west_main WHERE (Allergy IS NULL OR {excludePlural}) AND PASTA = 0 AND MeatSeafood = "Seafood"  ORDER BY Popularity ASC') 
                cursor.execute(query4,excludeSetting)
                result4 = cursor.fetchall()
        else : 
            result = ("Error, please retry again!") 
            result = cursor.fetchall()
            conn.close()
            
            return result
        
        conn.close()
        outcome = "[b]HERE WE GO![/b]\nSee the [i]recommendation list[/i] by [color=#ed5cb0][u]Popularity[/u][color=#<color>])\n"
        if result1:
            for i in result1 :
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1}[/color]\n" .format(i[0],i[1])
        if result10:
            for i in result10 :
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1}[/color]\n" .format(i[0],i[1])                     
        if result2:
            outcome += "[color=#ed5cb0][b]Pasta >[/b][color=#<color>]\n"
            for j in result2 :
              outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#3983e3]Protein?[/color][color=#F5F5DC] : {2}\n[/color]" .format(j[0],j[1],j[2])             
        if result3:
            outcome += "[color=#ed5cb0][b]Meat >[/b][color=#<color>] \n"
            for k in result3 : 
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#3983e3]Protein?[/color][color=#F5F5DC] : {2}\n[/color]" .format(k[0],k[1],k[2])             
        if result4:
            outcome += "[color=#ed5cb0][b]Seafood >[/b][color=#<color>]\n"
            for l in result4 :
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#3983e3]Protein?[/color][color=#F5F5DC] : {2}\n [/color]" .format(l[0],l[1],l[2])             
        if result20:
            outcome += "[color=#ed5cb0][b]Pasta >[/b][color=#<color>]\n"
            for j in result20 :
              outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#3983e3]Protein?[/color][color=#F5F5DC] : {2}\n[/color]" .format(j[0],j[1],j[2])             
        if result30:
            outcome += "[color=#ed5cb0][b]Meat >[/b][color=#<color>] \n"
            for k in result30 : 
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#3983e3]Protein?[/color][color=#F5F5DC] : {2}\n[/color]" .format(k[0],k[1],k[2])             
        if result40:
            outcome += "[color=#ed5cb0][b]Seafood >[/b][color=#<color>]\n"
            for l in result40 :
                outcome +="[color=#F5F5DC]{0})[/color] [color=#33ab64]Name[/color][color=#F5F5DC] : {1},[/color] [color=#3983e3]Protein?[/color][color=#F5F5DC] : {2}\n [/color]" .format(l[0],l[1],l[2])             


        for line in outcome.split('\n'):
            labelbox = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            label = Label(text = line, markup = True,color = '#F5F5DC',bold = True, font_size = '10dp', halign = 'left',valign = 'middle')
            labelbox.add_widget(label)
            self.contentresult.add_widget(labelbox)
        
     
    def showInfo(self):
        Clock.schedule_once(self.bringInfo,0.1)
        

if __name__ == '__main__':
    WestFood().run()