from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button

from repentista.composicion import composicion

class PantallaSeleccionarComposicion(Screen):

    popup = ObjectProperty()
    composicion = StringProperty()

    gl_composiciones = ObjectProperty()
    sv_composiciones     = ObjectProperty()

    def __init__(self, **kwargs):
        super(PantallaSeleccionarComposicion, self).__init__(**kwargs)
        self.mostrar_composiciones()

    def btn_composicion_on_press(self, instance):
        self.on_seleccionar(instance.text)
        self.popup.dismiss()

    def mostrar_composiciones(self):
        composiciones = composicion()
        for c in composiciones:
            b = Button(text = c)
            b.size_hint_y = None
            b.height = 60
            b.bind(on_press=self.btn_composicion_on_press)
            self.gl_composiciones.add_widget(b)

    @staticmethod
    def mostrar(on_seleccionar):
        pantalla = PantallaSeleccionarComposicion()
        pop = Popup(title="Seleccione el tipo de composición", content=pantalla, size_hint=(None,None),size=(500,800)) 
        pop.separator_height = 0 
        pantalla.popup = pop
        pantalla.on_seleccionar = on_seleccionar
        pop.open() 