# db.py
import logging
from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY
from postgrest.exceptions import APIError

# Configuración de logging
type_logging = logging.INFO
logging.basicConfig(level=type_logging,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def obtener_client() -> Client:
    """
    Crea y devuelve un cliente de Supabase autenticado con la service_role key.
    """
    return create_client(SUPABASE_URL, SUPABASE_KEY)


def actualizar_embedding(
    client: Client,
    tabla: str,
    campo_vector: str,
    record_id: str,
    embedding: list[float]
) -> None:
    """
    Actualiza el campo vectorial de un registro existente en Supabase.

    Parámetros:
    - client: instancia de Supabase Client.
    - tabla: nombre de la tabla (p. ej., 'job_position').
    - campo_vector: nombre de la columna de tipo vector donde se almacenará el embedding.
    - record_id: valor de la clave primaria (id) del registro a actualizar.
    - embedding: lista de floats representando el vector.

    Lanza RuntimeError si ocurre un error durante la actualización.
    """
    try:
        # Ejecutar actualización
        respuesta = (
            client
            .table(tabla)
            .update({campo_vector: embedding})
            .eq("id", record_id)
            .execute()
        )
        # Verificar datos devueltos
        if respuesta.data:
            logger.info(
                f"Registro con id={record_id} actualizado correctamente en '{tabla}'."
            )
        else:
            logger.warning(
                f"Registro con id={record_id} no encontrado en '{tabla}', no se actualizó nada."
            )
    except APIError as api_err:
        logger.error(
            f"APIError al actualizar registro id={record_id} en '{tabla}': {api_err}"
        )
        raise RuntimeError(f"Error al actualizar Supabase: {api_err}")
    except Exception as exc:
        logger.exception(
            f"Excepción inesperada al actualizar embedding para id={record_id}: {exc}"
        )
        raise
