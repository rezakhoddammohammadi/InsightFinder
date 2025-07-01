"""
Downloads necessary NLTK data files for the InsightFinder project.
"""

import nltk

print("Downloading required NLTK resources...")
nltk.download('punkt')
nltk.download('stopwords')

# Confirm one of the resources is available
print("NLTK 'punkt' tokenizer path:", nltk.data.find('tokenizers/punkt'))
