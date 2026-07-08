# from openai import OpenAI

# client = OpenAI(
#     base_url="http://127.0.0.1:11434/v1",
#     api_key="ollama"   # Can be any string; Ollama ignores it.
# )

# completion = client.chat.completions.create(
#     model="llama3.2",   # Or "qwen2.5:1.5b" if you've downloaded it.
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a virtual assistant, Jarvis skilled in tasks like Alexa."
#         },
#         {
#             "role": "user",
#             "content": "What is malaria?"
#         }
#     ]
# )

# print(completion.choices[0].message.content)