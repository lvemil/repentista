from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label

from repentista.rima import riman_con
from configuracion import Configuracion

class PantallaSeleccionarPalabraRima(Screen):

    popup = ObjectProperty()
    palabra = StringProperty()

    gl_palabras = ObjectProperty()
    sv_palabras = ObjectProperty()

    def __init__(self, **kwargs):
        super(PantallaSeleccionarPalabraRima, self).__init__(**kwargs)
        self.palabra = kwargs["palabra"]
        self.mostrar_palabras()

    def btn_palabra_on_press(self, instance):
        self.on_seleccionar(instance.text)
        self.popup.dismiss()

    def btn_buscar_on_press(self):
        self.palabra = self.txt_palabra.text
        self.mostrar_palabras()

    def mostrar_palabras(self):
        if self.palabra:
            self.gl_palabras.clear_widgets()
            consonante, asonante = riman_con(self.palabra, Configuracion.obtener("db"))
            l = Label()
            l.text = "Rima consonante"
            l.size_hint_y = None
            l.height = 60
            l.color = [0,0,0,1]
            self.gl_palabras.add_widget(l)
            if consonante:
                for c in consonante:
                    b = Button(text = c)
                    b.size_hint_y = None
                    b.height = 60
                    b.bind(on_press=self.btn_palabra_on_press)
                    self.gl_palabras.add_widget(b)
            else:
                l = Label()
                l.text = "[ninguna]"
                l.size_hint_y = None
                l.height = 60
                l.color = [0,0,0,1]
                self.gl_palabras.add_widget(l)
            l = Label()
            l.text = "Rima asonante"
            l.size_hint_y = None
            l.height = 60
            l.color = [0,0,0,1]
            self.gl_palabras.add_widget(l)
            if asonante:
                for c in asonante:
                    b = Button(text = c)
                    b.size_hint_y = None
                    b.height = 60
                    b.bind(on_press=self.btn_palabra_on_press)
                    self.gl_palabras.add_widget(b)
            else:
                l = Label()
                l.text = "[ninguna]"
                l.size_hint_y = None
                l.height = 60
                l.color = [0,0,0,1]
                self.gl_palabras.add_widget(l)

    @staticmethod
    def mostrar(palabra, on_seleccionar):
        pantalla = PantallaSeleccionarPalabraRima(palabra = palabra)
        pop = Popup(title="Seleccione la palabra", content=pantalla, size_hint=(None,None),size=(500,800)) 
        pop.separator_height = 0 
        pantalla.popup = pop
        pantalla.on_seleccionar = on_seleccionar
        pop.open() 