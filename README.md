# API Splitter de Texto

Este proyecto proporciona una API simple para dividir texto en fragmentos utilizando `RecursiveCharacterTextSplitter` de `langchain`.
También incluye un modo CLI para el procesamiento directo de texto.

## Características

- Divide texto en fragmentos con un tamaño y superposición definidos.
- Punto de acceso API para procesar solicitudes de texto.
- Interfaz de línea de comandos (CLI) para el procesamiento directo de texto.

## Requisitos

- Python 3.8+
- FastAPI
- Uvicorn
- Langchain
- Pydantic

## Instalación

1. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

## Estructura del Proyecto

- `splitter.py`: Implementación core del divisor de texto
- `api_server.py`: Servidor API FastAPI

## Ejecutar el Servidor API

Para iniciar el servidor API, ejecuta:

```sh
python api_server.py
```

Por defecto, el servidor se ejecuta en `http://0.0.0.0:9000`. Puedes cambiar el puerto usando la opción `--port`:

```sh
python api_server.py --port 8000
```

### Punto de acceso API

#### `POST /split`

Divide el texto dado en fragmentos según el tamaño de fragmento y la superposición especificados.

**Cuerpo de la solicitud:**

```json
{
  "text": "Tu texto largo aquí...",
  "chunk_size": 100,
  "chunk_overlap": 10
}
```

**Respuesta:**

```json
{
  "chunks": ["Texto del fragmento 1...", "Texto del fragmento 2..."]
}
```

## Ejecutar en Modo CLI

Puedes usar el script en modo CLI para dividir texto de ejemplo:

```sh
python splitter.py --chunk-size 100 --overlap 10
```
