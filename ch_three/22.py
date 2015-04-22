# ◑ Examine the results of processing the URL http://news.bbc.co.uk/ using the regular expressions suggested above. You will see that there is still a fair amount of non-textual data there, particularly Javascript commands. You may also find that sentence breaks have not been properly preserved. Define further regular expressions that improve the extraction of text from this web page.


from urllib import request
from bs4 import BeautifulSoup
import re
from nltk import word_tokenize
from nltk.corpus import words

def unknown(url):
	"""Takes a URL as its argument and returns a list of unknown words that occur on that webpage."""
	
	# gets the text of the page
	html = request.urlopen(url).read().decode('utf8')
	raw = BeautifulSoup(html).get_text()

	# finds the lower case words by searching for a word boundary plus one or more lower case letters
	lower_case_words = re.findall(r'\b[a-z]+', raw)

	# searches through the list of lower case words and gets rid of those in the words corpus.
	unknowns = [word for word in lower_case_words if word not in words.words()]
	return unknowns

#THIS IS WHERE YOU SHOULD START WITH ERIC. you tried to go through and make a regex that would find everything contained within brackets, but that didn't seem to be working. In general, what are other ways of stripping out non-text stuff from pages?

def js_stripper(text):
	for word in text:
		# returns anything contained within brackets
		junkre = re.compile(r'\{.*\}', re.DOTALL)
		junkre.sub('', text)
		print

unknown_words_raw = unknown('http://news.bbc.co.uk/')

