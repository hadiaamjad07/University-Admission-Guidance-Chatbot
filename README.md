# 🎓 University Admission Guidance Chatbot

##  Overview

This project is a University Admission Guidance Chatbot built using Python and Streamlit.

It helps students get information about universities, scholarships, admissions, degree programs, and higher education opportunities.

The chatbot uses web scraping to collect educational content from multiple websites and then provides answers based on that dataset.



##  Features

* 🌐 Web scraping from educational websites
* 📚 Dataset creation from online educational sources
* 🎓 University admission guidance
* 💰 Scholarship information support
* 💬 Interactive Streamlit web interface
* ⚡ Fast keyword-based response system
* 📖 Higher education information for students



##  Technologies Used

* Python 🐍
* Streamlit
* BeautifulSoup (bs4)
* Requests
* Regular Expressions (re)



##  Project Structure

University-Admission-Guidance-Chatbot/

│

├── app.py # Streamlit chatbot UI

├── web_scraper.py # Web scraping script

├── training_data.txt # Collected dataset

├── requirements.txt # Required libraries

├── README.md # Project documentation



##  How It Works

### 1️⃣ Data Collection

* Scrapes text from educational websites
* Extracts useful paragraphs
* Stores cleaned data in training_data.txt

### 2️⃣ Processing

* Splits text into sentences
* Matches user input with dataset keywords
* Finds the most relevant answers

### 3️⃣ Output

* Displays relevant information in chatbot format
* Provides admission and scholarship guidance



## ▶️ How to Run

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run Scraper

```bash
python web_scraper.py
```

### Step 3: Run Chatbot

```bash
python -m streamlit run app.py
```

### Step 4: Open Browser

```text
http://localhost:8501
```



##  Example Questions

* What is a university?
* What is higher education?
* What is a scholarship?
* What are degree programs?
* How does university admission work?



##  Limitations

* Does not use a deep learning model
* Works primarily on keyword matching
* Depends on scraped data quality
* Limited to information available in the dataset



##  Future Improvements

* Add AI/NLP-based responses
* Improve answer accuracy
* Add ChatGPT-style interface
* Support multiple university databases
* Deploy online using Streamlit Cloud
* Add voice interaction support



##  Author

* Student Project – University Admission Guidance Chatbot
* Built for learning purposes (Python + Web Scraping + Streamlit)

