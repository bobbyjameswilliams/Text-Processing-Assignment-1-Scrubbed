
class Retrieve:
    
    # Create new Retrieve object storing index and term weighting 
    # scheme. (You can extend this method, as required.)
    def __init__(self,index, term_weighting):
        self.index = index
        self.term_weighting = term_weighting
        self.num_docs = self.compute_number_of_documents()
        if self.term_weighting == 'binary':
            print("Constructing Documents Binary Weighted Vector... ")
            #make a dictionary of docs
            self.document_vector = self.binary_weighted_document_vectors()


    def compute_number_of_documents(self):
        self.doc_ids = set()
        for term in self.index:
            self.doc_ids.update(self.index[term])
        return len(self.doc_ids)


    def calculate_cosine_distance(self, filtered_doc_IDs, query_vector):
        results = {}
        for id in filtered_doc_IDs:
            sigma_qd = 0
            sigma_d_sqrd = 0

            for term in self.document_vector[id]:
                if term not in self.document_vector[id]:
                    document_term = 0
                else:
                    document_term = self.document_vector[id][term]

                if term not in query_vector[0]:
                    query_term = 0
                else:
                    query_term = query_vector[0][term]

                sigma_qd += (document_term) * (query_term)
                sigma_d_sqrd += (document_term ** 2)

            similarity = sigma_qd/(sigma_d_sqrd ** 0.5)

            results.update({id : similarity})
        sorted_results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1], reverse= True)}
        return sorted_results


    # Method performing retrieval for a single query (which is
    # represented as a list of preprocessed terms). Returns list 
    # of doc ids for relevant docs (in rank order).

    def binary_weighted_document_vectors(self):
        document_vectors = {}
        for doc_id in self.doc_ids:
            vector = {}
            for term in self.index:
                if doc_id in self.index[term]:
                    vector.update({term : 1})
            document_vectors.update({doc_id : vector})
        return document_vectors

    def binary_weighted_query_vector(self,query):
        vector = {}
        for query_term in query:
            vector.update({query_term : 1})
        query_vector = ({0 : vector})
        return query_vector


### FREQUENCY WEIGHTED

    def frequency_weighted_vector(self):
        pass

    def produce_query_vector(self):
        pass


### TFIDF
    def tfidf_weighted_vector(self):
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
        if self.term_weighting == 'binary':
            print("For " + str(query))
            print("Constructing Query Binary Weighted Vector")
            query_vector = self.binary_weighted_query_vector(query)
            print("######################################")
            processed_results = self.calculate_cosine_distance(filtered_doc_IDs, query_vector)
            return list(processed_results.keys())
        else:
            print("Something went wrong...")

