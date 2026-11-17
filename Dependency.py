class Document:
    def __init__(self, content):
        self.content = content

class Printer:
    def print_document(self, document):
        return document.content

my_doc = Document("Hello, World!")
my_printer = Printer()

print(my_printer.print_document(my_doc))