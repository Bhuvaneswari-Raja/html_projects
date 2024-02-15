import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the meaning of life?"}
  ]
)

print(completion.choices[0].message)

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Classify user messages as positive or negative sentiment."},
    {"role": "user", "content": "This course I'm taking on machine learning is so great!"}
  ]
)

print(completion.choices[0].message)

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  temperature = 0.2,
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a joke."}
  ]
)

print(completion.choices[0].message)

