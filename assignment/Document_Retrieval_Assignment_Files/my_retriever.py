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
    '''
    def check_dict(self,dict1,dict2):
        if len(dict1)!= len(dict2):
            print("Length is Different")
            return False
        for key,value in dict1.items():
            if abs(dict2[key]-value)>10**-4:
                print("Value is Different\n")
                print("Key:{},True:{},Get:{}".format(key,value,dict2[key]))
                return False
        print("The Same")
        return True
    '''

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
    '''
    # only calculate the mode for tf mode
    def VectorMode(self):
        mode = dict()
        for docid in range(1,self.__getDoclength()+1): # number of all documents
            dd = 0 # set mode to 0
            for term in self.index: # all the term appear in all documents
                d = self.index[term].get(docid,0)  # get frequency of the term
                dd += d*d
            mode[docid] = pow(dd,1/2)
        return mode
    '''

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
