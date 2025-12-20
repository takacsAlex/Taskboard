from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
    
class TaskBoxModule(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.count_task = 7
        
        self.cols = 1
        self.orientation = "tb-lr"      #top => bottom and left => right
        self.size_hint_y = None
        self.spacing = 10
        self.height = self.minimum_height
        self.widht = self.minimum_width
        self.bind(minimum_height=self.setter('height'))
        
        #template only
        for i in range(self.count_task):
            self.label = Button()
            self.label.text = "task" + str(i + 1)
            self.label.size_hint = (.5, None)
            self.add_widget(self.label)

