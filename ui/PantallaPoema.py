from datetime import datetime
import logging
import functools


from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

from ui.TarjetaPoema import TarjetaPoema
from ui.PantallaConfirmacion import PantallaConfirmacion
from ui.Verso import Verso
from ui.PantallaSeleccionarPalabraRima import PantallaSeleccionarPalabraRima
from modelo.Poema import Poema
from repentista.rima import rima_poema
from repentista.composicion import composicion, debe_rimar_con

class PantallaPoema(Screen):
    gl_versos = ObjectProperty()
    sv_versos = ObjectProperty()
    txt_titulo = ObjectProperty()

    id = StringProperty()
    titulo = StringProperty()
    composicion = StringProperty()
    cuerpo = StringProperty()
    modificado = StringProperty()
    estado = StringProperty()
    verso_activo = ObjectProperty()

    def __init__(self, **kwargs):
        super(PantallaPoema, self).__init__(**kwargs)
        self.on_enter = self.do_on_enter
        self.on_pre_leave = self.do_on_pre_leave

    def on_estado(self, instance, value):
        print(value)

    def btn_atras_on_press(self):
        self.manager.current = 'inicio'

    def btn_eliminar_on_press(self):
        PantallaConfirmacion.mostrar(on_aceptar = lambda : {
            self.eliminar_poema()
        })        

    def on_seleccionar_palabra(self, palabra):
        self.gl_versos.children[0-self.verso_activo.num].texto += palabra 

    def btn_buscar_rima_on_press(self):
        v = debe_rimar_con(self.verso_activo.num, self.composicion)
        if v:       
            t = self.gl_versos.children[0-v].texto
            palabra = t.split()[-1]
        else:
            palabra = ""
        PantallaSeleccionarPalabraRima.mostrar(palabra = palabra, on_seleccionar=self.on_seleccionar_palabra)

    def txt_titulo_on_text(self):
        if self.estado == "editando":
            self.estado = "modificado"

    def auto_guardar(self, dt):
        self.guardar_poema()

    def do_on_enter(self):
        if self.manager.id_poema:
            self.id = self.manager.id_poema
            p = Poema.Obtener("data/repentista.db", self.id)
            self.titulo = p.titulo
            self.cuerpo = p.cuerpo if p.cuerpo else ""
            self.modificado = p.modificado
            self.composicion = p.composicion
            versos = self.cuerpo.split("\n")
            self.gl_versos.clear_widgets()
            self.estado = "cargando"
            c = composicion(p.composicion)
            cant_versos = len(versos)
            for i,v in enumerate(versos):
                if p.composicion == "libre":
                    self.adicionar_verso(texto = v, ultimo = 0)    
                else:
                    self.adicionar_verso(
                        texto = v, 
                        ultimo = 0 if i < cant_versos-1 else 1, 
                        metrica_composicion = str(c[0][i][0]), 
                        rima_composicion = c[0][i][1])

            if p.composicion == "libre":
                self.adicionar_verso(texto = "", ultimo=1)
        else:
            self.id = ""
            self.titulo = "Nuevo poema"
            self.cuerpo = ""
            self.composicion = self.manager.composicion
            self.modificado = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.gl_versos.clear_widgets()
            if self.manager.composicion:
                self.agregar_espacios(self.manager.composicion)
        
        self.estado = "editando"
        self.buscar_rima()
        self.__clock_event = Clock.schedule_interval(self.auto_guardar, 60)

    def do_on_pre_leave(self):
        self.guardar_poema()

    def agregar_espacios(self, nombre_composicion):
        c = composicion(nombre_composicion)
        cant_versos = len(c[0])
        for i,v in enumerate(c[0]):
            self.adicionar_verso(texto = "", ultimo = 0 if i < cant_versos-1 else 1, metrica_composicion = str(v[0]), rima_composicion = v[1])

    def guardar_poema(self):
        if self.estado == "modificado":
            print("guardando...")
            versos = list(reversed([v.texto for v in self.gl_versos.children]))
            cuerpo = versos if self.composicion != "libre" else versos[:-1]
            p = Poema(id = self.id, titulo = self.txt_titulo.text, composicion = self.composicion, cuerpo = cuerpo)
            r = Poema.Guardar("data/repentista.db", p)
            self.id = r
            self.modificado = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.estado = "editando"
    
    def eliminar_poema(self):        
        Poema.Eliminar("data/repentista.db", self.id)
        self.estado = "eliminado"
        self.btn_atras_on_press()
        
    def adicionar_verso(self, texto = '', ultimo = 0, metrica_composicion = "", rima_composicion = ""):
        w = Verso()
        w.pantalla = self
        w.texto = texto
        w.num = len(self.gl_versos.children) + 1
        w.ultimo = ultimo
        w.metrica_composicion = metrica_composicion
        w.rima_composicion = rima_composicion
        self.gl_versos.add_widget(w)

    def buscar_rima(self):
        if self.estado in ["editando", "modificado"]:
            versos = list(reversed([v.texto for v in self.gl_versos.children]))
            if versos:
                versos = versos if versos[-1] else versos[:-1]
                rima = rima_poema(versos)
                if rima:
                    o = 0 if self.gl_versos.children[0].texto else 1 
                    for i, r in enumerate(reversed(rima)):
                        self.gl_versos.children[i+o].rima = r

