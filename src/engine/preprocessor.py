import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


class Preprocessor:
    def __init__(self):
        self.stopwords = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()

    def tokenize(self, html_content, use_stemming):
        soup = BeautifulSoup(html_content, 'html.parser')
        title_tag = soup.title.string if soup.title else ""

        if not title_tag or title_tag.lower().strip() in ["player profile", "index", "home"]:
            h1_tag = soup.find('h1')
            title_text = h1_tag.get_text() if h1_tag else ""
        else:
            title_text = title_tag

        body_text = soup.get_text(separator=' ')

        def process_field(text):
            text = text.lower()
            tokens = re.findall(r'\b\w+\b', text)
            tokens = [t for t in tokens if t not in self.stopwords]
            if use_stemming:
                tokens = [self.stemmer.stem(t) for t in tokens]
            return tokens

        return process_field(title_text), process_field(body_text)