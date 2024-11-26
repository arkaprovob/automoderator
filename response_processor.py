from mock_data import mock_response

class Document:
    def __init__(self, documentKind, path, title, abstract, sortTitle, rerank_score, original_rank):
        self.documentKind = documentKind
        self.path = path
        self.title = title
        self.abstract = abstract
        self.sortTitle = sortTitle
        self.rerank_score = rerank_score
        self.original_rank = original_rank

    def __str__(self):
        return f"Document(title='{self.title}', rank={self.original_rank})"

    def __repr__(self):
        return self.__str__()


def extract_doc_info(json_data):
    try:
        # Get the docs array directly from the response section
        docs = json_data['response']['docs']

        # Create list of Document objects
        doc_list = [
            Document(
                documentKind=doc['documentKind'],
                path=doc['path'],
                title=doc['title'],
                abstract=doc['abstract'],
                sortTitle=doc['sortTitle'],
                rerank_score=doc['rerank_score'],
                original_rank=doc['original_rank']
            )
            for doc in docs
        ]

        return doc_list

    except Exception as e:
        print(f"Error processing JSON data: {e}")
        return []


# Extract the documents example
documents = extract_doc_info(mock_response)

# Print the documents
for doc in documents:
    print(f"Document Kind: {doc.documentKind}")
    print(f"Title: {doc.title}")
    print(f"Path: {doc.path}")
    print(f"Abstract: {doc.abstract}")
    print(f"Sort Title: {doc.sortTitle}")
    print(f"Rerank Score: {doc.rerank_score}")
    print(f"Original Rank: {doc.original_rank}")
    print("---")