from docling.document_converter import DocumentConverter
from pathlib import Path

source = "https://arxiv.org/pdf/2408.09869"

converter = DocumentConverter()
result = converter.convert(source)

##print(result.document.export_to_markdown())


output_dir = Path("scratch")
output_dir.mkdir(parents=True, exist_ok=True)

doc_filename = 'markdownresults'

with (output_dir / f"{doc_filename}.txt").open("w", encoding="utf-8") as fp:
        fp.write(result.document.export_to_markdown(strict_text=True))



# This will result in a markdown file with some headlines (level two --> ##)
# A useful case would be to separate the documents based on the headlines and read in the whole paragraph --> Then query the embedded paragraphs with an embedded input