# University Report Entry

Run **`python3 program.py`** in the same directory as the program file, `input.txt` file and the `chromedriver` after replacing the login credentials.

---

- Fills up entries for MAKAUT reports.
- Saved a lot of time for 6 subjects x 8 entries each.
- Does everything from login to multiple report entries automatically, except the input for choosing faculty & datetime.
- Needs login credentials and an input file with the following headers. Check the `input.txt` file for more on the format. The report details should be on new lines delimited by `;`  
  `Topic Platform Link Duration Post_Class AS AR Test Activity Remarks Week_No`
- **TODOS**:  
   [] Add CSV support  
   [] Fix the input for faculty & datetime  
   [] Find solution for `time.sleep()`  
   [] Figure out better input file solution
