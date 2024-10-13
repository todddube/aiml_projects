import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": "Tell me an interesting fact about elephants",
        },
    ],
)
print(response["message"]["content"])
stat = ollama.stop("llama3)
                   
print (state)