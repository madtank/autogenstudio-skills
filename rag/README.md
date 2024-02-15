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

## Usage

Both the indexing and retrieval scripts are intended for local use to ensure they function correctly with your dataset before integrating them as skills in AutoGen Studio.

### Document Indexing

To index your documents for the first time or to update the index:

1. Add any new document files to the `documents` directory.
2. Run the `document_indexer.py` script, which will automatically index the documents and update the `knowledge` folder.

### Document Retrieval Usage Instructions

The `document_retriever.py` script facilitates the retrieval of documents based on a specified query. Follow the steps below to utilize the script for your document retrieval needs:

1. **Prepare the Environment:**
   Ensure that all necessary dependencies are installed, including `tiktoken`, `langchain-community`, `FAISS`, and `HuggingFaceEmbeddings`. If you haven't installed these yet, use `pip` to install them or refer to their respective documentation for installation instructions.

2. **Configure the Index Path:**
   Before running the script, make sure to set the `index_folder` in the CONFIG variable to point to the directory containing your FAISS index and the `chunk_id_to_index.pkl` file.

3. **Set Up the Query Parameters:**
   - Open the `document_retriever.py` file in your preferred text editor.
   - Scroll to the bottom of the file and locate the `if __name__ == "__main__":` section.
   - Within this section, you will find the `query`, `size`, and `target_length` parameters.
   - Modify the `query` parameter to reflect the text you want to search for.
   - Adjust the `size` parameter to control the number of results you want to retrieve.
   - Set the `target_length` parameter to determine the length of text surrounding your query match within the retrieved documents.

4. **Execution:**
   - Save the file after making the necessary changes.
   - Run the script from the command line by executing `python document_retriever.py` followed by your search query in quotes (e.g., `python document_retriever.py "example search query"`).
   - If your setup is correct, the script will output the retrieved documents formatted in JSON.


Certainly, here's a streamlined update for integrating the `document_retriever.py` skill into AutoGenStudio, focusing on the Build > Skills section:

---

## Integration with AutoGenStudio for GPT-4

To integrate the `document_retriever.py` skill with AutoGenStudio for use in GPT-4 workflows:

1. **Create a New Skill:**
   - Navigate to the Build > Skills section within AutoGenStudio.
   - Create a new skill and give it a relevant name that easily identifies its purpose, such as "Document Retriever".

2. **Add the Python Script:**
   - Copy the content of the `document_retriever.py` script into the code area of the new skill.
   - Ensure that the script is complete and correctly formatted to run as a standalone skill within the AutoGenStudio environment.

3. **Configure the Index Path:**
   - Locate the CONFIG variable within the script.
   - Update the `"index_folder"` key to point to your specific directory containing the FAISS index and associated files. This path must be accessible from within the AutoGenStudio environment.

5. **Incorporate Into Workflow:**
   - Once testing is successful, incorporate the skill into your desired workflow.
   - Set up instructions within the agent that will prompt the skill to execute when needed.

### Additional Notes:

- Ensure that the path to the `index_folder` is accessible from the environment where the script is being run.
- If any changes are made to the indexing structure or if new documents are added to the database, make sure to update the FAISS index accordingly.
- The output is in JSON format for easy integration with other systems or for further processing.

By following these instructions, you should be able to successfully retrieve documents using the `document_retriever.py` script. If you encounter any issues, review the configuration steps to ensure all settings are correct.

## Contributing

Contributions to improve these skills or extend their capabilities are welcome. Please submit pull requests or open issues to discuss potential enhancements.
