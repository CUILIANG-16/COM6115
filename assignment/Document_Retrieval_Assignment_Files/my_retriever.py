
class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting):
        self.index = index
        self.termWeighting = termWeighting
        self.mode = self.VectorMode()

    def VectorMode(self):
        mode = dict()
        for docid in range(1,self._length()+1):
            dd = 0
            for term in self.index:
                d = self.index[term].get(docid,0)
                dd += d*d
            mode[docid] = pow(dd,1/2)
        return mode

    def _length(self):
        max_index = 0
        for term in self.index:
            present = max(self.index[term])
            max_index = present if present > max_index else max_index
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