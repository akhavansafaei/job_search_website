# Job Search Website

## Description
This project is a web-based job search application built using Flask. It allows users to search for job listings, create new job listings, and view detailed information about each job. A machine learning model trained in Milestone I is integrated to recommend job categories based on job descriptions and titles.

## Student Information
- **Student Name:** Golnaz Akbari
- **Student Number:** s3852157
- **link:

## Dependencies
- Python 3.10
- Flask 3.0.3
- NLTK 3.8.1
- pandas 2.2.2
- gensim 4.3.2
- scikit-learn 1.2.2

## Instructions to Run the Code
1. **Clone the repository from GitHub:**


2. **Set up a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install the required dependencies using pip:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```
   python app.py
   ```

5. **Open a web browser and navigate to** `http://localhost:5000` **to access the application.**

## File Structure
```
job_search_website/
├── app.py                   # Main Flask application file
├── templates/               # Directory containing HTML templates
│   ├── base.html
│   ├── home.html
│   ├── job_list.html
│   ├── job_detail.html
│   ├── create_job.html
│   ├── create_job_step1.html
│   ├── create_job_step2.html
├── static/                  # Directory containing static files (e.g., CSS, JavaScript)
│   ├── css/
│   │   └── style.css
│   ├── js/
│       └── script.js
├── models/                  # Directory containing trained machine learning models
│   └── job_model.pkl
└── data/                    # Directory containing job data CSV file
    └── jobs.csv
```

##Functionalities
* For Job Seekers:
- Job Search: Allows job seekers to search for job listings by keyword. The search supports similar forms of keywords (e.g., "work", "works", "worked").
- Job Detail: View detailed information about each job listing by clicking on a job ad preview.
* For Employers:
- Create New Job Listing: Employers can create new job listings with information such as title, description, and company name. A machine learning model recommends job categories based on the job description and title. Employers can override the recommended categories.

## Additional Notes
- Make sure to have NLTK data downloaded by running `nltk.download('punkt')` before running the application for the first time. (already included in app.py so no action is needed)
- For any issues or feedback, please contact [Your Email Address].

## Setting Up Virtual Environment (Optional but Recommended)
To keep your dependencies isolated, you can set up a virtual environment:

1. Navigate to your project directory:
   ```
   cd C:\Users\YourUsername\Documents\job_search_website
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

## Code Explanation
The main application logic is contained in `app.py`, which defines the Flask routes and handles user interactions:

### Routes
- **Home (`/`):** Displays the last 5 job postings.
- **Search (`/search`):** Allows users to search for job listings by keyword.
- **Job Detail (`/job/<int:index>`):** Displays detailed information about a specific job.
- **Create Job (`/create` and `/create_step2`):** Allows users to create new job listings in a two-step form.

### Templates
The HTML templates are located in the `templates` directory and are used to render the web pages.

### Static Files
The static files (CSS and JavaScript) are located in the `static` directory.

### Data and Models
- **Data (`data/jobs.csv`):** Contains job listings data.
- **Model (`models/job_model.pkl`):** Contains the trained machine learning model for job category prediction.

By following this guide, you should be able to set up and run the Job Search Website application successfully.