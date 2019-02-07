import os
import shutil

import omdb


omdb.set_default('apikey', '63bd66b7')


def title_formater(title):
    if '(' in title:
        title = title[:title.index(' (')]
    return title


def organize_movies(path):
    movies = os.listdir(path)
    os.chdir(path)
    for title in movies:
        if title in [str(i) for i in range(1, 11)]:
            continue
        formated_title = title_formater(title)
        rating = omdb.title(formated_title)['imdb_rating']
        print(f'Moving "{formated_title}" to folder {rating[0]}')
        if not os.path.exists(rating[0]):
            os.mkdir(rating[0])
        shutil.move(title, rating[0])


if '__main__' == __name__:
    organize_movies('')