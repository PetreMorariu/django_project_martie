import random
from datetime import date
from main_app.models import Book, BookDetail


def generate_isbn():
    #returns a number with is 13 random characters

    result = []
    for i in range(13):
        v = random.randint(0, 9)
        result.append(str(v))
    return ''.join(result)

def summarize_text(text):
    return text[:10]

def create_book_detail(book:Book):
    BookDetail.objects.create(
        summary = summarize_text(book.title),
        published_date = date.today(),
        isbn = generate_isbn(),
        book = book
    )