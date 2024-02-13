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

Alright, if the example usage is already part of your `document_retriever.py` script and users just need to update it with their specific details, the `README.md` should instruct users to modify the example code directly in the script. Here's how you can present that in the `README.md`:

---

## Usage

Both the indexing and retrieval scripts are intended for local use to ensure they function correctly with your dataset before integrating them as skills in AutoGen Studio.

### Document Indexing

To index your documents for the first time or to update the index:

1. Add any new document files to the `documents` directory.
2. Run the `document_indexer.py` script, which will automatically index the documents and update the `knowledge` folder.

### Document Retrieval

The `document_retriever.py` script contains a sample usage example at the bottom of the file. To test document retrieval:

1. Open `document_retriever.py` in a text editor.
2. Locate the example usage section.
3. Update the `query`, `size`, and `target_length` variables with the details relevant to your search.
4. Save the changes and run the script:

```bash
python document_retriever.py
```

This will execute the retrieval function with your specified parameters and print the results.

After confirming the scripts work with your local setup, you can upload them as skills to AutoGen Studio, ensuring the `index_folder` parameter correctly points to your knowledge base.

## Integration with AutoGenStudio

These skills can be integrated into AutoGenStudio workflows by defining them as custom skills within the AutoGenStudio environment. Refer to the AutoGenStudio documentation on how to incorporate custom Python scripts as skills.

## Contributing

Contributions to improve these skills or extend their capabilities are welcome. Please submit pull requests or open issues to discuss potential enhancements.
