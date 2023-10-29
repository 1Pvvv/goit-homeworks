import json
import connect

from datetime import datetime
from models import Tag, Author, Quote


def saving_quotes_to_db():
    print(f' [x] Saving quotes.json to mongoDB')
    with open("../data/quotes.json", "r", encoding="utf-8") as file:
        quotes = json.load(file)
    for item in quotes:
        tags = Tag(name=item["tags"])

        for author in Author.objects():
            if author.fullname == item["author"]:
                quote = Quote(tags=tags, author=author, quote=item["quote"])
                quote.save()
    print(f' [x] Done\n')


def saving_authors_to_db():
    print(f' [x] Saving authors.json to mongoDB')
    with open("../data/authors.json", "r", encoding="utf-8") as file:
        authors = json.load(file)

    for item in authors:
        author = Author(
            fullname=item["fullname"],
            born_date=datetime.strptime(item["born_date"], "%B %d, %Y"),
            born_location=item["born_location"],
            description=item["description"],
        )
        author.save()
    print(f' [x] Done\n')
