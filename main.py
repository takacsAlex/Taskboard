#set resizable false by giving size
from kivy.config import Config
Config.set("graphics", "width", 650)
Config.set("graphics", "height", 600)
Config.set("graphics", "resizable", False)

#set backgroundcolor
from kivy.core.window import Window
Window.clearcolor = "#393939"

#import essentials
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle

#components
from components.title import Title
from components.task_frame import TaskBox


class MainBoard(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #title for project name
        with self.canvas:
            Color(.15, .15, .15, mode="rgb")
            self.background = Rectangle(pos=(0, 500), size=(650, 100))
        self.title = Title()
        self.add_widget(self.title)
        
        self.add_widget(TaskBox())
        

class TaskBoard(App):
    def build(self):
        return MainBoard()