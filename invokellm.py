from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

response = llm.invoke("How many bits in a byte?")

print(response)