import math

class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting):
        self.index = index
        self.termWeighting = termWeighting
        self.docLength = self.__getDocLength()
        if self.termWeighting == 'tfidf':
            self.idf = {term:math.log10(self.docLength/len(docid_dict)) for term,docid_dict in self.index.items()}
        self.docMode = self.getDocMode()

    # get the total number of documents
    def __getDocLength(self):
        max_index = 0
        for term in self.index:
            present_term = max(self.index[term])
            max_index = present_term if present_term > max_index else max_index
        return max_index

    def getDocMode(self):
        doc_mode = dict().fromkeys(range(1,self.docLength+1),0)
        if self.termWeighting == 'tf':
            for term,docid_dict in self.index.items():
                for docid,freq in docid_dict.items():
                    doc_mode[docid] += freq*freq
        elif self.termWeighting == 'binary':
            for term,docid_dict in self.index.items():
                for docid,freq in docid_dict.items():
                    doc_mode[docid] += 1
        elif self.termWeighting == 'tfidf':
            for term,docid_dict in self.index.items():
                idf = self.idf[term]
                for docid,freq in docid_dict.items():
                    doc_mode[docid] += freq*idf*freq*idf
        # may don't need to do know
        # TODO: sqrt later
        for docid, accu in doc_mode.items():
            doc_mode[docid] = math.sqrt(accu)
        return doc_mode

    # Method performing retrieval for specified query
    def forQuery(self, query):
        sellected_index = {k:v for k,v in self.index.items() if k in query}
        com_mode = dict()#.fromkeys(range(1,t3.docLength+1),0)
        if self.termWeighting == 'tf':
            for term,docid_dict in sellected_index.items():
                for docid,freq in docid_dict.items():
                    com_mode[docid] = com_mode.get(docid,0) + query[term] * freq
        elif self.termWeighting == 'binary':
            for term,docid_dict in sellected_index.items():
                for docid,freq in docid_dict.items():
                    com_mode[docid] = com_mode.get(docid,0) + 1
        elif self.termWeighting == 'tfidf':
            for term,docid_dict in sellected_index.items():
                idf = self.idf[term]
                for docid,freq in docid_dict.items():
                    com_mode[docid] = com_mode.get(docid,0) + query[term] * idf * freq * idf
        for docid,accu in com_mode.items():
            com_mode[docid] = com_mode[docid] / self.docMode[docid]
        results = sorted(com_mode, key = lambda k: com_mode[k], reverse=True)
        return results[:10]
