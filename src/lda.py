# coding=utf-8
from gensim import corpora, models, similarities

# 将分完词的文档加载成符合gensim文格式的输入
with open('document.txt', 'r', encoding='utf-8') as f:
    train = []
    for line in f.readlines():
        line = [word.strip() for word in line.split()]
        train.append(line)

# 构造词典
dictionary = corpora.Dictionary(train)
feature_cnt = len(dictionary.token2id)  # 词典中词的数量
dictionary.save('dict.txt')  # 保存生成的词典,用于以后加载
# dictionary=Dictionary.load('dict.txt')#加载词典

# 基于词典，将【分词列表集】转换成【向量集】，形成【语料库】
corpus = [dictionary.doc2bow(text) for text in train]

# 使用【TF-IDF模型】处理语料库
tfidf_model = models.TfidfModel(corpus)

# 打印模型参数：文档数量与语料库单词数
print(tfidf_model)

# 存储通过tfidf转化过的文档
with open('tfidf_doc.txt', 'w', encoding='utf-8') as fr:
    for doc in tfidf_model[corpus]:
        fr.write(doc.__str__() + '\n')
