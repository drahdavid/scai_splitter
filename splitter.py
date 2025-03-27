from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List, Optional
import argparse


class TextChunkSplitter:
    def __init__(
        self,
        chunk_size: int = 100,
        chunk_overlap: int = 0,
        length_function: Optional[callable] = len,
    ):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=length_function,
        )

    def split_text(self, text: str) -> List[str]:

        if not text or not text.strip():
            return []

        try:
            return self.text_splitter.split_text(text)
        except Exception as e:
            print(f"Error splitting text: {e}")
            return []

    def split_texts(self, texts: List[str]) -> List[str]:
        all_chunks = []
        for text in texts:
            chunks = self.split_text(text)
            all_chunks.extend(chunks)
        return all_chunks


def main():
    parser = argparse.ArgumentParser(description="Split text into chunks")
    parser.add_argument(
        "--chunk-size", type=int, default=100, help="Maximum size of each chunk"
    )
    parser.add_argument(
        "--overlap", type=int, default=0, help="Number of characters to overlap"
    )
    args = parser.parse_args()

    # Example text
    sample_text = """
    Lorem Ipsum is simply dummy text of the  printing and typesetting industry.
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
    when an unknown printer took a galley of type and scrambled it to make a type specimen book.
    It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of
    Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing
    software like Aldus PageMaker including versions of Lorem Ipsum.
    """

    # Create splitter instance
    splitter = TextChunkSplitter(
        chunk_size=args.chunk_size,
        chunk_overlap=args.overlap,
    )

    # Split text and print chunks
    chunks = splitter.split_text(sample_text)
    print(f"\nSplit into {len(chunks)} chunks:")
    for i, chunk in enumerate(chunks, 1):
        print(f"\nChunk {i}:")
        print(chunk)
        print("-" * 50)


if __name__ == "__main__":
    main()
