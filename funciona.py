import requests

api_key = "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"  # Reemplaza con tu propia API key de OpenAI

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "prompt": "¡Hola, OpenAI!",
    "max_tokens": 5
}

response = requests.post("https://api.openai.com/v1/engines/davinci-codex/completions", json=data, headers=headers)

if response.status_code == 200:
    print("La API key está funcionando correctamente.")
else:
    print("Hubo un problema al realizar la solicitud. Asegúrate de que la API key sea válida y esté activa.")
