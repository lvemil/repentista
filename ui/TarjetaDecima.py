from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.label import Label

class TarjetaDecima(ButtonBehavior, BoxLayout):
    id = StringProperty()
    titulo = StringProperty()
    verso = StringProperty()
    modificado = StringProperty()
    manager = ObjectProperty()

    def __init__(self, **kwargs):
        super(TarjetaDecima, self).__init__(**kwargs)

    def on_press(self):
        self.manager.id_poema = self.id
        self.manager.current = 'poema'