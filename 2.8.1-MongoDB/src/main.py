import connect
from models import Author, Quote


def tags_from_db(request):
    qoutes = Quote.objects(tags__name__in=request)
    for qoute in qoutes:
        print(qoute.quote)


def tag_from_db(request):
    qoutes = Quote.objects(tags__name=request)
    for qoute in qoutes:
        print(qoute.quote)


def name_from_db(request):
    authors = Author.objects(fullname=request)
    for author in authors:
        qoutes = Quote.objects(author=author.id)
        for qoute in qoutes:
            print(qoute.quote)


while True:
    request = input('command: ').split(':')
    if len(request) > 2:
        print(':(')
        break

    match request[0]:
        case 'exit':
            break
        case 'tags':
            data = request[1].split(',')
            tags_from_db(data)
        case 'tag':
            data = request[1]
            tag_from_db(data)
        case 'name':
            data = request[1]
            name_from_db(data)
