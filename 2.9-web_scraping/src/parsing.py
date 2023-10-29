import json
import requests
from bs4 import BeautifulSoup


def parse():
    page = 1
    authors_list = list()
    quotes_list = list()
    links = list()

    while True:
        print(f' [x] Parsing page: {page}')
        response = requests.get(f'https://quotes.toscrape.com/page/{page}')
        soup = BeautifulSoup(response.text, 'lxml')

        pages = soup.find(class_='pager').find(class_='next')
        if not pages:
            print(f' [x] Done\n')
            break
        page += 1

        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        tags = soup.find_all('div', class_='tags')
        links += [author.findParent().find('a').get('href') for author in authors]

        for i in range(0, len(quotes)):
            tags_for_quote = tags[i].find_all('a', class_='tag')
            quote = {
                "tags": [tag.text for tag in tags_for_quote],
                "author": authors[i].text,
                "quote": quotes[i].text
            }
            quotes_list.append(quote)
        print(f' [x] Done\n')

    for link in set(links):
        print(f' [x] Parsing link: https://quotes.toscrape.com{link}')
        response = requests.get(f'https://quotes.toscrape.com{link}')
        soup = BeautifulSoup(response.text, 'lxml')

        details = soup.find('div', class_='author-details')
        fullname = details.find(class_='author-title')
        born_date = details.find(class_='author-born-date')
        born_location = details.find(class_='author-born-location')
        description = details.find(class_='author-description')

        authors_list.append(
            {
                'fullname': fullname.text,
                'born_date': born_date.text,
                'born_location': born_location.text,
                'description': description.text.strip()
            }
        )
        print(f' [x] Done\n')

    print(f' [x] Saving to json')

    with open('../data/quotes.json', 'a', encoding='utf-8') as file:
        json.dump(quotes_list, file, indent=4, ensure_ascii=False)

    with open('../data/authors.json', 'a', encoding='utf-8') as file:
        json.dump(authors_list, file, indent=4, ensure_ascii=False)

    print(f' [x] Done\n')
