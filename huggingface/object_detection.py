from transformers import pipeline
from accelerate import Accelerator

task_name = 'object_deteaction'
accelerator_id = Accelerator().device


print(f"Hello to a huggingface pipeline Example for {task_name}")
print(f"Fastest Device is {accelerator_id}")


model_id = 'hustvl/yolos-tiny'
# facebook/detr-resnet-50
# 'hustvl/yolos-tiny' 188 GB --> 

pipeline_worker = pipeline(model=model_id)

detection_result = pipeline_worker("https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png")

print(detection_result)