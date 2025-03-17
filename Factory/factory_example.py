from abc import ABC, abstractmethod

# Product interface: Document
class Document(ABC):
    @abstractmethod
    def read(self):
        pass

# Concrete Product: PDF Document
class PDFDocument(Document):
    def read(self):
        print("Reading PDF document")

# Concrete Product: Word Document
class WordDocument(Document):
    def read(self):
        print("Reading Word document")

# Creator abstract class with a factory method
class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self, doc_type: str) -> Document:
        pass

# Concrete Creator that implements the factory method
class ConcreteDocumentFactory(DocumentFactory):
    def create_document(self, doc_type: str) -> Document:
        if doc_type.lower() == 'pdf':
            return PDFDocument()
        elif doc_type.lower() == 'word':
            return WordDocument()
        else:
            raise ValueError("Unknown document type")

# Client code demonstrating the usage of the factory
if __name__ == "__main__":
    factory = ConcreteDocumentFactory()
    
    # Create and use a PDF document
    pdf_doc = factory.create_document("pdf")
    pdf_doc.read()
    
    # Create and use a Word document
    word_doc = factory.create_document("word")
    word_doc.read()
