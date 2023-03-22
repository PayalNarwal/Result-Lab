# RESULT LAB

# Introduction

The Result Lab is a project designed to help the examination department of a college manage student details and marks easily. This system allows for easy data entry, retrieval, and management of student information, course details, and exam results.

# Features

- **Easy data entry**: The system allows for easy input of student details, course information, and exam results.
- **Quick retrieval of information**: The system provides a way to retrieve student information, course details, and exam results in a table format.
- **Marks analysis**: The system provides a way to analyse student marks course-wise, student-wise as well as all together.

# Technologies

- Python 3.11.2
- SQL
- Python Modules:
    - tkinter
    - sqlite3
    - matplotlib
    - pillow

# How to Use

## Dashboard

Dashboard is the main window which opens when the code is run. It consists of various buttons which direct you to the required sub-window. 

### Course

- This sub-window stores information about each course.
- Entry Fields: These entries get stored in the database in the “Course Table”.
    
    
    | COURSE NAME |
    | --- |
    | DURATION |
    | BRANCH |
    | DESCRIPTION |
- Buttons:
    
    
    | SAVE | Saves data to the database |
    | --- | --- |
    | UPDATE | Updates the data present in database |
    | DELETE | Deletes the data from database |
    | CLEAR | Clears the entry fields |
- Search Panel:
    
    It is used to read the details present in a specific course.
    

### Student Details

- This sub-window stores information about individual student.
- Entry Fields: These entries get stored in the database in the “Student Table”.
    
    
    | ROLL NO. |
    | --- |
    | DATE OF BIRTH |
    | NAME |
    | CONTACT |
    | EMAIL |
    | ADMISSION YEAR |
    | MOTHER’S NAME |
    | FATHER’S NAME |
    | COURSE |
    | BRANCH |
- Drop Box: This helps in restricting the possible entries.
    
    
    | GENDER |
    | --- |
    | COURSE |
- Buttons:
    
    
    | SAVE | Saves data to the database |
    | --- | --- |
    | UPDATE | Updates the data present in database |
    | DELETE | Deletes the data from database |
    | CLEAR | Clears the entry fields |
- Search Panel:
    
    It is used to read the details present in a specific Roll Number.
    

### Exam Details

- This sub-window stores information about exam details.
- Entry Fields:
    
    
    | ROLL NO. |
    | --- |
    | NAME |
    | SEMESTER |
    | SUB 1 |
    | SUB 2 |
    | SUB 3 |
    | SUB 4 |
    | SUB 5 |
    | SUB 6 |
- Drop Box:
    
    
    | COURSE |
    | --- |
    | EXAM |
- Buttons:
    
    
    | SAVE | Saves data to the database |
    | --- | --- |
    | UPDATE | Updates the data present in database |
    | DELETE | Deletes the data from database |
    | CLEAR | Clears the entry fields |
- Search Panel:
    
    It is used to read the details present in a specific Roll Number.
    

### Upload Marks

- It is used to upload marks of each individual from different courses.
- Drop Box:
    
    
    | ROLL NUMBER |
    | --- |
- Search Panel:
    
    It is used to read the name of the individual.
    
- Entry Fields:
    
    
    | READ ONLY | NAME  |
    | --- | --- |
    | READ ONLY | COURSE |
    | READ ONLY | SUB 1 |
    | READ ONLY | SUB 2 |
    | READ ONLY | SUB 3 |
    | READ ONLY | SUB 4 |
    | READ ONLY | SUB 5 |
    | READ ONLY | SUB 6 |
    | SUBJECT 1/2/3/4/5/6 | MARKS OBTAINED |
    | SUBJECT 1/2/3/4/5/6 | MAXIMUM MARKS |
- Buttons:
    
    
    | OBTAINED MARKS | Calculates the total obtained marks |
    | --- | --- |
    | TOTAL MARKS | Calculates the total marks |
    | PERCENTAGE | Calculates the percentage |
    | SAVE | Saves data to the database |
    | UPDATE | Updates the data present in database |
    | DELETE | Deletes the data from database |
    | CLEAR | Clears the entry fields |

### Student Report

- It is a report card which displays each individual’s scores and analysis.
- Search Panel:
    
    It is used to read the details present in a specific Roll Number.
    
- Entry Fields:
    
    
    | READ ONLY | NAME |
    | --- | --- |
    | READ ONLY | COURSE |
    | READ ONLY | BRANCH |
    | READ ONLY | D.O.B |
    | READ ONLY | MOTHER’S NAME |
    | READ ONLY | FATHER’S NAME |
    | READ ONLY | MARKS OBTAINED |
    | READ ONLY | TOTAL PERCENTAGE |
- Graph:
    - A bar graph depicting marks obtained in each subject by the individual.
- Buttons:
    
    
    | CLEAR | Clears the entry fields |
    | --- | --- |

### Course Report

- It is the analysis of the performance of the students in a particular course.
- Search Panel:
    
    It is used to read the details present in a specific Roll Number.
    
- Entry Fields:
    
    
    | READ ONLY | TOTAL CANDIDATES |
    | --- | --- |
    | READ ONLY | CANDIDATES PASSED |
    | READ ONLY | CANDIDATES FAILED |
    | READ ONLY | AVERAGE MARKS |
    | READ ONLY | HIGHEST MARKS |
    | READ ONLY | LOWEST MARKS |
- Buttons:
    
    
    | CLEAR | Clears the entry fields |
    | --- | --- |

# Team - Oopsie here :)

This project was successfully developed by the contribution of the following team members:

- Payal Narwal (CSE-AI , 2026)
- Shatakshi Bansal (CSE-AI , 2026)
- Prachi Verma (CSE-AI , 2026)

