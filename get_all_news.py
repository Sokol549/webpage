from webapp import create_app
from webapp.news.parsers import ranobe

app = create_app()
with app.app_context():
    ranobe.ranobe_pars()