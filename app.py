from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import gensim.downloader as gensim_downloader
import pickle
import random
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

# Download NLTK data
nltk.download('punkt')
ps = PorterStemmer()
def stem_text(text):
    words = word_tokenize(text)
    stemmed_words = [ps.stem(word) for word in words]
    return ' '.join(stemmed_words)

app = Flask(__name__)

# Load job data
df = pd.read_csv('data/jobs.csv')

# Load pretrained word embedding model
word_embedding_model = gensim_downloader.load('word2vec-google-news-300')

# Function to generate word embeddings
def generate_embeddings(text, model):
    words = [word for word in text.split() if word in model]
    if words:
        embedding_sum = sum(model[word] for word in words)
        return embedding_sum / len(words)
    else:
        return np.zeros(model.vector_size)

def predict_category(title, description):
    # Generate word embeddings for title and description
    title_embedding = generate_embeddings(title, word_embedding_model)
    description_embedding = generate_embeddings(description, word_embedding_model)
    
    # Concatenate title and description embeddings
    combined_embedding = np.concatenate((title_embedding, description_embedding)).reshape(1, -1)
    
    # Predict category using the loaded model
    predicted_category = model.predict(combined_embedding)[0]
    
    return predicted_category

# Load the trained model
with open('models/job_model.pkl', 'rb') as file:
    model = pickle.load(file)

def generate_unique_webindex(df):
    while True:
        webindex = random.randint(10000000, 99999999)
        if webindex not in df['Webindex'].values:
            return webindex

@app.route('/')
def home():
    # Get the last 5 records from the DataFrame and reverse the order
    last_5_jobs = df.tail(5).iloc[::-1].to_dict('records')
    return render_template('home.html', jobs=last_5_jobs)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form['keyword']
        stemmed_keyword = stem_text(keyword)
        
        # Convert Title and Description columns to strings
        df['Title'] = df['Title'].astype(str)
        df['Description'] = df['Description'].astype(str)
        
        # Apply stemming to the job titles and descriptions
        df['StemmedTitle'] = df['Title'].apply(stem_text)
        df['StemmedDescription'] = df['Description'].apply(stem_text)
        
        # Simple keyword search with stemming
        matched_jobs = df[df.apply(lambda x: stemmed_keyword in x['StemmedDescription'] or stemmed_keyword in x['StemmedTitle'], axis=1)]
        return render_template('job_list.html', jobs=matched_jobs.to_dict('records'))
    return render_template('home.html')


@app.route('/job/<int:index>')
def job_detail(index):
    job = df[df['Webindex'] == index].iloc[0]
    return render_template('job_detail.html', job=job)



@app.route('/create', methods=['GET', 'POST'])
def create_job():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        company = request.form['company']
        
        # Always predict category
        predicted_category = predict_category(title, description)

        return redirect(url_for('create_job_step2', title=title, company=company, description=description, predicted_category=predicted_category))
    
    return render_template('create_job_step1.html')

# @app.route('/create_step2', methods=['GET', 'POST'])
# def create_job_step2():
#     if request.method == 'GET':
#         title = request.args.get('title')
#         company = request.args.get('company')
#         description = request.args.get('description')
#         predicted_category = request.args.get('predicted_category')
        
#         # Debug prints to check received values
#         print("Received values in create_step2 (GET):")
#         print("Title:", title)
#         print("Company:", company)
#         print("Description:", description)
#         print("Predicted Category:", predicted_category)
        
#         return render_template('create_job_step2.html', title=title, company=company, description=description, predicted_category=predicted_category)
    
#     elif request.method == 'POST':
#         title = request.form['title']
#         company = request.form['company']
#         description = request.form['description']
#         category = request.form['category']
        
#         webindex = generate_unique_webindex(df)

#         # Debug prints to check received values
#         print("Received values in create_step2 (POST):")
#         print("Title:", title)
#         print("Company:", company)
#         print("Description:", description)
#         print("Category:", category)
        
#         new_job = {
#             'Webindex': webindex,
#             'Category': category,
#             'Title': title,
#             'Company': company,
#             'Description': description
#         }
#         df.loc[len(df)] = new_job
#         df.to_csv('data/jobs.csv', index=False)
        
#         # Debug print to confirm new job addition
#         print("New job added:", new_job)
#         print("Total jobs in DataFrame:", len(df))
        
#         return redirect(url_for('job_detail', index=len(df) - 1))
@app.route('/create_step2', methods=['GET', 'POST'])
def create_job_step2():
    if request.method == 'GET':
        title = request.args.get('title')
        company = request.args.get('company')
        description = request.args.get('description')
        predicted_category = request.args.get('predicted_category')
        
        # Debug prints to check received values
        print("Received values in create_step2 (GET):")
        print("Title:", title)
        print("Company:", company)
        print("Description:", description)
        print("Predicted Category:", predicted_category)
        
        return render_template('create_job_step2.html', title=title, company=company, description=description, predicted_category=predicted_category)
    
    elif request.method == 'POST':
        title = request.form['title']
        company = request.form['company']
        description = request.form['description']
        category = request.form['category']
        
        webindex = generate_unique_webindex(df)

        # Debug prints to check received values
        print("Received values in create_step2 (POST):")
        print("Title:", title)
        print("Company:", company)
        print("Description:", description)
        print("Category:", category)
        
        new_job = {
            'Webindex': webindex,
            'Category': category,
            'Title': title,
            'Company': company,
            'Description': description
        }
        df.loc[len(df)] = new_job
        df.to_csv('data/jobs.csv', index=False)
        
        # Debug print to confirm new job addition
        print("New job added:", new_job)
        print("Total jobs in DataFrame:", len(df))
        
        return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)

