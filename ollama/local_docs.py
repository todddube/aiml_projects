from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader("C:/Users/todd/OneDrive/Desktop/Todd Dube Resume 2024 KMX.docx")
books = loader.load()
len(books)