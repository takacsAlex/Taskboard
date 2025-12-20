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
from components.task_box import TaskBox


class MainBoard(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #title for project name:
        with self.canvas:
            Color(.15, .15, .15, mode="rgb")
            self.background = Rectangle(pos=(0, 500), size=(650, 100))
        self.title = Title()
        self.add_widget(self.title)
        
        #task manage components:
        ##in-progress task's box
        with self.canvas:
            Color(.15, .15, .15, mode="rgb")
            self.background = Rectangle(pos=(65, 50), size=(227.5, 390))
        self.in_progress = TaskBox()
        self.in_progress.pos_hint = {"center_x": .275, "center_y": .41}
        self.add_widget(self.in_progress)
        
        ##completed task's box
        with self.canvas:
            Color(.15, .15, .15, mode="rgb")
            self.background = Rectangle(pos=(365, 50), size=(227.5, 390))
        self.in_completed_layout = TaskBox()
        self.in_completed_layout.pos_hint = {"center_x": .736, "center_y": .41}
        self.add_widget(self.in_completed_layout)


class TaskBoard(App):
    def build(self):
        return MainBoard()