import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import os
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
from shutil import copyfile
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


def readname(filePath):
    name = os.listdir(filePath)
    return name


# 定义一个用于提取特征的函数
# 输入一段文本返回形如：{'It': True, 'movie': True, 'amazing': True, 'is': True, 'an': True}
# 返回类型是一个dict
def extract_features(word_list):
    return dict([(word, True) for word in word_list])


def probability_distribution(data, name):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文无法显示的问题
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    bins = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    # print(len(bins))
    # for i in range(0, len(bins)):
    # print(bins[i])
    plt.xlim(0, 1)
    # plt.ylim(0, 100)
    plt.title(name + "情感消极概率直方图")
    plt.xlabel('probability of negative')
    plt.ylabel('频数')
    # 频率分布normed=True，频次分布normed=False
    plt.hist(x=data, bins=bins, color='steelblue',  # 指定直方图的填充色
             edgecolor='black')
    plt.savefig(name + "_prob.png")
    plt.clf()
    # plt.show()


# 我们需要训练数据，这里将用NLTK提供的电影评论数据
if __name__ == '__main__':
    # 加载积极与消极评论
    positive_fileids = movie_reviews.fileids('pos')  # list类型 1000条数据 每一条是一个txt文件
    negative_fileids = movie_reviews.fileids('neg')
    # print(type(positive_fileids), len(negative_fileids))

    # 将这些评论数据分成积极评论和消极评论
    # movie_reviews.words(fileids=[f])表示每一个txt文本里面的内容，结果是单词的列表：['films', 'adapted', 'from', 'comic', 'books', 'have', ...]
    # features_positive 结果为一个list
    # 结果形如：[({'shakesp: True, 'limit': True, 'mouth': True, ..., 'such': True, 'prophetic': True}, 'Positive'), ..., ({...}, 'Positive'), ...]
    features_positive = [(extract_features(movie_reviews.words(fileids=[f])), 'Positive') for f in positive_fileids]
    features_negative = [(extract_features(movie_reviews.words(fileids=[f])), 'Negative') for f in negative_fileids]

    # 分成训练数据集（80%）和测试数据集（20%）
    threshold_factor = 0.8
    threshold_positive = int(threshold_factor * len(features_positive))  # 800
    threshold_negative = int(threshold_factor * len(features_negative))  # 800
    # 提取特征 800个积极文本800个消极文本构成训练集  200+200构成测试文本
    features_train = features_positive[:threshold_positive] + features_negative[:threshold_negative]
    features_test = features_positive[threshold_positive:] + features_negative[threshold_negative:]
    print("\n训练数据点的数量:", len(features_train))
    print("测试数据点的数量:", len(features_test))
    # 训练朴素贝叶斯分类器
    classifier = NaiveBayesClassifier.train(features_train)
    print("\n分类器的准确性:", nltk.classify.util.accuracy(classifier, features_test))

    # print("\n十大信息最丰富的单词:")
    # for item in classifier.most_informative_features()[:10]:
    # print(item[0])

    filedir = ['BBC', 'CNN', 'Daily Mail', 'SMH', 'TASS',
               'VOA', '澳大利亚新闻网', 'India today']
    for j in filedir:
        prob = []
        input_reviews = []
        filePath = 'D:/Desktop/情感极性分析（分媒体/' + j
        # filePath = 'D:/desktop/train/' + j
        name = readname(filePath)
        for i in name:
            file = filePath + '/' + i
            f = open(file, "r", encoding='utf-8')
            content = f.read()
            content = content.strip("\n")
            probdist = classifier.prob_classify(extract_features(content.split()))
            pred_sentiment = probdist.max()
            if pred_sentiment == 'Positive':
                prob.append(1 - probdist.prob(pred_sentiment))
            elif pred_sentiment == 'Negative':
                prob.append(probdist.prob(pred_sentiment))
        probability_distribution(prob, j)
