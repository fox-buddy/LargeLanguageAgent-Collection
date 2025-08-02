import chromadb
import pandas as pd
import pdfquery

# Create persistent Client
# File will be created if not yet exists
client = chromadb.PersistentClient(path="./chromafiles")
collection = client.create_collection(name="example")


# Check if connection still exists
# keepAlive = client.heartbeat()

# Read pdf file
btc_wp = pdfquery.PDFQuery('bitcoinwp.pdf')
btc_wp.load()


# convert to xml and print
btc_wp.tree.write('btc_wp_xml', pretty_print = True)


