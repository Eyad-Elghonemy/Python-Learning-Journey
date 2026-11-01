# ----------------------------------------
# -- Flask => Intro And Your First Page --
# ----------------------------------------
# - Flask Is Micro Framework Built With Python
# --------------------------------------------
# - HTML
# - CSS
# - JavaScript
# --------------------------------------------

from flask import Flask

skills_app = Flask(__name__)

@skills_app.route("/")
def home_page():
    
    return "Hello From Flask FrameWork"


@skills_app.route("/about")
def about():
    
    return "About Page From Flask FrameWork"


if __name__ == "__main__" :
    
    skills_app.run()