import psycopg
import dotenv
import os
from random import randint


vars = (
    ('host', 'PG_HOST'),
    ('port', 'PG_PORT'),
    ('user', 'PG_USER'),
    ('password', 'PG_PASSWORD'),
    ('dbname', 'PG_DBNAME'),
)

dotenv.load_dotenv()
credentials = {var: os.getenv(env_var) for var, env_var in vars}

connection = psycopg.connect(**credentials)
cursor = connection.cursor()

# genres = (
#     ('computer science', 
#      'you want to abandon your normal life for good? your clear choice'),
#     ('detective', 'try and find out how students homework works'),
#     ('horror', 'first flake8 usage'),
#     ('fantasy', 'full students attendance'),
# )
# for genre in genres:
#     cursor.execute('INSERT INTO library.genre (name, description) VALUES (%s, %s)', genre)

cursor.execute('SELECT id FROM library.genre')
genres_ids = [row[0] for row in cursor.fetchall()]

cursor.execute('SELECT id FROM library.book')
books_ids = [row[0] for row in cursor.fetchall()]
if genres_ids:
    for book_id in books_ids:
        genres = genres_ids.copy()
        for _ in range(randint(1, 3)):
            cursor.execute(
                'INSERT INTO library.book_genre (book_id, genre_id) VALUES (%s, %s)',
                (book_id, genres.pop(randint(0, len(genres) - 1))),
            )

cursor.close()
connection.commit()
connection.close()
