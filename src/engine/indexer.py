from collections import defaultdict

class InvertedIndex:
    def __init__(self):

        self.index = defaultdict(lambda: defaultdict(int))
        self.doc_map = {}

    def add_document(self, doc_id, tokens, metadata):
        self.doc_map[doc_id] = metadata
        for token in tokens:
            self.index[token][doc_id] += 1