import math
from collections import Counter

class Searcher:
    def __init__(self, index_obj):
        self.index = index_obj.index
        self.doc_map = index_obj.doc_map
        self.N = len(self.doc_map)

    def _get_idf(self, term):
        df = len(self.index.get(term, {}))
        if df == 0 or self.N == 0:
            return 0.0
        return math.log10(self.N / df)

    def rank_results(self, query_tokens):
        query_counts = Counter(query_tokens)
        query_vec = {t: tf * self._get_idf(t) for t, tf in query_counts.items()}

        scores = {}
        doc_len_sq = {}

        for term, q_weight in query_vec.items():
            if q_weight == 0:
                continue

            postings = self.index.get(term, {})
            idf = self._get_idf(term)

            for doc_id, tf in postings.items():
                d_weight = tf * idf
                scores[doc_id] = scores.get(doc_id, 0.0) + (q_weight * d_weight)
                doc_len_sq[doc_id] = doc_len_sq.get(doc_id, 0.0) + (d_weight * d_weight)

        q_len = math.sqrt(sum(w*w for w in query_vec.values())) or 1.0

        for doc_id in list(scores.keys()):
            d_len = math.sqrt(doc_len_sq.get(doc_id, 0.0)) or 1.0
            scores[doc_id] = scores[doc_id] / (q_len * d_len)

        return sorted(scores.items(), key=lambda x: x[1], reverse=True)
