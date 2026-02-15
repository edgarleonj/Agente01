from dotenv import load_dotenv
from groq import Groq
import os


load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    print("❌ Error: No se encontró la GROQ_API_KEY en el archivo .env")
    exit()

client = Groq(api_key=api_key)


print("Hello, World!")


messages = [
    {"role": "user", "content": "You are a helpful assistant."},
]

resp = client.chat.completions.create(model="qwen/qwen3-32b", messages=messages)

#msg = resp.choices[0].message.content
#assistant_text = msg.content or ""
#print(f"Asistente: {assistant_text}")

# La forma correcta para la versión actual de la librería:
assistant_text = resp.choices[0].message.content
print(assistant_text)