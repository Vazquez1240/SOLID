# Problema
# La clase FileManager esta encargada de leer y escribir archvios, asi como cargar el contenido 

# Codigo que no cumple SRP

class FileManager:
    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    
    def write_file(self, file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)
    
    def counts_words(self, content):
        return len(content.split())
    
    
# Solucion se paramos la responsabilidad de procesar el contenido en una clase separada llamada ContentProcessor

# Codigo que cumple SRP

class FileManagerSRP:
    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    
    def write_file(self, file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)
            
    class ContentProcessor:
        @staticmethod
        def counts_words(content):
            return len(content.split())