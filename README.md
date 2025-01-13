# Spreadsheet Web Application
Develop a web application that closely mimics the user interface and core functionalities  of Google Sheets, with a focus on mathematical and data quality functions, data entry,  and key UI interactions.
eatures
# 1. Spreadsheet Interface
Google Sheets-like grid using Handsontable.js.
Formula bar and toolbar for basic formatting (bold, italics, font color, etc.).
Cell dependencies and formula parsing.
Drag functionality for cells and selections.
# 2. Mathematical Functions
SUM: Calculates the sum of a range of cells.
AVERAGE: Calculates the average of a range of cells.
MAX, MIN, COUNT: Basic numerical operations.
# 3. Data Quality Functions
TRIM: Removes extra spaces from text.
UPPER, LOWER: Converts text to uppercase/lowercase.
REMOVE_DUPLICATES: Eliminates duplicate rows.
FIND_AND_REPLACE: Find and replace specific text.
# 4. Data Entry & Validation
Numeric and text input validation.
Error highlighting for invalid inputs.
# 5. Tech Stack
Frontend: Vue.js, Handsontable.js
Backend: Python Flask
Database: SQLite
Libraries: NumPy, Pandas, Handsontable.js

# requirements for the project (installation required)
flask
pandas
# 1. Clone the repository:
   git clone <repository-url>
   cd spreadsheet-webapp
# 2. Install frontend dependencies:
   cd frontend
   npm install
   npm run serve
# 3.Install backend dependencies:
    cd backend
    pip install -r requirements.txt
    python main.py
# 4. Access the application:
    The frontend runs on http://localhost:8080
    The backend runs on http://localhost:5000
# Testing
    cd backend\pytest
# Data Structures and Design Choices
   Handsontable.js: Chosen for its grid system and formula support.
   Directed Graph: Used for handling cell dependencies and recalculations.
   NumPy & Pandas: For efficient numerical computations and data cleaning
# Future Improvements (Bonus Features)
   Complex formula parsing with absolute and relative references.
   Save and load spreadsheet states.
   Data visualization with Chart.js.
# License
   This project is licensed under the MIT License.
