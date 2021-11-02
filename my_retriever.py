
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
    def TFIDF_weighted_vector(self):
        print("This is a test")
        pass

    def binary_weighted_vector(self, query):
        # dictionary with doc index as key and distance as value
        # for each term in index which is also in query
        # add docID's to a list
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

    #Returns docIDs of documents that contain words in the query.
    def docs_to_consider(self, query):
        docID_to_consider = []
        for term in query:
            term_value = self.index.get(term)
            if term_value != None:
                for data in term_value:
                    docID_to_consider.append(data)
        return set(docID_to_consider)

    def for_query(self, query):
        doc_IDs_to_consider = self.docs_to_consider(query)
        print(len(doc_IDs_to_consider))
        return list(range(1,11))








