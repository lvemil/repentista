import logging
import kivy
from kivy.config import Config 

from repentista.silabeador import separar_silabas

from RepentistaApp import RepentistaApp

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    kivy.require('1.11.1')
    app = RepentistaApp() 
    app.run()