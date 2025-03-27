from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn
import argparse
from splitter import TextChunkSplitter

app = FastAPI(title="Text Splitter API")


class SplitTextRequest(BaseModel):
    text: str
    chunk_size: int = 100
    chunk_overlap: int = 0


class SplitTextResponse(BaseModel):
    chunks: List[str]


@app.post("/split", response_model=SplitTextResponse)
def split_text_endpoint(request: SplitTextRequest):
    splitter = TextChunkSplitter(
        chunk_size=request.chunk_size,
        chunk_overlap=request.chunk_overlap
    )
    chunks = splitter.split_text(request.text)
    return SplitTextResponse(chunks=chunks)


def main():
    parser = argparse.ArgumentParser(description="Start the Text Splitter API server")
    parser.add_argument(
        "--port", type=int, default=9000, help="Port for API server"
    )
    args = parser.parse_args()
    
    uvicorn.run(app, host="0.0.0.0", port=args.port)


if __name__ == "__main__":
    main()
