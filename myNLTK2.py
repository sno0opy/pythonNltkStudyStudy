#coding=utf-8
#开头不声明 默认为ascⅡ编码保存 本书为python自然语言处理
#============================================================符号声明
'''
									!					软件和书中版本不同注意点
									表达式：            基本表达式	
'''
#============================================================
from __future__ import division
import nltk 
#from nltk.book import *				# *太费时间改为text1却发现无用
#----------------------------------------2.1获取文本语料库
#古腾堡语料库
'''
#nltk.corpus.gutenberg.fileids()
emma=nltk.corpus.gutenberg.words('austen-emma.txt')
print len(emma)
from nltk.corpus import gutenberg		#前面太长另一种import方法
for fileid in gutenberg.fileids():
	num_chars=len(gutenberg.raw(fileid))
	num_words=len(gutenberg.words(fileid))
	num_sents=len(gutenberg.sents(fileid))
	num_vocab=len(set([w.lower() for w in gutenberg.words(fileid)]))
	print int(num_chars/num_words),int((num_words/num_sents)),int(num_words/num_vocab),fileid
'''
#网络和聊天文本
'''
from nltk.corpus import webtext
for fileid in webtext.fileids():
	print fileid ,webtext.raw(fileid)[:50],"..."
from nltk.corpus import nps_chat

chatroom=nps_chat.posts('10-19-20s_706posts.xml')
print chatroom[123]
'''
#布朗语料库
'''
from nltk.corpus import brown
print brown.categories()
print brown.words(categories='news')
print brown.words(fileids=['cg22'])
print brown.sents(categories=['news','editorial','reviews'])
news_text=brown.words(categories='news')
fdist=nltk.FreqDist([w.lower() for w in news_text])
modals=['can','could','may','might','must','will']
for m in modals:
	print m +":",fdist[m],
cfd=nltk.ConditionalFreqDist((genre,word)  						#此处函数不会语法错误
	for genre in brown.categories() 
	for word in brown.word(categories=genre))
genres=['news','religion','hobbies','science_fiction','romance','humor']
#modals=['can','could','may','might','must','will']
cfd.tabulate(Conditionals=genres,samples=modals) 
'''
#路透社语料库
'''
from nltk.corpus import udhr
raw_text=udhr.raw('javanese-Latin1')
nltk.FreqDist(raw_text).plot()
'''
#----------------------------------------2.2条件概率分布
#----------------------------------------2.3python代码重用
'''
def plural(word):
	if word.endswith('y'):
		return word[:-1]+'ies'
	elif word[-1] in 'sx' or word [-2:] in ['sh','ch']:
		return word+'es'
	elif word.endswith("an"):
		return word[:-2]+'en'
	else:
		return word+"s"
print plural('word')
print plural('worry')
print plural("fan")
'''
#----------------------------------------2.5WordNet
#意义与同义词
from nltk.corpus import wordnet as wn
print wn.synsets('motorcar')
print wn.synset('car.n.01').lemma_names
print wn.synset('car.n.01').examples
print wn.synset('car.n.01').definition
print wn.synset('car.n.01').lemmas