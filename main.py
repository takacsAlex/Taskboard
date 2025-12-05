from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

class MainBoard(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

class TaskBoard(App):
    def build(self):
        Window.clearcolor = "#393939"
        return MainBoard()