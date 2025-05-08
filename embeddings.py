# embeddings.py
from typing import List
import google.generativeai as genai
from config import GEMINI_API_KEY

# Configuramos la API key al importar el módulo
genai.configure(api_key=GEMINI_API_KEY)

def generar_embedding(texto: str) -> List[float]:
    """
    Genera un vector de embedding a partir de un texto usando el modelo seleccionado de Gemini.
    """
    resultado = genai.embed_content(
        model="models/text-embedding-004",
        content=texto,
        task_type="SEMANTIC_SIMILARITY"
    )
    return resultado["embedding"]
