import webbrowser
import argparse

# Puts together a collection of sites to open and opens them


def open_results(song, artist):

    # Youtube channel names arranged by artist focus
    youtube = {
        'JM': [
            'Zartimus', 'JamieHarrisonGuitar', 'PaulDavids', 'GuitarZero2Hero',
            'SixStringFingerpicking', 'GuitarLessons365SongLessons'
        ],
        'TS': [
            'GuitarGoddess', 'TheGroovyGuitarDude', 'for3v3rfaithful'
        ],
        'Other': ['JustinSandercoeSongs', 'rajshrilearn']
    }

    sites = []

    # getting song search results from Youtube channels
    for channel in youtube[artist]+youtube['Other']:
        youtube_channel_url = 'https://www.youtube.com/c/'+channel+'/search?query='+song
        sites.append(youtube_channel_url)

    # general Youtube search results
    for option in ['chords', 'tabs']:
        youtube_general_url = 'https://www.youtube.com/results?search_query=' + \
            song + ' ' + artist + ' ' + option
        sites.append(youtube_general_url)

    # general Utimate Guitar search results
    ug_chords = 'https://www.ultimate-guitar.com/search.php?title=' + \
        song+'&page=1&type=300'
    ug_tabs = 'https://www.ultimate-guitar.com/search.php?title=' + \
        song+'&page=1&type=200'

    sites.extend([ug_chords, ug_tabs])

    # open all these sites
    for i in sites:
        webbrowser.open(i)


# argparse setup
my_parser = argparse.ArgumentParser(
    description='Given a song and artist, opens up Youtube search results from a pre-defined list of channels and Ultimate Guitar search results for tabs & chords.',
    epilog='Keep strumming & picking! :)')

my_parser.add_argument('Song', metavar='song', type=str,
                       help='Name of the song')
my_parser.add_argument('Artist', metavar='artist', type=str,
                       help='Name of the artist')
args = my_parser.parse_args()

# call the function that will process theese command line arguments
open_results(args.Song, args.Artist)
