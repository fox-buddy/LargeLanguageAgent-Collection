from ollama import chat
from pydantic import BaseModel, Field
from pathlib import Path

# Read File

markdown_directory = Path("markdown")
input_prompt = ""

with (markdown_directory/"markdownresult.md").open("r", encoding="utf-8") as markdownfile:
    input_prompt = markdownfile.read()



# Defining Invoice Object
class Invoice_Item(BaseModel):
    position_article_number: int = Field(default=0, examples=[1, 2, 38, 482])
    position_article_name: str = Field(default="", examples=["Arbeiten", "Ziegel", "Erdarbeiten", "Computerteile"])
    position_amount: float = Field(default=0.0, examples=[1.0, 2.5, 3.0 , 48.34, 65.0, 85, 2])
    position_single_price: float = Field(default=0.0, examples=[23.00, 2.54, 38.0, 482.21, 1.0, 5])


class Invoice_Header(BaseModel):
    invoice_number: str = Field(default="", examples=["35846", "RE-4562"])
    invoice_date: str = Field(default="", examples=["09.12.2024", "4.8.25"])
    invoice_total: float = Field(default=0.0, examples=[1289.94, 0.0, 45.80, 23])
    recipient_name: str = Field(default="", examples=["Thomas Fischer"])
    recipient_address: str = Field(default="")
    billers_name: str = Field(default="", examples=["Sowas GmbH", "Super Duper Dienstleistungen", "Software Produkte AG"])
    billers_address: str = Field(default="")


class Extracted_Invoice_Data(BaseModel):
    invoice_header: Invoice_Header = Field(default=Invoice_Header(), examples=[Invoice_Header()])
    invoice_items: list[Invoice_Item]


chat_response = chat(
    model='deepseek-r1:latest',
    messages=[{'role': 'user', 'content': input_prompt}],
    format=Extracted_Invoice_Data.model_json_schema(),
)



invoice_data = Extracted_Invoice_Data.model_validate_json(chat_response.message.content)
print(invoice_data)