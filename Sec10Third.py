from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.button import Button

class Helper213(App):
    def build(self):

        self.pageTurner = ScreenManager()

        self.pageSec10 = SecThird10Page(app=self)
        secondinfoscreen = Screen(name = 'secondinfoscreen')
        secondinfoscreen.add_widget(self.pageSec10)
        self.pageTurner.add_widget(secondinfoscreen)

        return self.pageTurner
    
    def goingtofirst(self,going):
        self.pageTurner.current = going

    def goingnextpage(self,value):
        self.pageTurner.current = value

class SecThird10Page(BoxLayout):
    def __init__(self,app,**kwargs):
        super(SecThird10Page,self).__init__(**kwargs,orientation = 'vertical')
     
        self.infow = app 
        imageseeing = ScrollView(do_scroll_y = True, always_overscroll = True)
        imagegrid = GridLayout(cols = 1, spacing = 10, size_hint_y = None)
        imagegrid.bind(minimum_height = imagegrid.setter('height'))
        euinform = ['images\info211.jpg','images\info212.jpg','images\info213.jpg']
        for one in euinform :
            one = Image(source = one,size_hint_y = None,keep_ratio = True, size = Window.size)
            imagegrid.add_widget(one)

        imageseeing.add_widget(imagegrid)  
        self.add_widget(imageseeing)
        
        bottomlayout1 = BoxLayout(orientation = 'horizontal')
        button26 = Button(font_size = 19, markup = True,text = '[color=#F5F5DC]Go\nBack![/color]',halign='center')
        button26.bind(on_release = lambda instance : self.infow.goingnextpage('secondscreen'))
        bottomlayout1.add_widget(button26)
        button27 = Button(font_size = 19, bold = True, markup = True,text = '[color=#F5F5DC] Home [/color]',halign='center')
        button27.bind(on_release = lambda instance : self.infow.goingtofirst('firstscreen'))
        bottomlayout1.add_widget(button27)
        self.add_widget(bottomlayout1)
        bottomlayout1.size_hint = (1,0.13)
        imageseeing.size_hint = (1,0.87)

        
if __name__ == '__main__':
    Helper213().run()     