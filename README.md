This repository contains programs I created to automate a few simple everyday tasks which otherwise take up a lot of time for me. Currently, it has 4 kinds of activities it automates:

- Course Search
- Directory Rename & Cleanup
- University Report Entry
- Job Search

## **Course Search**:

- Opens search results from a variety of educational course websites for a particular topic with a filter applied for free courses.
- Prevents a lot of hassle when trying to quickly find available course options.
- **Websites currently supported**: Coursera, Udemy, Udacity, edX, freeCodeCamp, Codecademy, Khan Academy, Academic Earth, Alison
- Run **`python3 courses.py topic`** in the same directory as the program file.
- **TODOS**:  
   [] Add more websites  
   [] Add support for multiple topics at one go  
   [] Add support for setting filters

## **University Report Entry**:

- Fills up entries for MAKAUT reports.
- Saved a lot of time for 6 subjects x 8 entries each.
- Does everything from login to multiple report entries automatically, except the input for choosing faculty & datetime.
- Needs login credentials and an input file with the following headers. The report details should be on new lines delimited by `;`  
  `Topic Platform Link Duration Post_Class AS AR Test Activity Remarks Week_No`
- Run **`python3 program.py`** in the same directory as the program file, `input.txt` file and the `chromedriver` after replacing the login credentials.
- **TODOS**:  
   [] Add CSV support  
   [] Fix the input for faculty & datetime  
   [] Find solution for `time.sleep()`  
   [] Figure out better input file solution

## **Directory Rename & Cleanup**:

- Created to make uniform names for folders and files associated with downloaded movies and TV shows.
- It has two parts - one for movies and one for TV shows
- Quick way to make folders and files neat
- for **Movies**:
  - The root folder for the movie containing the video file + optional subtitles and images should be renamed to the desired name.
  - The video and subtitles files are given the same name to support devices that require it.
  - **Functions**:
    - Renames the video file and subtitle files with the name of the root folder
    - Deletes irrelevant images usually downloaded by torrent engines
    - Indicates if the movie has a subtitle file downloaded or not.
  - Run **`python3 Movies.py`**. The program file should be placed in the parent directory of this root folder.
  - **TODOS**:  
     [] Take path input for folder  
     [] Extract movie name & year to create default rename template  
     [] Add subtitle file download automatically if not present
- for **TV Shows**:
  - Renames video + optional subtitles files based on the episode number extracted.
  - **TODOS**:  
     [] Extract episode names from wiki based on show name  
    [] Add subtitle file download automatically if not present  
    [] Group episode video and subtitle into sub-folders

## **Job Search**:

- Opens search results from a variety of job sites + company websites with a pre-set of filters.
- Segregates between sites you may open for daily/weekly updates and those for only when you ask.
- Run **`python3 jobs.py`** in the same directory as the program file.
- **TODOS**:  
   [] Add more websites  
   [] Add support for setting filters  
   [] Add more categories  
   [] Add web scraping and UI to display results
