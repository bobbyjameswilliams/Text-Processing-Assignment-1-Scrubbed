import math


class Retrieve:

    # Create new Retrieve object storing index and term weighting 
    # scheme. (You can extend this method, as required.)
    def __init__(self, index, term_weighting):
        self.index = index
        self.term_weighting = term_weighting
        self.num_docs = self.compute_number_of_documents()
        # these indexes and boolean are used in the creation of the TFIDF index.
        self.df_index = {}
        self.idf_index = {}
        self.tf_index = {}

        # Prints to console what weighting is being produced.
        print("Constructing Documents " + self.term_weighting.upper() + " Weighted Vector... ")

        # make a dictionary of docs
        if self.term_weighting == 'tfidf':
            #TFIDF requires more global helper indexes.
            self.df_index = self.create_df_index()
            self.idf_index = self.create_idf_index()
            self.tf_index = self.weighted_document_vectors()
            self.document_vector = self.weighted_document_vectors()

        else:
            self.document_vector = self.weighted_document_vectors()

    def compute_number_of_documents(self):
        self.doc_ids = set()
        for term in self.index:
            self.doc_ids.update(self.index[term])

        return len(self.doc_ids)

### MAIN FUNCTIONS ###

    # Returns docIDs of documents that contain words in the query.
    def filter_documents(self, query):
        docID_to_consider = []
        for term in query:
            term_value = self.index.get(term)
            if term_value is not None:
                for data in term_value:
                    docID_to_consider.append(data)
        set_of_docID_to_consider = set(docID_to_consider)

        return set_of_docID_to_consider

    # Used to calculate cosine distance for all weightings. Returns the results as a sorted list of document indexs
    # based on their similarity score.
    def calculate_cosine_distance(self, filtered_doc_IDs, query_vector):
        results = {}
        for id in filtered_doc_IDs:
            sigma_qd = 0
            sigma_d_sqrd = 0

            for term in self.document_vector[id]:
                document_term = self.document_vector[id][term]

                if term in query_vector:
                    query_term = query_vector[term]
                else:
                    query_term = 0

                sigma_qd += (document_term) * (query_term)
                sigma_d_sqrd += (document_term ** 2)

            similarity = sigma_qd / (sigma_d_sqrd ** 0.5)

            results.update({id: similarity})
        sorted_results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1], reverse=True)}

        return sorted_results

    # Main function for creating document vectors. Creates different ones based on the selected term weighting.
    def weighted_document_vectors(self):
        if self.term_weighting == 'binary':
            print("Producing Binary Weighted Document Vector...")
        elif self.term_weighting == 'tf':
            print("Producing TF Weighted Document Vector...")
        document_vectors = {}
        for doc_id in self.doc_ids:
            vector = {}
            for term in self.index:
                if doc_id in self.index[term]:
                    if self.term_weighting == 'binary':
                        vector.update({term: 1})
                    # for TFIDF, on the first pass the TF index is created as this is needed for TDFIDF
                    elif self.term_weighting == 'tf' or (self.term_weighting == 'tfidf' and self.tf_index == {}):
                        vector.update({term: self.index[term][doc_id]})
                    # Once TF index is created, TFIDF index is created.
                    elif self.term_weighting == 'tfidf' and self.tf_index != {}:
                        term_tf = self.tf_index[doc_id][term]
                        term_idf = self.idf_index[term]
                        tfidf = term_tf * term_idf
                        vector.update({term: tfidf})

            document_vectors.update({doc_id: vector})

        return document_vectors

    ### QUERY VECTORS ###.

    def binary_weighted_query_vector(self, query):
        query_vector = {}
        for query_term in query:
            query_vector.update({query_term: 1})

        return query_vector

    def tf_query_vector(self, query):
        query_vector = {}
        for query_term in query:
            if query_term in query_vector:
                newcount = query_vector[query_term] + 1
                query_vector.update({query_term: newcount})
            else:
                query_vector.update({query_term: 1})

        return query_vector

    def tfidf_query_vector(self, query):
        tf_query_vector = self.tf_query_vector(query)
        query_vector = {}
        for query_term in query:
            if query_term in self.index:
                term_tf = tf_query_vector[query_term]
                term_idf = self.idf_index[query_term]
                tfidf = term_tf * term_idf
                query_vector.update({query_term: tfidf})

        return query_vector

    ### TFIDF HELPER INDEXES ###

    def create_df_index(self):
        dictionary = {}
        for term in self.index:
            dictionary.update({term: len(self.index[term])})
        return dictionary

    # Creates it in one pass at the beginning for reference later
    def create_idf_index(self):
        dictionary = {}
        for term in self.df_index:
            df = self.df_index[term]
            prelog_idf = (self.num_docs / df)
            idf = math.log10(prelog_idf)
            dictionary.update({term: idf})
        return dictionary

    def for_query(self, query):
        print("Filtering Doc IDs ...")
        filtered_doc_IDs = self.filter_documents(query)
        print("For " + str(query))
        if self.term_weighting == 'binary':
            print("Constructing Query Binary Weighted Vector")
            query_vector = self.binary_weighted_query_vector(query)
            print("######################################")
            processed_results = self.calculate_cosine_distance(filtered_doc_IDs, query_vector)
            return list(processed_results.keys())
        elif self.term_weighting == 'tf':
            print("Constructing Query Frequency Weighted Vector")
            query_vector = self.tf_query_vector(query)
            print("######################################")
            processed_results = self.calculate_cosine_distance(filtered_doc_IDs, query_vector)
            return list(processed_results.keys())
        elif self.term_weighting == 'tfidf':
            print("Constructing Query TFIDF Weighted Vector")
            query_vector = self.tfidf_query_vector(query)
            print("######################################")
            processed_results = self.calculate_cosine_distance(filtered_doc_IDs, query_vector)
            return list(processed_results.keys())


        else:
            print("Something went wrong...")
