# Ranked Information Retrieval System — Vector Space Model (TF-IDF)

## Overview
This project implements a ranked search engine using the Vector Space Model (VSM) with TF-IDF weighting. Documents and queries are converted into weighted vectors and ranked using dot-product similarity.

The system supports keyword and named-entity queries and returns results ordered by estimated relevance.

---

## Requirements

Python 3.10 or newer is recommended.

Install required packages:

```bash
pip install -r requirements.txt
```

Dependencies:

```
beautifulsoup4==4.14.3
nltk==3.9.2
regex==2026.1.15
```

---

## NLTK Setup  

The system should automatically download required NLTK data files, which may take 1-3 minutes on first run.
If this fails,
Run once before using the system:

```bash
python -m nltk.downloader punkt stopwords
```

---

## Project Structure

```
data/              document collection
main.py            main program (builds vectors and runs search)
requirements.txt
README.md
```

Place your document corpus inside the `data/` folder.

---

## How To Run

From the project root directory, run:

```bash
python main.py
```

The program will automatically:

- load the document collection
- preprocess and tokenize text
- compute TF-IDF weights
- build document vectors
- accept a user query
- compute similarity scores
- output ranked results


---

## Example Queries

```
Placente, Diego
Defender
Fast left sided defender
```

---

## Notes

- Queries are processed using the same preprocessing pipeline as documents.
- Ranking is based on TF-IDF weighted vector similarity.
- Results are displayed in descending similarity score order.

---

## License
This project is licensed under the MIT License.

---

## Author

Ben Maddison
