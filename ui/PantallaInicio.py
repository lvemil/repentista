from datetime import datetime

from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.utils import get_color_from_hex

from ui.TarjetaPoema import TarjetaPoema
from ui.PantallaSeleccionarComposicion import PantallaSeleccionarComposicion
from modelo.Poema import Poema

class PantallaInicio(Screen):
    gl_poemas = ObjectProperty()
    sv_poemas = ObjectProperty()
    def __init__(self, **kwargs):
        super(PantallaInicio, self).__init__(**kwargs)
        self.on_enter = self.do_on_enter

    def do_on_enter(self):
        self.orden = "DESC"
        self.mostrar_poemas()

    def btn_orden_on_press(self):
        self.orden = "DESC" if self.orden == "ASC" else "ASC"
        self.mostrar_poemas()

    def on_seleccionar_composicion(self, composicion):
        self.manager.id_poema = None
        self.manager.composicion = composicion
        self.manager.current = 'poema'

    def btn_nuevo_on_press(self):
        PantallaSeleccionarComposicion.mostrar(on_seleccionar=self.on_seleccionar_composicion)
    
    def mostrar_poemas(self):
        poemas = Poema.ObtenerTodos("data/repentista.db", self.orden)
        self.gl_poemas.clear_widgets()
        for p in poemas:
            d = TarjetaPoema()
            d.manager = self.manager
            d.id = p[0]
            d.titulo = str(p[1])
            d.composicion = p[5]
            d.verso = (p[2].splitlines()[0] + "...") if p[2] else "[vacio]"
            m = datetime.strptime(p[3], "%Y-%m-%d %H:%M:%S")
            d.modificado = m.strftime("%d/%m/%Y")
            self.gl_poemas.add_widget(d)
