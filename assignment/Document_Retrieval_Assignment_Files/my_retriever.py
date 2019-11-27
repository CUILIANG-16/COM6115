import math


class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self, index, termWeighting):
        self.index = index
        self.termWeighting = termWeighting
        self.docLength = self.__getDocLength() # Compute the total number of documents in the collection
        # Computed the value of idf, generated a dictionary with key as docid and value as idf
        if self.termWeighting == 'tfidf':
            self.idf = {term: math.log10(
                self.docLength / len(docid_dict)) for term, docid_dict in self.index.items()}
        self.docMode = self.__getDocMode() # Compute the size of each document vector

    # Compute the total number of documents in the collection
    def __getDocLength(self):
        '''Compute the total number of documents in the collection.

        Get the largest document id from a 2-level dictionary traversal

        Args:
            max_index: Store maximum document id as variable.
            present_term: Get the dictionary corresponding to the current term.

        Returns:
            An integer
        '''
        max_index = 0 # the number of maximum document id
        for term in self.index:
            present_term = max(self.index[term])
            max_index = present_term if present_term > max_index else max_index
        return max_index

    # Compute the size of each document vector
    def __getDocMode(self):
        '''Compute the size of each document vector.

        Iterate through each item in the index and add the square of the frequency
        to the file ID corresponding to the dictionary. If it is in binary mode,
        accumulate 1; in TF mode, accumulate frequency; in TFIDF, first multiply
        the frequency by the idf corresponding to the current term, and then
        accumulate.

        Args:
            doc_mode: A dictionary to store the length of each document, where the
                key is the document id and the value is the size of the corresponding
                document.

        Returns:
            A dictionary where the key is the docid and value is the corresponding
            vector length.
            For example:

            {1: 5.4218639897298155,
             2: 6.046778468200997,
             3: 4.337707805638354,
             ...}
             
        Raises:
            NameError: An error occurres when math package is not imported.
        '''
        doc_mode = dict().fromkeys(range(1, self.docLength + 1), 0) # Pre-created dictionary to store the length of each document, default value is 0
        if self.termWeighting == 'tf':
            for term, docid_dict in self.index.items():
                for docid, freq in docid_dict.items():
                    doc_mode[docid] += freq * freq # Cumulative frequency squared
        elif self.termWeighting == 'binary':
            for term, docid_dict in self.index.items():
                for docid, freq in docid_dict.items():
                    doc_mode[docid] += 1 # Cumulative binary
        elif self.termWeighting == 'tfidf':
            for term, docid_dict in self.index.items():
                idf = self.idf[term]
                for docid, freq in docid_dict.items():
                    doc_mode[docid] += freq * idf * freq * idf # Cumulative TF-IDF squared
        for docid, accu in doc_mode.items():
            doc_mode[docid] = math.sqrt(accu)
        return doc_mode

    # Method performing retrieval for specified query
    def forQuery(self, query):
        '''Find the top 10 documents that are most relevant to the current query.

        Args:
            sellected_index: Filter the dictionary containing the term in query
                from index. It is a subset of the index dictionary.
            com_mode: A dictionary used to record the product of the current
                document vector and query, whose key is the document id.
            results: Similarity storage dictionary, whose key is the document id,
                and the value is the similarity between the corresponding document
                and query.

        Returns:
            A list of the top 10 document ids for similarity ranking.
            For example:

            [1938,1071,1572,2371,1410,2319,971,2218]
        '''
        sellected_index = {k: v for k, v in self.index.items() if k in query} # Subset of index dictionary related to query
        com_mode = dict()
        if self.termWeighting == 'tf':
            for term, docid_dict in sellected_index.items():
                for docid, freq in docid_dict.items():
                    com_mode[docid] = com_mode.get(
                        docid, 0) + query[term] * freq
        elif self.termWeighting == 'binary':
            for term, docid_dict in sellected_index.items():
                for docid, freq in docid_dict.items():
                    com_mode[docid] = com_mode.get(docid, 0) + 1
        elif self.termWeighting == 'tfidf':
            for term, docid_dict in sellected_index.items():
                idf = self.idf[term]
                for docid, freq in docid_dict.items():
                    com_mode[docid] = com_mode.get(
                        docid, 0) + query[term] * idf * freq * idf
        # Divide the accumulated value by the size of the corresponding document
        for docid, accu in com_mode.items():
            com_mode[docid] = com_mode[docid] / self.docMode[docid]
        # Sort by dictionary value, that is, similarity order
        results = sorted(com_mode, key=lambda k: com_mode[k], reverse=True)
        return results[:10]
