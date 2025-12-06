from pathlib import Path

from docling.document_converter import DocumentConverter

source = ".\Endrechnung 180252 David.pdf"

converter = DocumentConverter()
doc = converter.convert(source).document

print(doc.export_to_markdown())


print()
print()
print("Now i export!")


output_dir = Path("markdown")
output_dir.mkdir(parents=True, exist_ok=True)

with (output_dir/f"markdownresult.md").open("w", encoding="utf-8") as dest_file:
    dest_file.write(doc.export_to_markdown())




## Try to perform with ollama and different invoices
## Process markdown with a Large Language Modell --> Output has to be consitent to process further
## the invoice items, especially article informations like name and number, should be checked against a rest api
## Insert if not present, update if present (Backend must handle price history)
## Insert Invoice Detail somewhere --> Data Warehouse (API should be present)
