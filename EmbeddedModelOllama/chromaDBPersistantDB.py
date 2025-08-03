from tools.PDFChromLoader import DocumentEmbedderPdf
import sys

# Create persistent Client
# File will be created if not yet exists

try:
    btc_vector_db = DocumentEmbedderPdf("btccol", "C:/Users/Torst/Documents/GitHub/LargeLanguageAgent-Collection/EmbeddedModelOllama/bitcoinwp.pdf")
except Exception as err_db:
    print("Error creating or getting Vector Database")
    print(err_db)
    sys.exit(1)