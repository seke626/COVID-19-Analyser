# COVID-19-Analyser

COVID-19 Analyzer is a web application built with Django that allows users to upload CSV files containing COVID-19 data, perform data analysis, and visualize the data using Matplotlib. Users can register, log in, and save their analysis results for future reference.

**Features**

 - User registration and authentication.
 - Upload CSV files containing COVID-19 data.
 - Perform data analysis using Pandas to calculate statistics and trends.
 - Visualize data using Matplotlib to create charts and graphs.
 - Save analysis results to the database for registered users.

Installation

Clone the repository:
`git clone https://github.com/your-username/COVID-19-Analyzer.git`

Navigate to the project directory:
`cd COVID-19-Analyzer`

Install dependencies:
`pip install -r requirements.txt`

Run migrations:
`python manage.py migrate`

Start the development server:
`python manage.py runserver`

Access the application at http://localhost:8000

**Usage**

 - Register for a new account or log in if you already have one.
 - Upload a CSV file containing COVID-19 data.
 - View analysis results and visualizations.
 - Save analysis results for future reference.

**Technologies Used**

 - Python
 - Django
 - Pandas
 - Matplotlib
