import json
from models import Author, Quote

authors_file = 'authors.json'
quotes_file = 'quotes.json'

with open(authors_file, 'r', encoding='utf-8') as f:
    authors_data = json.load(f)

with open(quotes_file, 'r', encoding='utf-8') as f:
    quotes_data = json.load(f)

authors_dict = {}
for author_data in authors_data:
    author = Author(
        fullname=author_data['fullname'],
        born_date=author_data.get('born_date'),
        born_location=author_data.get('born_location'),
        description=author_data.get('description')
    )
    author.save()
    authors_dict[author.fullname] = author

for quote_data in quotes_data:
    author_name = quote_data['author']
    author = authors_dict.get(author_name)
    if author:
        quote = Quote(
            tags=quote_data['tags'],
            author=author,
            quote=quote_data['quote']
        )
        quote.save()