# %%
import visdom
vis = visdom.Visdom()


def Readfile(path):
    with open(path) as handle:
        text = handle.read()
    return text


ROOT = 'lab/data/'
FILE = 'mobydick.txt'
PATH = ROOT + FILE
data = Readfile(PATH)

# %%


def PrintStatus(func):
    def wrapper(*arg, **kwarg):
        tmp = func(*arg, **kwarg)
        print('Total words: {}'.format(tmp.length))
        print('Distinct words: {}'.format(tmp.unique))
        return tmp
    return wrapper


@PrintStatus
class words:
    def __init__(self, text: str):
        self.text = text
        self.stop = self._getStop()
        self.dict = dict()
        self.sortlist = list()
        self.CountWords()
        self.Sort(reverse=True)
        self.length = self._length()
        self.unique = len(self.sortlist)

    def _add2dict(self, word: str):
        self.dict[word] = self.dict.get(word, 0) + 1

    def _text2list(self, text: str) -> list:
        import re
        return re.findall(r'[a-z]+', text.lower())

    def _length(self):
        return len(self._text2list(self.text))

    def _getStop(slef):
        return ''

    def CountWords(self):
        stop_set = set(self._text2list(self.stop))
        words_list = self._text2list(self.text)
        for word in words_list:
            if word not in stop_set:
                self._add2dict(word)

    def Sort(self, reverse=False):
        self.sortlist = sorted(
            self.dict.items(), key=lambda i: i[1], reverse=reverse)

    def Sample(self, num=5, seed=410):
        import numpy as np
        np.random.seed(seed=seed)
        disorder = np.random.permutation(self.sortlist)
        return disorder[:num].tolist()

    def Head(self, num=20):
        return self.sortlist[:num]


law = words(data)

law.Sample(num=5, seed=410)
law.Head(num=20)

# %% 5. Plot words sorted frequencies
n_list = [100, 1000, None]

for n in n_list:
    index_freq = [i[1] for i in law.sortlist[:n]]
    index_word = range(len(law.sortlist[:n]))
    vis.line(index_freq)
    # vis.bar(index_freq)

# %% 6. Plot the cumulative count

index_freq = [i[1] for i in law.sortlist[:n]]
index_freq_cum = index_freq.copy()
for i in range(len(index_freq_cum)):
    index_freq_cum[i] = index_freq_cum[i] if i == 0 else index_freq_cum[i] + \
        index_freq_cum[i - 1]

for n in n_list:
    index_freq = [i[1] for i in law.sortlist[:n]]
    index_freq_cum = index_freq.copy()
    for i in range(len(index_freq_cum)):
        index_freq_cum[i] = index_freq_cum[i] if i == 0 else index_freq_cum[i] + \
            index_freq_cum[i - 1]
    index_word = range(len(law.sortlist[:n]))
    # vis.line(index_freq_cum)
    vis.bar(index_freq_cum)
