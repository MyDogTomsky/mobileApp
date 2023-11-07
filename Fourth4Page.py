from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen,ScreenManager

class PersonalSET(App):
    def build(self):
     self.pageTurner = ScreenManager()

     self.pageFourth = FourthPage(app=self)
     fourthscreen = Screen(name = 'fourthscreen')
     fourthscreen.add_widget(self.pageFourth)
     self.pageTurner.add_widget(fourthscreen)
    
     return self.pageTurner

class FourthPage(BoxLayout):
    def __init__(self,app, **kwargs):
            super(FourthPage,self).__init__(**kwargs,orientation = 'vertical')
            self.fourthis = app
            self.allergyIngred = list() 

            explain = Button(font_size = 20,markup = True, background_color = '#bcff37',bold = True,\
                     text = '[color=#F5F5DC]Hey!\n What to EXCLUDE! [/color]',halign = 'center')
            self.add_widget(explain)
            
            ingredientAll = {
                 'Veg,\n' : ['nuts','wheat','mushroom'],
                 'Dairy & Etc,\n' : ['milk','egg','cheese','caffeine'],
                 'Sea,\n' : ['shellfish','seafood','Fish'],
                 'Meat,\n' : ['Beef','Pork','Lamb','Venison','Duck','Chicken']}
            
            for groupIndex, ingredients in ingredientAll.items() : 
                sorting = Label(text = groupIndex, font_size = 17,size_hint_x=None, halign = 'left')
                self.add_widget(sorting)
                layoutset = BoxLayout(orientation = 'horizontal')
                
                for ingredient in ingredients : 
                    layoutin = BoxLayout(orientation = 'vertical')
                    checkbox1 = CheckBox(active = False)
                    checkboxlabel = Label(text = ingredient, font_size = 17,color = '#2382A1', valign = 'middle',bold = True, halign = 'center')
                    
                    layoutin.add_widget(checkbox1)
                    layoutin.add_widget(checkboxlabel)
                    
                    checkbox1.bind(active=self.checkMarking)
                    # checkbox no need about 'on_release' which is the button's functionality!
                    layoutset.add_widget(layoutin)
       
                self.add_widget(layoutset)
            referex = Label(font_size = 14,markup = True,text = 'Allergy OR Dislike',italic = True)
            self.add_widget(referex)
            bottomlayout = BoxLayout(orientation = 'horizontal')
            button26 = Button(font_size = 21,text = 'Home',halign='center')
            saveSet = Button(text = 'Save', bold = True, font_size = 21, on_press = self.goingSubmit)
            button26.bind(on_release = self.goingtofirst)
            bottomlayout.add_widget(button26)
            bottomlayout.add_widget(saveSet)
            self.add_widget(bottomlayout)
            
    def checkMarking(self,instance,state):
        ingredHelper = (instance.parent).children[0].text.strip()
        if  instance.active == True :
            self.allergyIngred.append(ingredHelper)
        else :
            self.allergyIngred.remove(ingredHelper)
        
        return self.allergyIngred

    def goingSubmit(self, instance):
        #=========== ☆★☆★ Developer Checking , whether the saving functionality is worked or not)  ☆★☆★
        if self.allergyIngred == []:
             print("Everything is OKAY for me!")
        else: print("allergy : ","," .join(self.allergyIngred))

    def goingtofirst(self,instance):
        self.fourthis.goingnextpage('firstscreen')

if __name__ == '__main__' : 
    PersonalSET().run()