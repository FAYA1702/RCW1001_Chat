from langchain_ollama import OllamaLLM
import time
 
model = OllamaLLM(model="llama3.2")
 
user_input = "Qui est le président du Canada ?"
 
result = model.invoke(user_input)
 
for char in result:
    print(char, end="", flush=True)
    time.sleep(0.02)
print()