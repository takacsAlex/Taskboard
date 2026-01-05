from kivy.uix.label import Label
from database.get_title import get_title

import os

class Title(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.project_name = ""
        #check if title created
        if os.path.isfile(".env"):
            self.project_name = get_title()
            
        self.text = self.project_name.capitalize() + " " + "Taskboard"
        self.font_size = "38pt"
        self.bold = True
        self.pos_hint = {"center_x": .35, "center_y": .92}