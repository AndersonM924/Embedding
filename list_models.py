# list_models.py
import google.generativeai as genai
from config import GEMINI_API_KEY

def main():
    # Configurar API Key
    genai.configure(api_key=GEMINI_API_KEY)

    # Listar modelos
    modelos = genai.list_models()

    # Imprimir nombre y descripción breve
    print("Modelos disponibles en Gemini:\n")
    for m in modelos:
        # El objeto 'Model' expone atributos, no dict
        nombre = getattr(m, 'name', '<sin nombre>')
        descripcion = getattr(m, 'description', '')
        print(f"- {nombre}: {descripcion}")

if __name__ == "__main__":
    main()
