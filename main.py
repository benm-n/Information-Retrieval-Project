import sys
import os

# Ensure the 'src' folder is reachable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("Loading Components...")
from src.engine.preprocessor import Preprocessor
from src.engine.indexer import InvertedIndex
from src.engine.searcher import Searcher

print("Components Loaded Successfully.")

def main():
    print("Checking for stopwords...")
    import nltk
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("Downloading required NLTK resources...")
        nltk.download('stopwords', quiet=True)

    prep = Preprocessor()
    index = InvertedIndex()
    data_path = "data/Soccer/"

    for filename in os.listdir(data_path):
        if filename.endswith(".html"):
            with open(os.path.join(data_path, filename), 'r', encoding='utf-8', errors='ignore') as f:
                title_tokens, body_tokens = prep.tokenize(f.read(), use_stemming=True)
                index.add_document(filename, title_tokens, metadata=filename, weight=2.0)
                index.add_document(filename, body_tokens, metadata=filename, weight=1.0)

    searcher = Searcher(index)

    print("Type 'quit' to exit.")

    while True:
        query = input("\nEnter search query: ").strip()

        if query.lower() == 'quit':
            break

        # Process query exactly like the documents
        title_tokens,body_tokens = prep.tokenize(query, use_stemming=True)
        query_tokens = title_tokens + body_tokens
        results = searcher.rank_results(query_tokens)

        if not results:
            print("No matches found.")
        else:
            print(f"\nTop Results for '{query}':")
            for doc_id, score in results[:5]:
                print(f"[{score:.4f}] - {doc_id}")


if __name__ == "__main__":
    main()