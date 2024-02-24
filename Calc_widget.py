from kivy.core.clipboard import Clipboard
import numpy as np
import PIL
from kivy.core.clipboard import Clipboard
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Canvas, Color, Rectangle
from kivy.properties import NumericProperty, ObjectProperty,ReferenceListProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.uix.screenmanager import Screen


class CalcGame(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    suit_val_n=0
    factor_n=0
    cFee_n=0   
    def updateval(self):
        try:
            self.suit_val_n = float(self.suit_val.text) # type: ignore
            self.factor_n=float(eval(self.factor.text)) #type: ignore
            self.cFee_n=round(self.calculate(self.suit_val_n*self.factor_n),2) # type: ignore
            self.cfee.text='[b][color=ffffff]Property Value :\n {} \n Court Fee :\n {}[/color][/b]'.format(str(self.suit_val_n),str(self.cFee_n)) # type: ignore
        except:

            self.cfee.text='[b][color=ffffff]Property Value :\n {} \n Court Fee :\n {}[/color][/b]'.format(str(self.suit_val_n),str(self.cFee_n)) # type: ignore
            self.suit_val.text=str(0)  # type: ignore
            self.factor.text=str(1) # type: ignore
    
    def pastef(self):
        self.suit_val.text=Clipboard.paste() # type: ignore
    def calculate(self,x):
        if x==0:
            return 0
        elif x>0 and x<=100:
            return np.ceil(x/5)*0.6
        elif x>100 and x<=1000:
            return self.calculate(100)+np.ceil((x-100)/10)*1.1
        elif x>1000 and x<=10000:
            return self.calculate(1000)+np.ceil((x-1000)/100)*7.50
        elif x>10000 and x<=20000:
            return self.calculate(10000)+np.ceil((x-10000)/500)*30
        elif x>20000 and x<=30000:
            return self.calculate(20000)+np.ceil((x-20000)/1000)*40
        elif x>30000 and x<=50000:
            return self.calculate(30000)+np.ceil((x-30000)/2000)*60
        elif x>50000 and x<=100000:
            return self.calculate(50000)+np.ceil((x-50000)/4000)*80
        elif x>100000:
            return self.calculate(100000)+np.ceil((x-100000)/10000)*100
        else:
            return 'Error'
    def reset(self):
        self.suit_val.text='0.0' # type: ignore
        self.factor.text='0.0' #type: ignore
        self.Fee='0.0' # type: ignore      
