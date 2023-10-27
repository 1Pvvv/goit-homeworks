import json

from datetime import datetime

import connect
from models import Tag, Author, Quote

with open('../data/authors.json', 'r', encoding='utf-8') as file:
    authors = json.load(file)

with open('../data/qoutes.json', 'r', encoding='utf-8') as file:
    quotes = json.load(file)

for item in authors:
    author = Author(
        fullname=item['fullname'],
        born_date=datetime.strptime(item['born_date'], "%B %d, %Y"),
        born_location=item['born_location'],
        description=item['description']
    ).save()

for item in quotes:
    tags = Tag(
        name=item['tags']
    )

    for author in Author.objects():
        if author.fullname == item['author']:
            quote = Quote(
                tags=tags,
                author=author,
                quote=item['quote']
            ).save()
