import datetime
import re

now = datetime.datetime.now()


def valiateBookPayload(payload, book):
    if payload['year'] < 0 or payload['year'] > now.year:
        book.abort(400, "Invalid input")


def valiateAuthorPayload(payload, author):
    emailPattern = "^[a-z][a-z0-9_\.]{5,32}@[a-z0-9]{2,}(\.[a-z0-9]{2,4}){1,2}$"
    if not bool(re.match(emailPattern, payload['email'])):
        author.abort(400, "Invalid input")

    phonePattern = "[0-9]+$"
    if not bool(re.match(phonePattern, payload['phone'])):
        author.abort(400, "Invalid input")
