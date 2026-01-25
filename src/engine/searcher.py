import math
from collections import Counter

class Searcher:
    def __init__(self, index_obj):
        self.index = index_obj.index
        self.doc_map = index_obj.doc_map
        self.N = len(self.doc_map)

    def _get_idf(self, term):
        df = len(self.index.get(term, {1}))
        if df == 0:
            return 0
        return math.log10(self.N / df)

    def rank_results(self, query_tokens):
        # calculating tf * idf for query
        query_counts = Counter(query_tokens)
        query_vec = {t: count * self._get_idf(t) for t, count in query_counts.items()}

        scores = {} # Document ID : Dot Product Score

        # calculating weights and similarity
        for term, q_weight in query_vec.items():
            if q_weight == 0:
                continue

            postings = self.index.get(term, {})
            for doc_id, tf in postings.items():
                d_weight = tf * self._get_idf(term)
                scores[doc_id] = scores.get(doc_id, 0) + (q_weight * d_weight)

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return ranked