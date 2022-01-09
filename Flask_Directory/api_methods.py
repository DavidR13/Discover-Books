import requests
import os
from Flask_Directory import json_functions


def request_key():
    api_key = os.environ['API_KEY']
    return api_key


def get_abs_path():
    abs_path = os.environ['ABS_PATH']
    return abs_path


def request_best_sellers(date, name):
    best_sellers_url = "https://api.nytimes.com/svc/books/v3/lists/" + date + "/" + name + ".json?api-key=" + request_key()
    best_sellers_response = requests.get(best_sellers_url).json()

    json_functions.save_to_file(best_sellers_response, f"{get_abs_path()}/best_sellers.json")
    return best_sellers_response


def request_book_reviews_isbn(isbn):
    reviews_isbn_url = "https://api.nytimes.com/svc/books/v3/reviews.json?isbn=" + str(isbn) + "&api-key=" + request_key()
    reviews_isbn_response = requests.get(reviews_isbn_url).json()

    json_functions.save_to_file(reviews_isbn_response, f"{get_abs_path()}/isbn_reviews.json")
    return reviews_isbn_response


def request_book_reviews_title(title):
    reviews_title_url = "https://api.nytimes.com/svc/books/v3/reviews.json?title=" + title + "&api-key=" + request_key()
    reviews_title_response = requests.get(reviews_title_url).json()

    json_functions.save_to_file(reviews_title_response, f"{get_abs_path()}/title_reviews.json")
    return reviews_title_response


def request_book_reviews_author(author):
    reviews_author_url = "https://api.nytimes.com/svc/books/v3/reviews.json?author=" + author + "&api-key=" + request_key()
    reviews_author_response = requests.get(reviews_author_url).json()

    json_functions.save_to_file(reviews_author_response, f"{get_abs_path()}/author_reviews.json")
    return reviews_author_response
