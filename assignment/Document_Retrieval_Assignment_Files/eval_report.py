import pandas as pd
import matplotlib.pyplot as plt
PATH = 'assignment/Document_Retrieval_Assignment_Files/'
data = pd.read_csv(PATH+'Evaluation.csv')
data = data.fillna(False)
for param in {'-s','-p'}:
    data[param] = data[param]==param
print(data)

class eval:
    def __init__(self,data,mode):
        self.mode = mode
        self.data = data[(data['Mode'] == mode)]

    def getData(self,s,p,column):
        item = self.data[(self.data['-s'] == s) & (self.data['-p'] == p)]
        if 't' in column.lower():
            return item['Time(s)'].values[0]
        elif 'p' in column.lower():
            return item['Precision'].values[0]
        elif 'f' in column.lower():
            return item['F-measure'].values[0]
        else:
            return item['Recall'].values[0]


# %% Time Cost
name_list = ['Binary','TF','TF-IDF']
binary = eval(data,'Binary')
tf = eval(data,'TF')
tfidf = eval(data,'TF-IDF')
s, p = False,False
ns_np_list = [binary.getData(s,p,'t'),tf.getData(s,p,'t'),tfidf.getData(s,p,'t')]
s, p = True,False
s_np_list = [binary.getData(s,p,'t'),tf.getData(s,p,'t'),tfidf.getData(s,p,'t')]
s, p = False,True
ns_p_list = [binary.getData(s,p,'t'),tf.getData(s,p,'t'),tfidf.getData(s,p,'t')]
s, p = True,True
s_p_list = [binary.getData(s,p,'t'),tf.getData(s,p,'t'),tfidf.getData(s,p,'t')]

plt.figure(figsize=(12, 6))
x =list(range(3))
total_width, n = 0.8, 4
width = total_width / n
color = ['#5871F6','#E51B2F','#F9B600','#8FBE00']

text_y = ns_np_list
ns_np = plt.bar(x, ns_np_list, width=width, label='raw',fc = color[0])
i = 0
for bar in ns_np:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1

for i in range(len(x)):
    x[i] = x[i] + width
text_y = ns_p_list
ns_p = plt.bar(x, ns_p_list, width=width, label='stem',tick_label = name_list,fc = color[1])
i = 0
for bar in ns_p:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1

for i in range(len(x)):
    x[i] = x[i] + width
text_y = s_np_list
s_np = plt.bar(x, s_np_list, width=width, label='stoplist',fc = color[2])
i = 0
for bar in s_np:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1


for i in range(len(x)):
    x[i] = x[i] + width
text_y = s_p_list
s_p = plt.bar(x, s_p_list, width=width, label='stoplist & stem',fc = color[3])
i = 0
for bar in s_p:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1

plt.title("Time Cost (second)",fontsize=16,fontweight='bold')
plt.legend(loc = 'upper right')
plt.savefig(PATH + 'TimeCost.png')
plt.show()

#%% Binary
name_list = ['Precision','Recall','F-Measure']
binary = eval(data,'Binary')
s, p = False,False
ns_np_list = [binary.getData(s,p,'p'),binary.getData(s,p,'r'),binary.getData(s,p,'f')]
s, p = True,False
s_np_list = [binary.getData(s,p,'p'),binary.getData(s,p,'r'),binary.getData(s,p,'f')]
s, p = False,True
ns_p_list = [binary.getData(s,p,'p'),binary.getData(s,p,'r'),binary.getData(s,p,'f')]
s, p = True,True
s_p_list = [binary.getData(s,p,'p'),binary.getData(s,p,'r'),binary.getData(s,p,'f')]


plt.figure(figsize=(12, 6))
x =list(range(3))
total_width, n = 0.8, 4
width = total_width / n
color = ['#5871F6','#E51B2F','#F9B600','#8FBE00']

text_y = ns_np_list
ns_np = plt.bar(x, ns_np_list, width=width, label='raw',fc = color[0])
i = 0
for bar in ns_np:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1

for i in range(len(x)):
    x[i] = x[i] + width
text_y = ns_p_list
ns_p = plt.bar(x, ns_p_list, width=width, label='stem',tick_label = name_list,fc = color[1])
i = 0
for bar in ns_p:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1

for i in range(len(x)):
    x[i] = x[i] + width
text_y = s_np_list
s_np = plt.bar(x, s_np_list, width=width, label='stoplist',fc = color[2])
i = 0
for bar in s_np:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1


for i in range(len(x)):
    x[i] = x[i] + width
text_y = s_p_list
s_p = plt.bar(x, s_p_list, width=width, label='stoplist & stem',fc = color[3])
i = 0
for bar in s_p:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1

plt.title("Binary Evaluation Score",fontsize=16,fontweight='bold')
plt.legend(loc = 'upper right')
plt.savefig(PATH + 'BinaryEvaluationScore.png')
plt.show()

# %% TF
name_list = ['Precision','Recall','F-Measure']
binary = eval(data,'TF')
s, p = False,False
ns_np_list = [binary.getData(s,p,'p'),binary.getData(s,p,'r'),binary.getData(s,p,'f')]
s, p = True,False
s_np_list = [binary.getData(s,p,'p'),binary.getData(s,p,'r'),binary.getData(s,p,'f')]
s, p = False,True
ns_p_list = [binary.getData(s,p,'p'),binary.getData(s,p,'r'),binary.getData(s,p,'f')]
s, p = True,True
s_p_list = [binary.getData(s,p,'p'),binary.getData(s,p,'r'),binary.getData(s,p,'f')]


plt.figure(figsize=(12, 6))
x =list(range(3))
total_width, n = 0.8, 4
width = total_width / n
color = ['#5871F6','#E51B2F','#F9B600','#8FBE00']

text_y = ns_np_list
ns_np = plt.bar(x, ns_np_list, width=width, label='raw',fc = color[0])
i = 0
for bar in ns_np:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1

for i in range(len(x)):
    x[i] = x[i] + width
text_y = ns_p_list
ns_p = plt.bar(x, ns_p_list, width=width, label='stem',tick_label = name_list,fc = color[1])
i = 0
for bar in ns_p:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1

for i in range(len(x)):
    x[i] = x[i] + width
text_y = s_np_list
s_np = plt.bar(x, s_np_list, width=width, label='stoplist',fc = color[2])
i = 0
for bar in s_np:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1


for i in range(len(x)):
    x[i] = x[i] + width
text_y = s_p_list
s_p = plt.bar(x, s_p_list, width=width, label='stoplist & stem',fc = color[3])
i = 0
for bar in s_p:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1

plt.title("TF Evaluation Score",fontsize=16,fontweight='bold')
plt.legend(loc = 'upper right')
plt.savefig(PATH + 'TFEvaluationScore.png')
plt.show()

# %% TF-IDF
name_list = ['Precision','Recall','F-Measure']
binary = eval(data,'TF-IDF')
s, p = False,False
ns_np_list = [binary.getData(s,p,'p'),binary.getData(s,p,'r'),binary.getData(s,p,'f')]
s, p = True,False
s_np_list = [binary.getData(s,p,'p'),binary.getData(s,p,'r'),binary.getData(s,p,'f')]
s, p = False,True
ns_p_list = [binary.getData(s,p,'p'),binary.getData(s,p,'r'),binary.getData(s,p,'f')]
s, p = True,True
s_p_list = [binary.getData(s,p,'p'),binary.getData(s,p,'r'),binary.getData(s,p,'f')]


plt.figure(figsize=(12, 6))
x =list(range(3))
total_width, n = 0.8, 4
width = total_width / n
color = ['#5871F6','#E51B2F','#F9B600','#8FBE00']

text_y = ns_np_list
ns_np = plt.bar(x, ns_np_list, width=width, label='raw',fc = color[0])
i = 0
for bar in ns_np:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1

for i in range(len(x)):
    x[i] = x[i] + width
text_y = ns_p_list
ns_p = plt.bar(x, ns_p_list, width=width, label='stem',tick_label = name_list,fc = color[1])
i = 0
for bar in ns_p:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1

for i in range(len(x)):
    x[i] = x[i] + width
text_y = s_np_list
s_np = plt.bar(x, s_np_list, width=width, label='stoplist',fc = color[2])
i = 0
for bar in s_np:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1


for i in range(len(x)):
    x[i] = x[i] + width
text_y = s_p_list
s_p = plt.bar(x, s_p_list, width=width, label='stoplist & stem',fc = color[3])
i = 0
for bar in s_p:
    plt.text(bar.get_x()+0.05,text_y[i]+0.003,round(text_y[i],3),fontsize = 8)
    i += 1

plt.title("TF-IDF Evaluation Score",fontsize=16,fontweight='bold')
plt.legend(loc = 'upper right')
plt.savefig(PATH + 'TF-IDFEvaluationScore.png')
plt.show()
