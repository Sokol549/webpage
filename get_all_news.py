from webapp import create_app
from webapp.news.parsers import ranobehub

app = create_app()
with app.app_context():
    ranobehub.get_ranobe_title()