from flask import render_template, request, redirect, url_for, flash
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

        if not bestsellers["results"]:
            flash(f'Sorry, there are no best sellers for the date: {selected_date} and genre {selected_name}')
            return render_template("best_sellers_search.html", form=form_bestsellers)

        for book in bestsellers["results"]["books"]:
            best_books = (book["rank"], book["title"], book["author"], book["book_image"], book["amazon_product_url"])
            bestsellers_list.append(best_books)

        return render_template("best_sellers_results.html", response=bestsellers_list, name=selected_name, date=selected_date)
    return render_template("best_sellers_search.html", form=form_bestsellers)


@app.route('/book-reviews-options', methods=["GET", "POST"])
def book_reviews_options():
    option_bookreviews = forms.Options(request.form)

    if request.method == 'POST':
        selected_option = request.form["option"]

        return redirect(url_for('book_reviews', option=str(selected_option)))
    return render_template("book_reviews_options.html", option_form=option_bookreviews)


@app.route('/book-reviews/<string:option>', methods=["GET", "POST"])
def book_reviews(option):
    form_bookreviews = forms.BookForms(request.form)

    if request.method == 'POST':
        # If ISBN option is selected
        if option == 'isbn':
            selected_isbn = request.form["isbn"]
            isbn_reviews = api_methods.request_book_reviews_isbn(selected_isbn)

            bookreviews_list = get_reviews_list(isbn_reviews, selected_isbn, option)

            return render_template("book_reviews_results.html", response=bookreviews_list, value=selected_isbn)

        # If Title option is selected
        elif option == 'title':
            selected_title = request.form["title"]
            title_reviews = api_methods.request_book_reviews_title(selected_title)

            bookreviews_list = get_reviews_list(title_reviews, selected_title, option)

            return render_template("book_reviews_results.html", response=bookreviews_list, value=selected_title)

        # If Author option is selected
        else:
            selected_author = request.form["author"]
            author_reviews = api_methods.request_book_reviews_author(selected_author)

            bookreviews_list = get_reviews_list(author_reviews, selected_author, option)

            return render_template("book_reviews_results.html", response=bookreviews_list, value=selected_author)

    return render_template("book_reviews_search.html", form=form_bookreviews, option=option)


def get_reviews_list(reviews, value, option):
    bookreviews = []

    if not reviews["results"]:
        flash(f'Sorry, there are no best sellers for the {option} {value}')
        return redirect(url_for('book_reviews', option=option))
    for review in reviews["results"]:
        reviews_info = (review["book_title"], review["book_author"], review["summary"], review["url"])
        bookreviews.append(reviews_info)

    return bookreviews