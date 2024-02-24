########## Imports ###########################
from kivy.config import Config
from kivy.lang import Builder
Config.set('graphics', 'width', 350)
Config.set('graphics', 'height', 600)
from kivy.logger import Logger
Logger.disabled = True
from Calc_widget import *
from Preview import *
from kivy.uix.screenmanager import ScreenManager

########## KIVY Imports ###########################
from kivy.app import App

class manage(ScreenManager):
    def switch_screen(self):
        if self.current=='wid':
            self.current='val_s'
        elif self.current=='val_s':
            self.current='wid'
    
class CalcApp(App):
    def build(self):
        sm= manage()
        sm.add_widget(CalcGame(name='wid'))
        sm.add_widget(Preview(name='val_s'))
        #Clock.schedule_interval(game.update, 1.0 / 20.0)
        return sm

if __name__ == '__main__':
    CalcApp().run()
