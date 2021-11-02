
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
    def tfidf_weighted_vector(self):
        print("This is a test")
        pass

    def binary_weighted_document_vectors(self, query, filtered_doc_IDs):
        document_vectors = []
        for ID in filtered_doc_IDs:
            vector = {}
            for term in self.index:
                if ID in self.index.get(term):
                    vector.update({term : 1})
                else:
                    vector.update({term : 0})
            temp_dict = {'DocID': ID, 'Data' : vector}
            document_vectors.append(temp_dict)
        return document_vectors

    def binary_weighted_query_vector(self,query):
        for query_term in query:
            vector = {}
            for index_term in self.index:
                if index_term == query_term:
                    vector.update({index_term : 1})
                else:
                    vector.update({index_term : 0})
        query_vector = ({'DocID' : 0, 'Data' : vector})
        return query_vector

    def construct_binary_query_vector(self,query, filtered_doc_IDs):
        print("For " + str(query))
        print("Constructing Documents Binary Weighted Vector... " )
        documents_vector = self.binary_weighted_document_vectors(query, filtered_doc_IDs)
        print("Constructing Query Binary Weighted Vector for... ")
        query_vector = self.binary_weighted_query_vector(query)
        print("######################################")

        pass





    def frequency_weighted_vector(self):
        pass

    def produce_query_vector(self):
        pass

    def calculate_similarity(self, query_vector):
        pass

    def calculate_tf(self):
        pass

    def calculate_df(self):
        pass

    def calculate_idf(self):
        pass

    #Returns docIDs of documents that contain words in the query.
    def filter_documents(self, query):
        docID_to_consider = []
        for term in query:
            term_value = self.index.get(term)
            if term_value is not None:
                for data in term_value:
                    docID_to_consider.append(data)
        set_of_docID_to_consider = set(docID_to_consider)
        return set_of_docID_to_consider

    def for_query(self, query):
        print("Filtering Doc IDs ...")
        filtered_doc_IDs = self.filter_documents(query)
        self.construct_binary_query_vector(query,filtered_doc_IDs)
        return list(range(1,11))








