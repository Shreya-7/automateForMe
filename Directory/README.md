# Directory Rename & Cleanup

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
