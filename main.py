# main.py
import argparse
from embeddings import generar_embedding
from db import obtener_client, actualizar_embedding

def parse_args():
    parser = argparse.ArgumentParser(
        description="Genera un embedding de un texto y lo actualiza en Supabase."
    )
    parser.add_argument(
        "-t", "--texto",
        type=str,
        required=True,
        help="Texto completo a procesar entre comillas."
    )
    parser.add_argument(
        "-i", "--id",
        type=str,
        required=True,
        help="ID del registro en public.job_position a actualizar."
    )
    return parser.parse_args()

def main():

    texto = "Ciudad donde es carlos galan"
    vector = generar_embedding(texto)
    print(f"Embedding generado (longitud {len(vector)})")

    # 3. Actualizar el registro en Supabase
    client = obtener_client()
    tabla = "city"
    campo_vector = "embedding"
    record_id = "71f46529-1a34-459a-90e5-52b885c50b4d"

    try:
        actualizar_embedding(client, tabla, campo_vector, record_id, vector)
        print("Registro actualizado correctamente en Supabase.")
    except RuntimeError as err:
        print(err)

if __name__ == "__main__":
    main()
