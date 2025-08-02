import chromadb
import pdfquery
import ollama
import sys

class PDFChromaLoader:

    def __init__(self):
        self.collection: any
        self.client: any
        self.chroma_path = "C:/Users/Torst/Documents/GitHub/LargeLanguageAgent-Collection/EmbeddedModelOllama/chromafiles"
        self.pdf_path = "C:/Users/Torst/Documents/GitHub/LargeLanguageAgent-Collection/EmbeddedModelOllama/bitcoinwp.pdf"

        try:
            self.client = chromadb.PersistentClient(path=self.chroma_path)
            self.collection = self.client.create_collection(name="btccol")
            self.load_pdf_file_to_embedd()
        except Exception as err_client:
            print(f"There was an error creating collection. We try to retrieve existing one: {err_client}")
            self.collection = self.try_to_get_existing_collection()

    def try_to_get_existing_collection(self):
        try:
            return self.client.get_collection(name="btccol")
        except Exception as e:
            raise(e)
       
    def load_pdf_file_to_embedd(self):
        btc_wp = pdfquery.PDFQuery(file=self.pdf_path)
        btc_wp.load()

        lines_of_pdf = btc_wp.pq('LTTextLineHorizontal')

        for idx, text_line in enumerate(lines_of_pdf):
            document_text = ''
            try:
                document_text = text_line.text
            except Exception as err_file:
                print(f"something went wrong while embedding the pdf document line: {err_file}")

            try:
                if(document_text):
                    response = ollama.embed(model="mxbai-embed-large", input=document_text)
                    embeddings = response["embeddings"][0]

                    self.collection.add(ids=str(idx), embeddings=embeddings, documents=[document_text])
                    print(f"processed {idx}")
            except Exception as err_embed:
                print(f"Something went wrong while embedding:  {err_embed}")
                print(document_text)






    
