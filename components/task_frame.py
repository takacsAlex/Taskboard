from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
    
class TaskBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "vertical"
        self.height = 50
        self.width = 100
        self.pos_hint = {"center_x": .2, "center_y": 0.5}
        
        for i in range(0, 3):
            self.label1 = Button()
            self.label1.text = "test1"
            self.add_widget(self.label1)

        