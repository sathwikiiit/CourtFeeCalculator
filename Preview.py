from kivy.core.clipboard import Clipboard
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Canvas, Color, Rectangle
from kivy.properties import NumericProperty, ObjectProperty,ReferenceListProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.vector import Vector

class Preview(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ext=[]
        self.val=0
        self.price=0
        self.V=""
    def add_sy(self):
        self.ext.append(self.v1.text+'-'+self.v2.text) # type: ignore
        self.val+=float(self.v1.text)*40+float(self.v2.text) # type: ignore
        self.valt.text='Ac. %d - %.2f gts.'%(self.val//40, self.val%40) # type: ignore
        self.v1.text='0' # type: ignore
        self.v2.text='0' # type: ignore
        
    def evaluate(self):
        self.price=self.val*float(self.pa.text)/40 # type: ignore
        self.l_price.text='Rs. '+str(float(self.price)) # type: ignore
    
    def copyf(self):
        Clipboard.copy(str(self.price))
    def reset(self):
        self.valt.text='Ac. 0 - 0.0 gts' # type: ignore
        self.v1.text='0' # type: ignore
        self.v2.text='0' # type: ignore
        self.price=0
        self.val=0
        self.l_price.text='Rs. 0.0' # type: ignore
        self.pa.text='0.0' # type: ignore

