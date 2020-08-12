from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from ui.PantallaInicio import PantallaInicio
from ui.PantallaPoema import PantallaPoema

class RepentistaApp(App):
    def build(self):

        self.title = 'Repentista'
        
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(PantallaInicio(name='inicio'))
        sm.add_widget(PantallaPoema(name='poema'))

        return sm