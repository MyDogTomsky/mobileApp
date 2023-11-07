from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.button import Button

class Helper223(App):
    def build(self):

        self.pageTurner = ScreenManager()

        self.pageSec20 = SecThird20Page(app=self)
        stwoinfoscreen = Screen(name = 'stwoinfoscreen')
        stwoinfoscreen.add_widget(self.pageSec20)
        self.pageTurner.add_widget(stwoinfoscreen)

        return self.pageTurner
    def goingtofirst(self,going):
        self.pageTurner.current = 'firstscreen'

    def goingnextpage(self,value):
        self.pageTurner.current = value
    
    

class SecThird20Page(BoxLayout):
    def __init__(self,app,**kwargs):
        super(SecThird20Page,self).__init__(**kwargs,orientation = 'vertical')

        self.app = app 
        imageseeing = ScrollView(do_scroll_y = True, always_overscroll = True)
        imagegrid = GridLayout(cols = 1, spacing = 10, size_hint_y = None)
        imagegrid.bind(minimum_height = imagegrid.setter('height'))
        
        euinform = ['images\info221.jpg','images\info222.jpg']
        for one in euinform :
            one = Image(source = one,size_hint_y = None,keep_ratio = True, size = Window.size)
            imagegrid.add_widget(one)

        imageseeing.add_widget(imagegrid)  
        self.add_widget(imageseeing)
        
        bottomlayout2 = BoxLayout(orientation = 'horizontal')
        button28 = Button(
             font_size = 19, markup = True,text = '[color=#F5F5DC]Go\nBack![/color]',halign='center')
        button28.bind(on_release = lambda instance : self.app.goingnextpage('stwoscreen'))

        bottomlayout2.add_widget(button28)
        button29 = Button(
             font_size = 19, bold = True, markup = True,text = '[color=#F5F5DC] Home [/color]',halign='center')
        button29.bind(on_release = lambda instance : self.app.goingtofirst('firstscreen'))
        
        bottomlayout2.add_widget(button29)
        self.add_widget(bottomlayout2)

        bottomlayout2.size_hint = (1,0.13)
        imageseeing.size_hint = (1,0.87)
        
        
if __name__ == '__main__':
    Helper223().run()     