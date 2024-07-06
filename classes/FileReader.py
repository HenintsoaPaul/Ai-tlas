from typing import Dict


class FileReader:
    @staticmethod
    def load_corpus(file_path: str) -> list[str]:
        data = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    data.append(line.strip())
            return data
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None
        
    @staticmethod
    def load_positif() -> list[str]:
        return FileReader.load_corpus('data/positif.txt')
    
    @staticmethod
    def load_negatif() -> list[str]:
        return FileReader.load_corpus('data/negatif.txt')
    
    @staticmethod
    def load_neutre() -> list[str]:
        return FileReader.load_corpus('data/neutre.txt')
    
    @staticmethod
    def load_all() -> Dict[str, list[str]]:
        return {
            'positif': FileReader.load_positif(),
            'negatif': FileReader.load_negatif(),
            'neutre': FileReader.load_neutre()
        }