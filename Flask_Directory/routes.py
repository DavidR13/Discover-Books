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
    bookreviews_list = []

    if request.method == 'POST':
        # Get results if ISBN option is selected
        if option == 'isbn':
            selected_isbn = request.form["isbn"]

            if not selected_isbn:
                flash("Please fill in the information to look for book reviews.")
                return render_template("book_reviews_search.html", form=form_bookreviews, option=option)

            isbn_reviews = api_methods.request_book_reviews_isbn(selected_isbn)

            if not isbn_reviews["results"]:
                flash(f'Sorry, there are no best sellers for the ISBN {selected_isbn}')
                return render_template("book_reviews_search.html", form=form_bookreviews, option=option)
            for book in isbn_reviews["results"]:
                reviews = (book["book_title"], book["book_author"], book["summary"], book["url"])
                bookreviews_list.append(reviews)

            return render_template("book_reviews_results.html", response=bookreviews_list, isbn=selected_isbn)

        # Get results if Title option is selected
        elif option == 'title':
            selected_title = request.form["title"]

        # Get results if Author option is selected
        else:
            selected_author = request.form["author"]

    return render_template("book_reviews_search.html", form=form_bookreviews, option=option)
