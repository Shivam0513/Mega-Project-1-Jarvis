from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)