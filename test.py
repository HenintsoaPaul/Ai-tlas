from classes.FileReader import FileReader
from classes.Sanitizer import Sanitizer


corpus = FileReader.load_positif()
phrase = corpus[0]
print(f"Phrase: {phrase}")
tokens = Sanitizer.dictionary(phrase)

print(tokens[0])
print(Sanitizer.tf(tokens[0], phrase))
print(Sanitizer.idf(tokens[0], corpus))
print(Sanitizer.tf_idf(tokens[0], phrase, corpus))