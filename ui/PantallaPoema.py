from datetime import datetime

from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty
from kivy.utils import get_color_from_hex

from ui.TarjetaDecima import TarjetaDecima
from modelo.Poema import Poema

class PantallaPoema(Screen):
    gl_decimas = ObjectProperty()
    sv_decimas = ObjectProperty()
    
    id = StringProperty()
    titulo = StringProperty()
    cuerpo = StringProperty()
    modificado = StringProperty()

    def __init__(self, **kwargs):
        super(PantallaPoema, self).__init__(**kwargs)
        self.on_enter = self.do_on_enter

    def do_on_enter(self):
        self.id = self.manager.id_poema
        p = Poema.Obtener("data/repentista.db", self.id)
        self.titulo = p.titulo
        self.cuerpo = p.cuerpo
        self.modificado = p.modificado
        versos = p.cuerpo.splitlines()
        self.gl_versos.clear_widgets()
        for v in versos:
            self.gl_versos.add_widget(TextInput(text = v, size_hint_y = None, height = 60))
    
    def btn_atras_on_press(self):
        self.manager.current = "inicio"
