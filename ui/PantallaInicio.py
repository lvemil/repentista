from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.utils import get_color_from_hex

from ui.TarjetaDecima import TarjetaDecima
from modelo.Poema import Poema

class PantallaInicio(Screen):
    gl_decimas = ObjectProperty()
    sv_decimas = ObjectProperty()
    def __init__(self, **kwargs):
        super(PantallaInicio, self).__init__(**kwargs)
        self.on_enter = self.do_on_enter

    def do_on_enter(self):
        poemas = Poema.ObtenerTodos("data/repentista.db")
        for p in poemas:
            d = TarjetaDecima()
            d.titulo = p[1]
            d.verso = (p[2].splitlines()[0] + "...") if p[2] else "[vacio]"
            self.gl_decimas.add_widget(d)