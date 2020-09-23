from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.uix.label import Label

from repentista.metrica import medir_verso

class Verso(BoxLayout):
    num = NumericProperty()
    texto = StringProperty()
    metrica = StringProperty()
    rima_composicion = StringProperty()
    metrica_composicion = StringProperty()
    rima = StringProperty()
    txt_texto = ObjectProperty()
    ultimo = NumericProperty ()
    pantalla = ObjectProperty()
    valido = StringProperty()

    def __init__(self, **kwargs):
        super(Verso, self).__init__(**kwargs)
        self.txt_texto.bind(focus = self.on_focus)

    def on_press(self):
        self.manager.id_poema = self.id
        self.manager.current = 'poema'

    def on_texto(self, instance, value):
        print(value)
        if value:
            m = medir_verso(value)
            if m:
                self.metrica = str(m["medida"])
            self.pantalla.buscar_rima()
            if self.pantalla.estado == "editando":
                self.pantalla.estado = "modificado"

    def on_rima(self, instance, value):
        if value:
            self.validar_verso()
    
    def on_metrica(self, instance, value):
        if value:
            self.validar_verso()

    def on_focus(self, instance, value):
        if value:
            self.pantalla.verso_activo = self

    def validar_verso(self):
        if self.metrica == self.metrica_composicion and self.rima == self.rima_composicion:
            self.valido = "ok"
        else:
            self.valido = ""

    def txt_texto_on_text(self):
        self.texto = self.txt_texto.text.strip()
        if self.ultimo == 1 and self.texto and self.pantalla.estado in ["editando", "modificado"] and self.pantalla.composicion == "libre":
            self.ultimo = 0
            self.pantalla.adicionar_verso()

