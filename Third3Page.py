from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager,Screen
from email.mime.text import MIMEText
import smtplib


class Claim(App):
    def build(self):
        self.pageTurner = ScreenManager()

        self.pageThird = ThirdPage(app=self)
        thirdscreen = Screen(name = 'thirdscreen')
        thirdscreen.add_widget(self.pageThird)
        self.pageTurner.add_widget(thirdscreen)

        return self.pageTurner

class ThirdPage(BoxLayout):
    def __init__(self,app,**kwargs):
        super(ThirdPage,self).__init__(**kwargs,orientation = 'vertical')

        self.app = app        
        opinion = Label(text = 'Leave your comments here.',font_size = 22, \
                        markup = True, color = '#0072B5', bold = True, halign = 'center',italic = True)
        opinioncause = Label(text = '(The feedback will greatly assist in improving our APP!)',font_size = 15, \
                        markup = True, color = '#0072B5', halign = 'center')
        self.add_widget(opinion)
        self.add_widget(opinioncause)
        
        inputComment = TextInput()
        self.add_widget(inputComment)

        bottomlayout = BoxLayout(orientation = 'horizontal')

        goback = Button(text = 'Go Back', bold = True, markup = True,\
                              font_size = 23, halign = 'center')
        commentEnter = Button(text = 'Bring To Us!', bold = True, markup = True,\
                              font_size = 23, halign = 'center')
        goback.bind(on_release = self.goingtofirst)
        commentEnter.bind(on_release = lambda wtcomment : self.send_mail(inputComment))

        bottomlayout.add_widget(goback)
        bottomlayout.add_widget(commentEnter)
        self.add_widget(bottomlayout)

        future = Label(text = 'Have you enjoyed your meal?\nThanks for using our RECOMMENDATION:)', font_size = 17, color = 'pink',markup = True)
        self.add_widget(future)
        opinion.size_hint = (1,0.13)
        opinioncause.size_hint = (1,0.07)
        inputComment.size_hint = (1,0.60)
        bottomlayout.size_hint = (1,0.1)
        future.size_hint = (1,0.1)
        
    def alert_popup(self):
        showpopup = Popup(title = 'Thanks for YOUR COMMENTS!', content=Label(text='[b]Delivered TO US![/b]',markup = True, ), size_hint=(None,None), \
                                size = (250,200),title_size = 13,title_align = 'center',\
                                separator_color = [255/255., 182/255., 193/255.,1],auto_dismiss=True)
        showpopup.open()

    def goingtofirst(self,instance):
        self.app.goingnextpage('firstscreen')

    def send_mail(self,instance):
        
        input = instance.text
        senderEmail = 'mengu2231@gmail.com' 
        receiverEmail = "2788203K@student.gla.ac.uk"
        senderpw =  'ywliqeaprjxdsgzz'

        
        whatfor = 'The User Feedback_: '
        
        feedback= MIMEText(whatfor+input)
        server = smtplib.SMTP('smtp.gmail.com',587)

        server.ehlo()
        server.starttls()
        print("stage 1: encryption completed")
        server.login(senderEmail,senderpw)
        print("stage 2: login completed")
      
        server.sendmail(senderEmail,receiverEmail,feedback.as_string())
        print("stage 3: Your Comment is delivered!")  
        server.quit()

        self.alert_popup()
        
          

if __name__ == '__main__':
    Claim().run()