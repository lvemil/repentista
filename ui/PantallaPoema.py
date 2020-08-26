from datetime import datetime

from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty
from kivy.utils import get_color_from_hex

from ui.TarjetaDecima import TarjetaDecima
from ui.Verso import Verso
from modelo.Poema import Poema
from repentista.rima import rima_poema

class PantallaPoema(Screen):
    gl_decimas = ObjectProperty()
    sv_decimas = ObjectProperty()
    txt_titulo = ObjectProperty()

    id = StringProperty()
    titulo = StringProperty()
    cuerpo = StringProperty()
    modificado = StringProperty()
    estado = StringProperty()

    def __init__(self, **kwargs):
        super(PantallaPoema, self).__init__(**kwargs)
        self.on_enter = self.do_on_enter
        self.on_pre_leave = self.do_on_pre_leave

    def btn_atras_on_press(self):
        self.manager.current = 'inicio'

    def do_on_enter(self):
        self.id = self.manager.id_poema
        p = Poema.Obtener("data/repentista.db", self.id)
        self.titulo = p.titulo
        self.cuerpo = p.cuerpo if p.cuerpo else ""
        self.modificado = p.modificado
        versos = self.cuerpo.splitlines()
        self.gl_versos.clear_widgets()
        self.estado = "cargando"
        for v in versos:
            self.adicionar_verso(v)    
        self.adicionar_verso("")
        self.estado = "editando"

    def do_on_pre_leave(self):
        self.salvar_poema()

    def salvar_poema(self):
        versos = list(reversed([v.texto for v in self.gl_versos.children]))
        cuerpo = versos if versos[-1] else versos[:-1]
        p = Poema(id = self.id, titulo = self.txt_titulo.text, cuerpo = cuerpo)
        r = Poema.Guardar("data/repentista.db", p)

    def adicionar_verso(self, texto = ''):
        w = Verso()
        w.pantalla = self
        w.texto = texto
        w.num = len(self.gl_versos.children) + 1
        self.gl_versos.add_widget(w)

    def buscar_rima(self):
        versos = list(reversed([v.texto for v in self.gl_versos.children]))
        if versos:
            versos = versos if versos[-1] else versos[:-1]
            rima = rima_poema(versos)
            o = 0 if self.gl_versos.children[0].texto else 1 
            for i, r in enumerate(reversed(rima)):
                self.gl_versos.children[i+o].rima = r

