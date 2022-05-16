# random functions for Natural Language Processing
import nltk
from nltk.book import *

def lexical_diversity(text):
	return  len(text) / len(set(text))

def percentage(count, total):
	return 100 * count / total

def vocab_size(text):
	return len(set([w.lower() for w in text]))

def percent(word, text):
	return text.count(word)/len(text)*100

def generate_model(cfdist, word, num=15):
	for i in range(num):
		print(word, end = ' ')
		word = cfdist[word].max()
	print('', end='\n')

def plural(word):
	if word.endswith('y'):
		return word[:-1] + 'ies'
	elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
		return word + 'es'
	elif word.endswith('an') and len(word) > 3:
		return word[:-2] + 'en'
	else:
		return word + 's'
