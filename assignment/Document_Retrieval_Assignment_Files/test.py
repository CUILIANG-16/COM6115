import re
import time
import math

def check_dict(dict1,dict2):
    if len(dict1)!= len(dict2):
        print("Different")
        return False
    for key,value in dict1.items():
        if dict2[key] != value:
            print("Different")
            return False
    print("The Same")
    return True

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
    def __init__(self,index, termWeighting, version):
        self.index = index
        self.termWeighting = termWeighting
        self.docLength = self.__getDocLength()
        if version == 1:
            self.docMode = self.getDocMode_v1()
        elif version == 2:
            self.docMode = self.getDocMode_v2()
        elif version == 3:
            self.docMode = self.getDocMode_v3()

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

    def __tf_mode(self,term,docid):
        freq = self.index[term].get(docid,0)
        return freq

    def __bi_mode(self,term,docid):
        binary = 1 if docid in self.index[term] else 0
        return binary

    @__Viewer()
    def getDocMode_v1(self):
        doc_mode = dict()
        mode_function_dict = {'tf':self.__tf_mode, 'binary':self.__bi_mode}
        mode_function = mode_function_dict[self.termWeighting]
        for docid in range(1,self.docLength+1): # number of all documents
            mode = 0 # set mode to 0
            for term in self.index: # all the term appear in all documents
                mode_item = mode_function(term,docid)
                mode += mode_item * mode_item
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

    @__Viewer()
    def getDocMode_v2(self):
        doc_mode = dict()
        if self.termWeighting == 'tf':
            for term,docid_dict in self.index.items():
                for docid,freq in docid_dict.items():
                    doc_mode[docid] = doc_mode.get(docid,0) + freq*freq
        elif self.termWeighting == 'binary':
            for term,docid_dict in self.index.items():
                for docid,freq in docid_dict.items():
                    doc_mode[docid] = doc_mode.get(docid,0) + 1
        # may don't need to do know
        # TODO: sqrt later
        for docid, accu in doc_mode.items():
            doc_mode[docid] = math.sqrt(accu)
        return doc_mode

    @__Viewer()
    def getDocMode_v3(self):
        doc_mode = dict().fromkeys(range(1,self.docLength+1),0)
        if self.termWeighting == 'tf':
            for term,docid_dict in self.index.items():
                for docid,freq in docid_dict.items():
                    doc_mode[docid] += freq*freq
        elif self.termWeighting == 'binary':
            for term,docid_dict in self.index.items():
                for docid,freq in docid_dict.items():
                    doc_mode[docid] += 1
        # may don't need to do know
        # TODO: sqrt later
        for docid, accu in doc_mode.items():
            doc_mode[docid] = math.sqrt(accu)
        return doc_mode

    # Method performing retrieval for specified query
    @__Viewer()
    def forQuery_v1(self, query):
        candidate_term = query.keys() & self.index.keys()
        candidate_docid = set()
        for term in candidate_term:
            candidate_docid |= self.index[term].keys()
        return range(10)
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

    @__Viewer()
    def forQuery(self, query):
        sellected_index = {k:v for k,v in self.index.items() if k in query}
        com_mode = dict()#.fromkeys(range(1,t3.docLength+1),0)
        for term,docid_dict in sellected_index.items():
            for docid,freq in docid_dict.items():
                com_mode[docid] = com_mode.get(docid,0) + query[term] * freq
        for docid,accu in com_mode.items():
            com_mode[docid] = com_mode[docid] / self.docMode[docid]
        results = sorted(com_mode, key = lambda k: com_mode[k], reverse=True)
        return results[:10]

# %%
tw = ['binary','tf'][0]
t1 = Retrieve(index = index,termWeighting = tw,version=1)
t2 = Retrieve(index = index,termWeighting = tw,version=2)
t3 = Retrieve(index = index,termWeighting = tw,version=3)
check_dict(t1.docMode,t2.docMode)
check_dict(t2.docMode,t3.docMode)

t3.forQuery(query)
