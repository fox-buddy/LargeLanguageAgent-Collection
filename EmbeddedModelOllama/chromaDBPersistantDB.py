from tools.PDFdocVectorDatabaseFactory import PDFdocVectorDatabaseFactory
import sys
import ollama

###################################################################
#####              Retrieve or Create Database                #####
###################################################################
# In this example the collection is created or retrieved (if already exists) by a Factory Class
# The Instance acts as the interface to the vector store

try:
    btc_vector_db = PDFdocVectorDatabaseFactory("btccol", "C:/Users/Torst/Documents/GitHub/LargeLanguageAgent-Collection/EmbeddedModelOllama/bitcoinwp.pdf")
    print("Retrieved Vecor Database")
except Exception as err_db:
    print("Error creating or getting Vector Database")
    print(err_db)
    sys.exit(1)


###################################################################
#####                Retrieve from Embeddings                 #####
###################################################################
while 1 == 1:
    usr_input = input("What do you want to know from this embedded model. Type exit to close example application: ")

    if usr_input == "exit":
        break
    
    # Embed Inputn before we search in Vecor Database
    # Model must be pulled before we want to work with it
    input_embedded = ollama.embed(model="mxbai-embed-large", input=usr_input)

    results = btc_vector_db.collection.query(
        query_embeddings=[input_embedded["embeddings"][0]], n_results=10
    )

    # This is an array of strings
    data = results['documents'][0]

    # This is a string combined from an array input --> The Results are much better
    separator = '/'
    data_combined = separator.join(data)

    # print(data)


    ###################################################################
    #####                 Generate Text with LLM                  #####
    ###################################################################
    # Important note: this is not the same model, that we used to generate embeddings
    # This is a Text Model
    output = ollama.generate(
        model="llama3.1",
        prompt=f"Benutze diese Daten: {data_combined}. To Respont to this Prompt: {usr_input}"
    )


    print(output.response)