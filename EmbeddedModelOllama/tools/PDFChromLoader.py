import chromadb
import pdfquery
import ollama

class DocumentEmbedderPdf:

    def __init__(self, colname="btccol", pdfpath="C:/Users/Torst/Documents/GitHub/LargeLanguageAgent-Collection/EmbeddedModelOllama/bitcoinwp.pdf"):
        self.collection: any
        self.collection_name = colname
        self.client: any

        self.chroma_path = "C:/Users/Torst/Documents/GitHub/LargeLanguageAgent-Collection/EmbeddedModelOllama/chromafiles"
        
        self.pdf_path = pdfpath

        try:
            self.client = chromadb.PersistentClient(path=self.chroma_path)
            self.collection = self.client.create_collection(name=self.collection_name)
            self.load_pdf_file_to_embedd()
        except Exception as err_client:
            print(f"There was an error creating collection. We try to retrieve existing one: {err_client}")
            self.collection = self.try_to_get_existing_collection()
            print("Existing Collection Retrieved")

    def try_to_get_existing_collection(self):
        try:
            return self.client.get_collection(name=self.collection_name)
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
            except Exception as err_inner_text:
                print(f"something went wrong while retrieving inner Text: {err_inner_text}")

            try:
                if(document_text):
                    response = ollama.embed(model="mxbai-embed-large", input=document_text)
                    embeddings = response["embeddings"][0]

                    self.collection.add(ids=str(idx), embeddings=embeddings, documents=[document_text])
                    print(f"processed {idx}")
            except Exception as err_embed:
                print(f"Something went wrong while embedding document:  {err_embed}")
                print(document_text)






    
