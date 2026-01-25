import re
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

class Preprocessor:
    def __init__(self):
        self.stopwords = stopwords.words('english')

    def tokenize(self, html_content):
        # Extract text from HTML tags
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text(seperator=' ')

        # text normalization and Regex tokenization
        text = text.lower()
        tokens = re.findall(r'\b\w+\b', text)

        # Remove stopwords for cleaner indexing
        return [token for token in tokens if token not in self.stopwords]



