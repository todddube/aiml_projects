from gpt4all import GPT4All 

# device='amd', device='intel'
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf", device='gpu') 
 
output = model.generate("The capital of France is ", max_tokens=3) 
print(output)