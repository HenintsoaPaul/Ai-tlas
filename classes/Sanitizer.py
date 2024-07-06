import re
import nltk
import math
from typing import Dict, List


class Sanitizer:
    @staticmethod
    def dictionary(sentence: str) -> list[str]:
        """Transforme la phrase en minuscule, puis retourne la liste 
        des mots uniques de la phrase. Toutes les caracteres non alphabetiques
        sont supprimes (ponctuations, chiffres, ...) sont supprimées."""
        
        tokens = nltk.word_tokenize(sentence.lower())
        unique_tokens = set(tokens)    
        return [token for token in unique_tokens if re.match(r'^\w+$', token)]
    
    @staticmethod
    def tf(my_word: str, text: str) -> int:
        """Compte le `Term Frequency` d'un mot dans une phrase
        apres l'avoir transforme en minuscule."""
        
        tokens = nltk.word_tokenize(text.lower())
        return sum(1 for word in tokens if my_word == word)
    
    @staticmethod
    def idf(my_word: str, corpus: list[str]) -> float:
        """Calcul l'`Inverse Document Frequency` d'un mot dans un dictionnaire."""
        
        count = 0
        dictionaries: list[list[str]] = [Sanitizer.dictionary(sentence) for sentence in corpus]
        for dict in dictionaries:
            if my_word in dict:
                count += 1
        return math.log10(len(corpus) / count)
    
    @staticmethod
    def tf_idf(my_word: str, text: str, corpus: List[str]) -> float:
        """Calcul le `Term Frequency Inverse Document Frequency` d'un mot dans une phrase."""
        
        tf: int = Sanitizer.tf(my_word, text)
        idf: float = Sanitizer.idf(my_word, corpus)
        return tf * idf