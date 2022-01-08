from flask import render_template, request
from Flask_Directory import app, forms, api_methods


@app.route('/', methods=["GET"])
@app.route('/home', methods=["GET"])
def index():
    return render_template("index.html")


@app.route('/best-sellers', methods=["GET", "POST"])
def best_sellers():
    form_bestsellers = forms.BookForms(request.form)
    if request.method == 'POST':
        selected_date = request.form["date_field"]
        selected_name = request.form["genre"]
        bestsellers = api_methods.request_best_sellers(selected_date, selected_name)
        bestsellers_list = []

        for i in bestsellers["results"]["books"]:
            best_books = (i["rank"], i["title"], i["author"], i["book_image"], i["amazon_product_url"])
            bestsellers_list.append(best_books)
            if len(bestsellers_list) == 10:  # once 10 books are appended, breaks from the loop
                break
        return render_template("best_sellers_results.html", response=bestsellers_list)
    return render_template("best_sellers_search.html", form=form_bestsellers)


@app.route('/book-reviews', methods=["GET", "POST"])
def book_reviews():
    form_bookreviews = forms.BookForms(request.form)
    if request.method == 'POST':
        selected_isbn = request.form["isbn"]
        selected_title = request.form["title"]
        selected_author = request.form["author"]
        bookreviews_list = []

    return render_template("book_reviews_search.html", form=form_bookreviews)
