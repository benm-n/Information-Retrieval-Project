from collections import defaultdict

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(lambda: defaultdict(float))
        self.doc_map = {}

    def add_document(self, doc_id, tokens, metadata=None, weight=1.0):
        if metadata is not None:
            self.doc_map[doc_id] = metadata

        for token in tokens:
            self.index[token][doc_id] += weight
