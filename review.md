[[toc]]
# I. Sentiment Analysis
## 1. Goal of SA
* [ ] Explain
* [ ] Determin objective & subjective texts
* [ ] Main elements
* [ ] Critical summary of the main approaches
* [ ] Explain the evaluation of SA system

## 2. Explain & Applications
**Definition of SA:**
1. Extract opinions, sentiment and emotions from text and use the information for business.
2. Huge volumes of text and can't be done manually.

**Examples:**
* Product review mining: features of iphone customers like & dislike.
* Review classification: movie positive & negative.
* Tracking sentiments toward topics over time: anger growing or cooling?
* Prediction trends: Election & market

## 3. Objective & Subjective
**Objective** refers to the facts:
* "I bought the new iPhone a few days ago."

**Subjective** may contain opinions of objects (positive or negative):
* "It was such a nice phone."

> 1. Objective can express opinions (indirectly):
>     * Sarcasm: "My phone broke in the second day.""
> 2. Subjective may not express positive or negative opinions:
>     * "I think he came yesterday."

## 4. Model Elements
* Target object: $o_j$
  - has components, sub-components
    - Phone -> Battery | Screen
  - has a set of attributes:
    - Phone{size, price} -> Battery{weight, battery life}"
* Feature of the object $o_j$ : $f_{jk}$
  - opinion on components or attributes
* The sentiment value: $so_{ijkl}$
  - positive or negative
  - rating, 1~5 stars in movie reviews
* Opinion holder: $h_i$
* Time: $t_l$

**Examples:**
![](img/Jietu20200125-013552.jpg)

> Challenges:
> * Co-reference Resolution: 上下文指代同一物品
> * Relation Extraction: 物品之间的关系，相机拍照片
> * Synonym Match: 同义词
# II. Information Retrieval
# III. Natural Language Generation
# IV. Information Extraction
