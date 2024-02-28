def ask_chatgpt(prompt, api_key, max_tokens=50, temperature=0.7, engine="davinci"):
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

# Example usage:
api_key = os.environ['openaikey']
prompt = "Q: What is the meaning of life?"
response = ask_chatgpt(prompt, api_key)
print("A:", response)
