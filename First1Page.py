from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
from Second2Page10 import SecondPage10
from Second2Page20 import SecondPage20
from Third3Page import ThirdPage
from Fourth4Page import FourthPage
from Sec10Third import SecThird10Page
from Sec20Third import SecThird20Page


class FirstPage(BoxLayout) :
    
    def __init__(self,app,**kwargs):
        super(FirstPage,self).__init__(**kwargs,orientation = 'vertical')
        
        self.firstis = app

        button00 = Button(
                font_size = 32, bold = True, markup = True, background_color = '#FFFF00', \
                text = '[color=#051249]Italy & the UK[/color]' )
            
        self.add_widget(button00)
        button00.bind(on_release = self.button_effect00)
        
        button01 = Button(
            font_size = 32, markup = True,  bold = True, \
            text = '[color=#DDA94B]Korea & Japan[/color]',background_color ='#1E4174' )
        button01.bind(on_release= self.button_effect00)
        self.add_widget(button01)

        self_bottom = BoxLayout(orientation = 'horizontal')

        button03 = Button(font_size = 24, markup = True, italic = True, bold = True,\
                          text = "[color=#1AAFBC]Claim[/color]",background_color = '#80634C' )
        button04 = Button(font_size = 24, markup = True, italic = True, bold = True,\
                          text = "[color=#80634C]Personal\n Setting[/color]", background_color = '#1AAFBC')
        self_bottom.add_widget(button03)  
        self_bottom.add_widget(button04)
        button03.bind(on_release= lambda instance :self.firstis.goingnextpage('thirdscreen'))
        button04.bind(on_release= lambda instance :self.firstis.goingnextpage('fourthscreen'))
        self.add_widget(self_bottom)
        
    def button_effect00(self,instance):
        putText = instance.text
        start = putText.find('[')
        start = putText.find(']',start+1)
        end = putText.find('[',start)
        putText = putText[start+1:end]
        print("Going to the Recommend!\t{0}" .format(putText))
        if putText == "Italy & the UK":
            self.firstis.goingnextpage('secondscreen')
        elif putText == "Korea & Japan":
            self.firstis.goingnextpage('stwoscreen')


class FirstApp(App):

     def build(self):
        self.pageTurner = ScreenManager()

        self.pageFirst = FirstPage(app=self)
        firstscreen = Screen(name = 'firstscreen')
        firstscreen.add_widget(self.pageFirst)
        self.pageTurner.add_widget(firstscreen)

        self.pageSecond10 = SecondPage10(app=self)
        secondscreen = Screen(name = 'secondscreen')
        secondscreen.add_widget(self.pageSecond10)
        self.pageTurner.add_widget(secondscreen)

        self.pageSecond20 = SecondPage20(app=self)
        stwoscreen = Screen(name = 'stwoscreen')
        stwoscreen.add_widget(self.pageSecond20)
        self.pageTurner.add_widget(stwoscreen)

        self.pageThird = ThirdPage(app=self)
        thirdscreen = Screen(name = 'thirdscreen')
        thirdscreen.add_widget(self.pageThird)
        self.pageTurner.add_widget(thirdscreen)

        self.pageFourth = FourthPage(app=self)
        fourthscreen = Screen(name = 'fourthscreen')
        fourthscreen.add_widget(self.pageFourth)
        self.pageTurner.add_widget(fourthscreen)

#---------------------------------------------------------------------------------------
        #from Sec10Third import SecThird10Page / from Sec20Third import SecThird20Page

        self.pageSec10 = SecThird10Page(app=self)
        secondinfoscreen = Screen(name = 'secondinfoscreen')
        secondinfoscreen.add_widget(self.pageSec10)
        self.pageTurner.add_widget(secondinfoscreen)

        self.pageSec20 = SecThird20Page(app=self)
        stwoinfoscreen = Screen(name = 'stwoinfoscreen')
        stwoinfoscreen.add_widget(self.pageSec20)
        self.pageTurner.add_widget(stwoinfoscreen)

        self.pageTurner.current = 'firstscreen'

        return self.pageTurner
     
     def goingnextpage(self,value):
        self.pageTurner.current = value


if __name__ == '__main__':
    FirstApp().run()