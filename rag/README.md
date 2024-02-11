# AutoGenStudio Document Management Skills

This repository contains two Python scripts designed as skills for AutoGenStudio, a framework for building and managing autonomous AI systems. These skills enable the indexing of documents and retrieval based on relevance, facilitating efficient document management within an AI-driven environment.

## Skills Overview

- `document_indexer.py`: This script is responsible for indexing documents, preparing them for quick and efficient retrieval. It processes documents, extracts relevant information, and creates an index that maps document content to their storage locations.

- `document_retriever.py`: Utilizes the indexes created by `document_indexer.py` to fetch documents based on queries. It ranks documents by relevance to the query, providing an interface for efficient document retrieval in the context of AI-driven tasks or workflows.

## Installation

Before using these skills, ensure you have the required dependencies installed. These scripts rely on external libraries for document processing and index management.

```bash
pip install beautifulsoup4 requests langchain-community tiktoken
```

Note: Replace the above dependencies with the actual ones required by the scripts, as my access does not include the ability to verify their content.

## Usage

### Document Indexing

To index your documents, navigate to the directory containing `document_indexer.py` and run:

```bash
python document_indexer.py --doc_path "/path/to/documents"
```

Replace `/path/to/documents` with the actual path to your documents. The script will process and index the documents, preparing them for retrieval.

### Document Retrieval

After indexing, you can retrieve documents by running `document_retriever.py` with a query:

```bash
python document_retriever.py --query "example search query"
```

The script will return documents that match the query based on the indexes created earlier.

## Integration with AutoGenStudio

These skills can be integrated into AutoGenStudio workflows by defining them as custom skills within the AutoGenStudio environment. Refer to the AutoGenStudio documentation on how to incorporate custom Python scripts as skills.

## Contributing

Contributions to improve these skills or extend their capabilities are welcome. Please submit pull requests or open issues to discuss potential enhancements.
