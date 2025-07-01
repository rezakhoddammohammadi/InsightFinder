# InsightFinder

InsightFinder is a Python-based email analysis tool designed for `.mbox` files (like Gmail exports). It helps you explore communication patterns, most frequent contacts, and common keywords in your email data.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)

## Features

- 📂 Analyze Gmail `.mbox` email export files
- 📊 Visualize email activity by sender and by day
- 🔤 Extract most common words using NLP
- 🧪 Includes unit tests for key modules
- 📈 Simple charts using matplotlib

## Project Structure
InsightFinder/
├── data/ # Raw input email files (.mbox)
├── src/ # Source code modules
├── tests/ # Unit and functional tests
├── notebooks/ # Jupyter notebooks (optional)
├── app.py # Flask API entry point
├── main.py # Script for CLI-based analysis
└── README.md

## Installation

Make sure Python 3.8+ is installed, then:

```bash
pip install -r requirements.txt
python src/download_nltk_data.py


##  Run Tests 
set PYTHONPATH=.
pytest

##  Run API Locally
python app.py
Then use test_api.py to send a .mbox file to:
http://127.0.0.1:5000/analyze


📷 Sample Output
Emails per sender
Emails per day
Top keywords
Bar chart (matplotlib)

📄 License
This project is licensed under the MIT License.

