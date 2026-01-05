import os
from dotenv import load_dotenv

def get_title():
    #check the existance of env
    if not os.path.isfile(".env"):
        print(".env is missing")
        return "no title yet"
    
    load_dotenv()
    title = os.getenv("PROJECT_NAME")
    
    #check if var exists
    if type(title) == "None":
        print("Title missing")
    else:
        return title
