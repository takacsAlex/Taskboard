from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color

class TaskComponent(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "tb-lr"
        self.cols = 1
        self.rows = 1

        
        self.teszt = Button(text="Task")
        self.add_widget(self.teszt)

        
        # with self.canvas:
        #     Color(1, 1, 1, mode="rgb")
        #     self.background = Rectangle()
        #     self.background.size = self.size
        #     self.background.pos = self.pos
        
        # self.teszt = Button(text="Task")
        # self.add_widget(self.teszt)
