import re
import nltk
from typing import Dict, List


class Sanitizer:
    @staticmethod
    def dictionary(sentence: str) -> list[str]:
        """Transforme la phrase en minuscule, puis retourne la liste 
        des mots uniques de la phrase. Les ponctuations sont supprimées."""
        
        tokens = nltk.word_tokenize(sentence.lower())
        unique_tokens = set(tokens)    
        # Filter ponctuations
        return [token for token in unique_tokens if re.match(r'^\w+$', token)]
