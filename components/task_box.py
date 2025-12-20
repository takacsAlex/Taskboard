from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from components.task_box_module import TaskBoxModule

class TaskBox(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.cols = 1
        self.size_hint = (.3, .6)
        
        self.scroll_bar = ScrollView()
        self.scroll_bar.do_scroll_x = False
        self.scroll_bar.do_scroll_y = True
        self.scroll_bar.size = self.size
        self.add_widget(self.scroll_bar)
        
        self.task_box_grid = TaskBoxModule()
        self.scroll_bar.add_widget(self.task_box_grid)