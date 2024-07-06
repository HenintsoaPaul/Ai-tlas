from classes.FileReader import FileReader
    
if __name__ == '__main__':
    # data = FileReader.load_data('data/neutre.txt')
    # print(data[5])
    
    data = FileReader.load_all()
    print(data['negatif'][5])
