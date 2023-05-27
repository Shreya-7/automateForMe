import io
import os
import re
import sys
import zipfile
import requests
import pprint


def get_movie_object(movie_name: str):
    movie = {}
    search_results = requests.get('https://yts-subs.com/search/ajax/' + movie_name).json()

    if len(search_results) > 1:
        print(f'\nFound multiple movies matching "{movie_name}", select one:\n')
        counter = 1
        for i in search_results:
            print(f"{counter}. {i['mov_title']}")
            counter+=1
        print()
        movie = search_results[int(input())-1]
    else:
        movie = search_results[0]
    return movie

def download_and_save_subtitle(movie_name: str):
    movie = get_movie_object(movie_name)

    # html page containing all subtitle results for the selected movie
    subtitles_html = requests.get('https://yts-subs.com/movie-imdb/' + movie['mov_imdb_code']).text
    subtitles_html = "".join(subtitles_html.split())

    # all rows, each row containing one subtitle
    rows = re.compile(r'\<tr.*?\/tr\>').findall(subtitles_html)
    english_subtitles = []

    for row in rows:
        # filter out rows containing english subtitles
        if re.compile(r'\<spanclass="sub-lang"\>English\<\/span\>').search(row) != None:
            rating = re.compile(r'\<spanclass="label.*?"\>(\d*)\<\/span\>').search(row).group(1)
            name = re.compile(r'\<spanclass="sub-lang"\>English\<\/span\>\<\/td>\<td\>\<ahref="/subtitles/(.*?)"\>').search(row).group(1)

            english_subtitles.append({
                'rating': rating,
                'name': name
            })

    # the highest rated subtitle will be downloaded
    english_subtitles.sort(key=lambda x: x['rating'], reverse=True)

    print("\nEnglish subtitles found:\n")
    pprint.pprint(english_subtitles)

    # fetch the zip of the highest rated subtitle
    response = requests.get('https://yifysubtitles.ch/subtitle/' + english_subtitles[0]['name'] + '.zip')
    z = zipfile.ZipFile(io.BytesIO(response.content))

    for info in z.infolist():
        # rename the subtitle to the movie name
        info.filename = movie['mov_title'] + '.srt'
        z.extract(info, path=os.path.join(os.getcwd(), 'output'))

    print("\nSubtitle successfully downloaded!!!\n")

if __name__ == '__main__':
    movie_name = sys.argv[1].strip()
    download_and_save_subtitle(movie_name)