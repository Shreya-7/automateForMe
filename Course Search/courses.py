import webbrowser
import sys

search = '+'.join(sys.argv[1:])

coursera = 'https://www.coursera.org/search?query=' + search + \
    '&index=prod_all_products_term_optimization&allLanguages=English'
udemy = 'https://www.udemy.com/courses/search/?lang=en&q=' + \
    search + '&sort=relevance&src=ukw'
udacity = 'https://www.udacity.com/courses/all'
edx = 'https://www.edx.org/course?search_query=' + search + '&language=English'
fcc = 'https://www.freecodecamp.org/news/search/?query=' + search
alison = 'https://alison.com/courses?query=' + search
earth = 'https://academicearth.org/?s=' + search
academy = 'https://www.codecademy.com/search?query=' + search
khan = 'https://www.khanacademy.org/search?page_search_query=' + search

sites = [coursera, udemy, edx, fcc, alison, earth, academy, khan, udacity]

for i in sites:
    webbrowser.open(i)
