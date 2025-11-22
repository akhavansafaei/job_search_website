# Job Search Website

## Overview
This project is a Flask-based web application that provides an intelligent job search and posting platform. It integrates a machine learning model for automated job category prediction, offering both job seekers and employers a streamlined experience for finding and posting job opportunities.

## Related Project
This web application is built upon the NLP job classification model developed in the companion repository:
**[NLP Job Positions](https://github.com/akhavansafaei/nlp_job_positions)**

The machine learning model (`models/job_model.pkl`) was trained using the techniques and data processing pipelines developed in that project, which focuses on natural language processing for job position classification.

## Student Information
- **Student Name:** Golnaz Akbari
- **Student Number:** s3852157

## Quick Start

### Prerequisites
- Python 3.10 or higher
- pip package manager
- 4GB+ RAM (8GB recommended)
- ~2GB free disk space

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/akhavansafaei/job_search_website.git
   cd job_search_website
   ```

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

## Key Features

### For Job Seekers
- **Intelligent Search**: Search for job listings using keywords with built-in text stemming support
  - Stemming allows matching similar word forms (e.g., "work", "works", "worked" all match "work")
  - Searches both job titles and descriptions for comprehensive results
- **Job Browsing**: View the latest 5 job postings on the homepage
- **Detailed Job View**: Access complete job information including title, company, category, and full description

### For Employers
- **Two-Step Job Posting**: Streamlined job creation process
  - **Step 1**: Enter basic job information (title, company, description)
  - **Step 2**: Review and confirm AI-predicted category or manually override
- **AI-Powered Category Prediction**: Machine learning model automatically suggests job categories based on:
  - Job title using Word2Vec embeddings
  - Job description using Word2Vec embeddings
  - Combined embeddings processed through Logistic Regression classifier
- **Manual Override**: Employers can adjust the AI-suggested category if needed

### Technical Features
- **NLP Integration**: Uses NLTK for text processing and stemming
- **Word Embeddings**: Leverages Google's Word2Vec pre-trained model (word2vec-google-news-300)
- **ML Classification**: Logistic Regression model for job category prediction
- **Persistent Storage**: Jobs stored in CSV format for easy data management
- **Responsive Design**: Clean, user-friendly interface with CSS styling

## Additional Notes

### Important Setup Information
- NLTK data is automatically downloaded when the application starts (punkt tokenizer)
- The Word2Vec model (~1.6GB) is downloaded on first run and cached locally by gensim
- First startup may take several minutes due to model downloads

### System Requirements
- Minimum 4GB RAM (recommended: 8GB due to Word2Vec model size)
- ~2GB free disk space for models and data
- Python 3.10 or compatible version

### Development Notes
- The application runs in debug mode by default (`debug=True` in app.py)
- Jobs are persisted to CSV after each creation
- Unique Webindex is generated randomly (8-digit number)
- Search functionality uses Porter Stemmer for improved recall

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

## Technical Architecture

### Application Structure
The application follows the MVC (Model-View-Controller) pattern:

**Model Layer:**
- `models/job_model.pkl`: Pre-trained Logistic Regression classifier
- `data/jobs.csv`: Job listings database
- Word2Vec embeddings: Google's pre-trained word2vec-google-news-300 model

**View Layer:**
- `templates/`: Jinja2 HTML templates
  - `base.html`: Base template with navigation
  - `home.html`: Homepage with recent jobs and search
  - `job_list.html`: Search results display
  - `job_detail.html`: Individual job details
  - `create_job_step1.html`: Initial job creation form
  - `create_job_step2.html`: Category confirmation and final submission
- `static/css/style.css`: Application styling
- `static/js/script.js`: Client-side JavaScript

**Controller Layer:**
- `app.py`: Flask application with route handlers and business logic

### Machine Learning Pipeline

The application uses a sophisticated NLP pipeline for job category prediction:

1. **Text Preprocessing**
   - Tokenization using NLTK
   - Stemming with Porter Stemmer for search functionality

2. **Feature Engineering**
   - Word2Vec embeddings (300 dimensions) for job titles
   - Word2Vec embeddings (300 dimensions) for job descriptions
   - Concatenation of embeddings (600-dimensional feature vector)

3. **Classification**
   - Logistic Regression model predicts job category
   - Model trained on historical job data from the NLP Job Positions project

4. **Prediction Flow**
   ```
   Job Title + Description → Word2Vec Embeddings → Concatenate → Logistic Regression → Predicted Category
   ```

### API Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Display homepage with 5 most recent jobs |
| `/search` | POST | Search jobs by keyword with stemming |
| `/job/<webindex>` | GET | Display detailed job information |
| `/create` | GET, POST | Step 1: Enter job details |
| `/create_step2` | GET, POST | Step 2: Confirm category and save job |

### Data Schema

Jobs are stored in CSV format with the following fields:
- `Webindex`: Unique 8-digit identifier
- `Category`: Job category (e.g., Healthcare_Nursing)
- `Title`: Job title
- `Company`: Employer name
- `Description`: Full job description
- `StemmedTitle`: Stemmed version of title (for search)
- `StemmedDescription`: Stemmed version of description (for search)

## Dependencies Explained

- **Flask 3.0.3**: Web framework for routing and request handling
- **NLTK 3.8.1**: Natural language processing toolkit for text stemming
- **pandas 2.2.2**: Data manipulation and CSV operations
- **gensim 4.3.2**: Word2Vec model loading and word embeddings
- **scikit-learn 1.2.2**: Machine learning model (Logistic Regression)
- **numpy 1.25.2**: Numerical operations for embeddings

## Project Workflow

1. User visits homepage → See latest 5 jobs
2. User searches for jobs → Stemmed keyword matching in titles/descriptions
3. User clicks job → View full details
4. Employer creates job → Enter details → AI predicts category → Confirm/override → Job saved
5. New jobs appear in search results and homepage

## Screenshots & Demo

The application includes:
- A clean homepage with search functionality
- Job listing results with matched keywords highlighted through stemming
- Detailed job view pages
- Two-step job creation wizard with AI assistance
- Category prediction with manual override capability

## Future Enhancements

Potential improvements for future versions:
- User authentication and role-based access (job seekers vs. employers)
- Advanced filtering (by category, company, date posted)
- Job application tracking system
- Email notifications for job matches
- RESTful API for mobile app integration
- Database migration from CSV to PostgreSQL/MySQL
- Job recommendation system based on user preferences
- Salary range filtering and analytics

## Troubleshooting

**Word2Vec model download fails:**
- Ensure stable internet connection
- Check available disk space (~2GB needed)
- Manually download model: `python -c "import gensim.downloader as api; api.load('word2vec-google-news-300')"`

**Application crashes on startup:**
- Verify Python version (3.10+)
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
- Check if port 5000 is available

**Search returns no results:**
- Verify jobs.csv is properly formatted
- Check if stemming is working correctly
- Try broader search terms

## Acknowledgments

- Machine learning model development based on techniques from [NLP Job Positions](https://github.com/akhavansafaei/nlp_job_positions)
- Word2Vec model: Google's pre-trained word2vec-google-news-300
- Flask framework and Python NLP community

---

By following this guide, you should be able to set up and run the Job Search Website application successfully. For questions or issues, please refer to the troubleshooting section or check the related NLP Job Positions repository for model training details.