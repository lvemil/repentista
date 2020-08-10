from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty
from kivy.uix.label import Label

class TarjetaDecima(ButtonBehavior, BoxLayout):
    titulo = StringProperty()
    verso = StringProperty()
    
    def __init__(self, **kwargs):
        super(TarjetaDecima, self).__init__(**kwargs)

    def on_press(self):
        pass

    def on_release(self):
        pass