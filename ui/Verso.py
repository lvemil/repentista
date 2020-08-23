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
    rima = StringProperty()
    txt_texto = ObjectProperty()
    ultimo = NumericProperty ()
    pantalla = ObjectProperty()

    def __init__(self, **kwargs):
        super(Verso, self).__init__(**kwargs)
        self.ultimo = 1

    def on_press(self):
        self.manager.id_poema = self.id
        self.manager.current = 'poema'

    def on_texto(self, instance, value):
        print(value)
        if value:
            m = medir_verso(value)
            if m:
                self.metrica = str(m["medida"])

    def txt_texto_on_text(self):
        self.texto = self.txt_texto.text.strip()
        if self.texto:
            self.pantalla.buscar_rima()
        if self.ultimo == 1 and self.texto:
            self.ultimo = 0
            self.pantalla.adicionar_verso()

    def txt_texto_on_key_down(self):
        print("key down")
