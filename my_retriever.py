
class Retrieve:
    
    # Create new Retrieve object storing index and term weighting 
    # scheme. (You can extend this method, as required.)
    def __init__(self,index, term_weighting):
        self.index = index
        self.term_weighting = term_weighting
        self.num_docs = self.compute_number_of_documents()
        
    def compute_number_of_documents(self):
        self.doc_ids = set()
        for term in self.index:
            self.doc_ids.update(self.index[term])
        return len(self.doc_ids)

    # Method performing retrieval for a single query (which is 
    # represented as a list of preprocessed terms). Returns list 
    # of doc ids for relevant docs (in rank order).
    def for_query(self, query):
        for word in self.index:
            value = word.value
        return list(range(1,11))

    def TFIDF_weighted_vector(self):
        pass

    def binary_weighted_vector(self):

        pass

    def frequency_weighted_vector(self):
        pass

    def produce_query_vector(self):
        pass

    def calculate_similarity(self, query_vector):
        pass

    def calculate_TF(self):
        pass

    def calculate_DF(self):
        pass

    def calculate_IDF(self):
        pass






