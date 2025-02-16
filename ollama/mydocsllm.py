import os
import ollama
print(dir(ollama))

def ingest_documents(directory):
    myOllama = ollama(api_key='C:/Users/todd/.ollama/id_ed25519.pub')  # Replace with your Ollama API key
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.docx') or file.endswith('.pdf') or file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    content = f.read()
                    myOllama.ingest_document(content)

if __name__ == "__main__":
    one_drive_directory = 'C:/Users/todd/OneDrive/Documents'
    ingest_documents(one_drive_directory)