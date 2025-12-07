#from pathlib import Path

#from pydantic import BaseModel, Field
from rich import print
from docling.datamodel.base_models import InputFormat
from docling.document_extractor import DocumentExtractor


source_file_path = (".\Endrechnung 180252 David.pdf")


extractor = DocumentExtractor(allowed_formats=[InputFormat.PDF, InputFormat.IMAGE])

# Extract with String Template

string_extract_result = extractor.extract(
    source=source_file_path
    , template='{"Endrechnung": "int", "Rechnungsbetrag": "float"}'
)

print(string_extract_result)

#pip install hf_xet