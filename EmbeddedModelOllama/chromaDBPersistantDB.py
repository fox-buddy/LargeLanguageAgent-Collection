import chromadb
import pdfquery
import ollama
import sys

# Create persistent Client
# File will be created if not yet exists
try:
    client = chromadb.PersistentClient(path="C:/Users/Torst/Documents/GitHub/LargeLanguageAgent-Collection/EmbeddedModelOllama/chromafiles")
    collection = client.create_collection(name="btccol")
except Exception as err_client:
    print(f"Error creating Client")
    print(err_client)

    sys.exit(0)




# Read pdf file
btc_wp = pdfquery.PDFQuery('C:/Users/Torst/Documents/GitHub/LargeLanguageAgent-Collection/EmbeddedModelOllama/bitcoinwp.pdf')
btc_wp.load()

# convert to xml and export to file --> If we want to check the contents to extract
# btc_wp.tree.write('C:/Users/Torst/Documents/GitHub/LargeLanguageAgent-Collection/EmbeddedModelOllama/btc_wp_xml', pretty_print = True)

# extract the lines of text
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

            collection.add(ids=str(idx), embeddings=embeddings, documents=[document_text])
            print(f"processed {idx}")
    except Exception as err_embed:
        print(f"Something went wrong while embedding:  {err_embed}")
        print(document_text)


