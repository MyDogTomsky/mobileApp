from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from First1Page import FirstPage
from Second2Page10 import SecondPage10
from Second2Page20 import SecondPage20
from Third3Page import ThirdPage
from Fourth4Page import FourthPage
from Sec10Third import SecThird10Page
from Sec20Third import SecThird20Page
from kivy.clock import Clock
from Wstarter1 import Weststartersare
from Wmain2 import Westmainsare
from Wdessert3 import Westdessertsare
from KJdessert3 import KorJpdesare
from KJside2 import KorJpssare
from KJmain0 import KorJpma0are
from KJmain1 import KorJpma1are
# ZeroPage is sort of Loading Page to draw attention.
from kivy.uix.screenmanager import ScreenManager, Screen

class ZeroLoading(App):
    def build(self):
        self.title = 'FOOD MAKERS'  
        # title --> App Name, Moving Page Functionality --> ScreenManger & Pages Setting Respectively!
        self.pageTurner = ScreenManager()

        self.pageZero = ZeroPage()
        zeroscreen = Screen(name = 'zeroscreen')
        zeroscreen.add_widget(self.pageZero)
        self.pageTurner.add_widget(zeroscreen)

        self.pageFirst = FirstPage(app = self)
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

        self.pageSec10 = SecThird10Page(app=self)
        secondinfoscreen = Screen(name = 'secondinfoscreen')
        secondinfoscreen.add_widget(self.pageSec10)
        self.pageTurner.add_widget(secondinfoscreen)

        self.pageSec20 = SecThird20Page(app=self)
        stwoinfoscreen = Screen(name = 'stwoinfoscreen')
        stwoinfoscreen.add_widget(self.pageSec20)
        self.pageTurner.add_widget(stwoinfoscreen)

#------------------------------------------------------------------ Data Filtering Page ------
        self.pageWest1 = Weststartersare(app=self, fourthpage = self.pageFourth)
        weststarterscreen = Screen(name = 'weststarterscreen')
        weststarterscreen.add_widget(self.pageWest1)
        self.pageTurner.add_widget(weststarterscreen)

        self.pageWest2 = Westmainsare(app=self, fourthpage = self.pageFourth)
        westmainscreen = Screen(name = 'westmainscreen')
        westmainscreen.add_widget(self.pageWest2)
        self.pageTurner.add_widget(westmainscreen)

        self.pageWest3 = Westdessertsare(app=self, fourthpage = self.pageFourth)
        westdessertscreen = Screen(name = 'westdessertscreen')
        westdessertscreen.add_widget(self.pageWest3)
        self.pageTurner.add_widget(westdessertscreen)

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

        self.pageTurner.current = 'zeroscreen'
        Clock.schedule_once(self.goingtofirst,7)
         
        return self.pageTurner
    
    def goingtofirst(self,dt):
        self.pageTurner.current = 'firstscreen'

    def goingnextpage(self,value):
        self.pageTurner.current = value
        

class ZeroPage(GridLayout):
    def __init__(self,**kwargs):
        super(ZeroPage,self).__init__(**kwargs)
    
        self.rows = 3
        loadfirst = Label(text = 'Personal',markup = True, italic = True, bold = True, color = '#0072B5',font_size = 40, halign = 'left')
        loadsecond = Label(text = 'MEAL',markup = True, italic = True, bold = True, color = '#0072B5',font_size = 40,halign = 'right' )
        loadthird = Label(text = 'HERE YOU GO !', italic = True, markup = True, bold = True, color = '#92ff60',font_size = 35, halign = 'center')

        self.add_widget(loadfirst)
        self.add_widget(loadsecond)
        self.add_widget(loadthird)

if __name__ == '__main__':
    appstart = ZeroLoading()
    appstart.run()