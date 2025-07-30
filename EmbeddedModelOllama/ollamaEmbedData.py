import ollama
import chromadb

###################################################################
#####                  Generating Embeddings                  #####
#####   This part should be done while initializing an API    #####
###################################################################

# This could also be Text that is retrieved from pdf Documents or HTML Pages
documents = [
    "Go ist eine von Google entwickelte Programmiersprache, die sich durch ihre Einfachheit, Geschwindigkeit und starke Parallelisierungsunterstützung auszeichnet.",
    "Die Syntax von Go ist übersichtlich und leicht zu erlernen, was den Einstieg auch für Anfänger erleichtert.",
    "In Go werden sogenannte Goroutinen verwendet, um parallele Abläufe effizient zu realisieren.",
    "Go besitzt ein starkes Typensystem und prüft viele Fehler bereits zur Compilezeit.",
    "Die Standardbibliothek von Go bietet umfangreiche Funktionen für Netzwerke, Datenbanken und Datenverarbeitung.",
    "Um eine Vektordatenbank zu bauen, empfiehlt sich der Einsatz von Slices und Maps, um dynamische Datenstrukturen zu verwalten.",
    "Für numerische Berechnungen und lineare Algebra kann man auf externe Bibliotheken wie Gonum zurückgreifen.",
    "Die Speicherverwaltung in Go erfolgt automatisch über Garbage Collection, was die Entwicklung vereinfacht.",
    "Mit Go lässt sich leicht eine REST-API implementieren, um Datenbankoperationen bereitzustellen.",
    "Für persistente Speicherung können Datenbanken wie SQLite, PostgreSQL oder spezielle NoSQL-Datenbanken über Go-Driver angebunden werden.",
    "Beim Aufbau einer Vektordatenbank sollte man auf effiziente Such- und Vergleichsalgorithmen achten, z.B. für die Annäherung von Vektoren (ANN).",
    "Es gibt Open-Source-Projekte wie Weaviate oder Milvus, die sich als Inspiration für eigene Implementierungen eignen und Go-Schnittstellen bieten.",
    "Go-Module ermöglichen das einfache Verwalten von Abhängigkeiten und das Teilen des eigenen Codes.",
    "Mit dem eingebauten Testing-Framework von Go kann die eigene Datenbank effizient getestet werden.",
    "Das Kompilieren von Go-Programmen ergibt statisch gelinkte Binärdateien, die sich einfach deployen lassen.",
]

client = chromadb.Client()
collection = client.create_collection(name="docs")


# Storing each Document in an embedded database
for idx, document in enumerate(documents):
    response = ollama.embed(model="mxbai-embed-large", input=document)
    #print(response["embeddings"][0])
    embeddings = response["embeddings"][0]

    # add embeddings with index to collection and link them do the document. Embeddings are numerical vectors that represent semantic meanings of text
    collection.add(ids=str(idx), embeddings=embeddings, documents=[document])


###################################################################
#####                Retrieve from Embeddings                 #####
#####                   Part of an Endpoint                   #####
###################################################################


# Example Input
user_input = "Welche Datenbanken kann ich bei Entwicklung mit Go zur persistenten Speicherung benutzen?"

# Embed Input to respresent it as numerical vector
input_empbedded = ollama.embed(model="mxbai-embed-large", input=user_input)

#print(inp_response.embeddings)[0]

# Search in documents for most relevant document
results = collection.query(
    query_embeddings=[input_empbedded["embeddings"][0]], n_results=1
)

#print(input_empbedded)

data = results['documents'][0][0]

# print(results)

###################################################################
#####                 Generate Text with LLM                  #####
#####                   Part of an Endpoint                   #####
###################################################################
# Important note: this is not the same model, that we used to generate embeddings
# This is a Text Model
output = ollama.generate(
    model="llama3.1",
    prompt=f"Benutze diese Daten: {data}. To Respont to this Prompt: {user_input}"
)


print(output.response)