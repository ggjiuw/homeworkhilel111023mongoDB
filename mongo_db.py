import pymongo
from config import USER, PASSWORD

url = f'mongodb+srv://{USER}:{PASSWORD}'\
    '@cluster0.pqlkvzb.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(url)

db = client.booksDB

fantasy_books_coll = db.fantasy_books
school_literature_coll = db.school_literature

fantasy_books_coll.insert_one(
    {'name': 'Гра престолів', 'price': 750, 'year': 2019, 'pages': 800}
)

school_books = [
    {'name': 'Хімія', 'class': 8, 'pages': 228, 'year': 2021},
    {'name': 'Історія України', 'class': 8, 'pages': 255, 'year': 2021},
    {'name': 'Англійська мова', 'class': 8, 'pages': 271, 'year': 2016},
    {'name': 'Інформатика', 'class': 8, 'pages': 221, 'year': 2021},
    {'name': 'Всесвітня історія', 'class': 8, 'pages': 143, 'year': 2021},
    {'name': 'Географія', 'class': 8, 'pages': 288, 'year': 2021},
    {'name': 'Алгебра', 'class': 8, 'pages': 270, 'year': 2019},
    {'name': 'Геометрія', 'class': 8, 'pages': 238, 'year': 2019},
    {'name': 'Українська мова', 'class': 8, 'pages': 191, 'year': 2018},
]

school_literature_coll.insert_many(school_books)

query = {'name': {'$regex': '[Іі]сторія'}}
result = school_literature_coll.find(query)
for doc in result:
    print(doc)

current = {'name': 'Гра престолів'}
operation = {'$inc': {'price': 56}}
data = fantasy_books_coll.update_one(current, operation)
print(f'+56\n{data.raw_result}')

current = {'name': 'Гра престолів'}
data = fantasy_books_coll.delete_one(current)
print(f'видалення\n{data.raw_result}')

filter = {'year': {'$lt': 2020}}
school_literature_coll.delete_many(filter)
