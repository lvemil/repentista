from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, StringProperty

class PantallaConfirmacion(Screen):

    popup = ObjectProperty()
    respuesta = StringProperty()

    def __init__(self, **kwargs):
        super(PantallaConfirmacion, self).__init__(**kwargs)

    def btn_si_on_press(self):
        self.on_aceptar()
        self.popup.dismiss()

    def btn_no_on_press(self):
        self.popup.dismiss()

    @staticmethod
    def mostrar(on_aceptar):
        pantalla = PantallaConfirmacion()
        pop = Popup(title="Confirmacion", content=pantalla, size_hint=(None,None),size=(400,400)) 
        pop.separator_height = 0 
        pantalla.popup = pop
        pantalla.on_aceptar = on_aceptar
        pop.open() 
