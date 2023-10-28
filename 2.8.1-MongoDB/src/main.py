import connect
from models import Author, Quote


def tags_from_db(req):
    quotes = Quote.objects(tags__name__in=req)
    for quote in quotes:
        print(quote.quote)


def tag_from_db(req):
    quotes = Quote.objects(tags__name=req)
    for quote in quotes:
        print(quote.quote)


def name_from_db(req):
    authors = Author.objects(fullname=req)
    for author in authors:
        quotes = Quote.objects(author=author.id)
        for quote in quotes:
            print(quote.quote)


while True:
    request = input("command: ").split(":")
    if len(request) > 2:
        print(":(")
        break

    match request[0]:
        case "exit":
            break
        case "tags":
            data = request[1].split(",")
            tags_from_db(data)
        case "tag":
            data = request[1]
            tag_from_db(data)
        case "name":
            data = request[1]
            name_from_db(data)
