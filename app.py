from transformers import pipeline

print("Loading AI model... Please wait")

generator = pipeline("text-generation", model="gpt2")

print("Model Loaded Successfully!")
print("----------------------------------")

while True:
    
    prompt = input("Enter a topic (or type exit): ")

    if prompt.lower() == "exit":
        print("Exiting program...")
        break

    print("\nGenerating text...\n")

    result = generator(
        prompt,
        max_length=120,
        num_return_sequences=1
    )

    generated_text = result[0]["generated_text"]

    print("AI Generated Text:\n")
    print(generated_text)
    print("\n----------------------------------\n")
