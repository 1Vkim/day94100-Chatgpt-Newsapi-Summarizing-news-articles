import requests
import os,json

newsKey = os.environ['newsapi']
country = "us"

url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"

result = requests.get(url)
data = result.json()


def ask_chatgpt(prompt, api_key, max_tokens=15, temperature=0.7, engine="davinci"):
  url = "https://api.openai.com/v1/chat/completions"
  headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
  }
  data = {

      "max_tokens": max_tokens,
      "temperature": temperature,

      "model": "gpt-3.5-turbo",
      "messages": [{"role": "system", "content": prompt}]# Use prompt as the content of the message
    }

  response = requests.post(url, json=data, headers=headers)

  if response.status_code == 200:
      return response.json()["choices"][0]["message"]["content"].strip() # Access the generated text
  else:
      print("Error:", response.text)
      return None




count=0
for article in data["articles"]:
  if "content" in article and article["content"]:
    api_key = os.environ['openaikey']
    prompt = "Summarize: " + article["content"]
    response = ask_chatgpt(prompt, api_key)
    print(article["title"])
    print("A:", response)
    count+=1
    if count==5:
      break

  else:
    print("Skipping article due to missing content:", article["title"])
  



