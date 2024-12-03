from flask import Flask, render_template, request
from app.utils.google_news_api import fetch_articles
from app.routes import app

app = Flask(__name__, static_folder='static', static_url_path='/static')


@app.route('/')
def index():
    # Pagination setup
    page = int(request.args.get('page', 1))
    per_page = 10
    all_articles = fetch_articles()
    total_articles = len(all_articles)
    total_pages = (total_articles + per_page - 1) // per_page
    paginated_articles = all_articles[(page - 1) * per_page: page * per_page]

    return render_template(
        'index.html',
        articles=paginated_articles,
        page=page,
        total_pages=total_pages
    )

if __name__ == "__main__":
    app.run(debug=True)


 