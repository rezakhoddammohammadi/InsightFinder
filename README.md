# InsightFinder

InsightFinder is a Python-based tool for analyzing email communication patterns from Gmail `.mbox` exports. It helps professionals understand who they contact most, when they’re most active, and what topics dominate their conversations.

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
