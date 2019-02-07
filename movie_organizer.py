import os
import shutil
import argparse
import omdb

from requests.exceptions import HTTPError


def title_formater(title):
    if '(' in title:
        title = title[:title.index(' (')]
    return title


def get_apikey():
    apikey = None

    if os.environ.get('OMDB_API_KEY'):
        apikey = os.environ.get('OMDB_API_KEY')
    
    if args.apikey:
        apikey = args.apikey
    
    return apikey


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
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help="Full path for movies folder.")
    parser.add_argument("--apikey", help="""You can get omdb api key from this link http://www.omdbapi.com/apikey.aspx.
                                         Or Add OMDB_API_KEY eniroment variable.""")
    args = parser.parse_args()

    omdb.set_default('apikey', get_apikey())
    
    try:
        organize_movies(args.path)
    except HTTPError as ex:
        print("Error: Can't authorize request you must add --apikey arg or OMDB_API_KEY env var.")
    except ConnectionError as ex:
        print('Error: you must have internet connection.')
