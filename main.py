from classes.FileReader import FileReader
from classes.Sanitizer import Sanitizer
    
if __name__ == '__main__':
    
    data = FileReader.load_all()
    
    # print(Sanitizer.dictionary_from_list_sentence(data['negatif']))
