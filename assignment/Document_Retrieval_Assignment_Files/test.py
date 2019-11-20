import re
import time
import math

class IndexLoader:
    def __init__(self, indexFile):
        self.index = {}
        docidCountRE = re.compile('(\d+):(\d+)')
        f = open(indexFile, 'r')
        for line in f:
            term = line.split(' ', 1)[0]
            self.index[term] = {}
            for (docid, count) in docidCountRE.findall(line):
                docid = int(docid)
                self.index[term][docid] = int(count)

    def getIndex(self):
        return self.index

index = IndexLoader('assignment/Document_Retrieval_Assignment_Files/index_nostoplist_nostemming.txt').getIndex()

query = {'an': 1, 'articles': 1, 'computers': 1, 'deal': 1, 'exist': 1, 'for': 1, 'ibm': 1, 'operating': 1, 'sharing': 1, 'system': 2, 'time': 1, 'tss': 1, 'what': 1, 'which': 1, 'with': 1}

class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting):
        self.index = index
        self.termWeighting = termWeighting
        self.docLength = self.__getDocLength()
        self.docMode = self.getDocMode()

    def __Viewer(description = None):
        def decorate(func):
            def wrapper(*args,**kwargs):
                print('Function:',func.__name__)
                tic = time.time()
                ans = func(*args,**kwargs)
                if description is not None:
                    print(description,ans)
                print('Time spent:',time.time()-tic,'\n')
                return ans
            return wrapper
        return decorate

    @__Viewer()
    def getDocMode(self):
        doc_mode = dict()
        if self.termWeighting == 'tf':
            for docid in range(1,self.docLength+1): # number of all documents
                mode = 0 # set mode to 0
                for term in self.index: # all the term appear in all documents
                    freq = self.index[term].get(docid,0)  # get frequency of the term
                    mode += freq * freq
                doc_mode[docid] = math.sqrt(mode) #pow(mode,1/2)
        elif self.termWeighting == 'binary':
            for docid in range(1,self.docLength+1): # number of all documents
                mode = 0 # set mode to 0
                for term in self.index: # all the term appear in all documents
                    binary = 1 if docid in self.index[term] else 0
                    mode += binary * binary
                doc_mode[docid] = math.sqrt(mode) #pow(mode,1/2)
        return doc_mode

    # get the total number of documents
    @__Viewer("The length of documents:")
    def __getDocLength(self):
        max_index = 0
        for term in self.index:
            present_term = max(self.index[term])
            max_index = present_term if present_term > max_index else max_index
        return max_index

    # Method performing retrieval for specified query
    def forQuery(self, query):
        candidate_term = query.keys() & self.index.keys()
        candidate_docid = set()
        for term in candidate_term:
            candidate_docid |= self.index[term].keys()
        score = dict()
        for docid in candidate_docid:
            qd = 0
            for term in candidate_term:
                q = query[term]
                d = self.index[term].get(docid,0)
                qd += q*d
            dd = 0
            mode = self.mode[docid]
            similarity = qd / mode
            score[docid] = similarity
        results = sorted(score, key = lambda k: score[k], reverse=True)
        return results[:10]

# %%
t = Retrieve(index = index,termWeighting = 'binary')
t.docMode
pow(t.docMode[500],2)
