from transformers import pipeline
from accelerate import Accelerator

task_name = 'Text Generation'
device_id = Accelerator().device

print(f"Hello to a huggingface pipeline Example for {task_name}")
print(f"Fastest Device is {device_id}")


model_id = "openai-community/gpt2"  
# openai-community/gpt2
# Qwen/Qwen2.5-Omni-3B
# LilaRest/gemma-4-31B-it-NVFP4-turbo
# openai/gpt-oss-120b


# we should login with a token (env variable --> see documentation. Because here we download the model per clear text request)
transformer_worker = pipeline(task="text-generation", model=model_id)

model_response = transformer_worker(["tell me a little riddle"])


print(model_response)