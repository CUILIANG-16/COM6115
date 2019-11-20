import json
index = dict()
with open('assignment/Document_Retrieval_Assignment_Files/'+'index.json', 'r') as fp:
     index = json.load(fp)

query = {'an': 1, 'articles': 1, 'computers': 1, 'deal': 1, 'exist': 1, 'for': 1, 'ibm': 1, 'operating': 1, 'sharing': 1, 'system': 2, 'time': 1, 'tss': 1, 'what': 1, 'which': 1, 'with': 1}

candidate_term = query.keys() & index.keys()
candidate_docid = set()
for term in candidate_term:
    candidate_docid |= index[term].keys()

score = dict()
for docid in candidate_docid:
    qd = 0
    for term in candidate_term:
        q = query[term]
        d = index[term].get(docid,0)
        qd += q*d
    dd = 0
    for term in index:
        d = index[term].get(docid,0)
        dd += d*d
    similarity = qd / pow(dd,1/2)
    score[docid] = similarity


results = sorted(score, key = lambda k: score[k], reverse=True)[:10]

results


max(index['an'])
