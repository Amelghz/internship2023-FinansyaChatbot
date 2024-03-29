# question_answering.py
# Import necessary modules from the langchain library
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import GPT4All, LlamaCpp

# Import constants from the constants module
from constants import CHROMA_SETTINGS
import os
# Retrieve environment variables
embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
persist_directory = os.environ.get('PERSIST_DIRECTORY')

model_type = os.environ.get('MODEL_TYPE')
model_path = os.environ.get('MODEL_PATH')
model_n_ctx = os.environ.get('MODEL_N_CTX')
model_n_batch = int(os.environ.get('MODEL_N_BATCH', 8))
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS', 4))

# Define a function to get the question-answering model instance
def get_qa_model():
    # Initialize HuggingFaceEmbeddings
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    # Initialize Chroma vector store for retrieval
    db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)
    retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
    # Initialize the LLM based on model_type
    if model_type == "LlamaCpp":
        llm = LlamaCpp(model_path=model_path, n_ctx=model_n_ctx, n_batch=model_n_batch, verbose=False)
    elif model_type == "GPT4All":
        llm = GPT4All(model=model_path, n_ctx=model_n_ctx, backend='gptj', n_batch=model_n_batch, verbose=False)
    else:
        raise Exception(f"Model type {model_type} is not supported. Please choose one of the following: LlamaCpp, GPT4All")
    # Initialize RetrievalQA based on the LLM and retriever   
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
    return qa

# Define the main question-answering function
def your_question_answering_function(question, documents):
     # Get the question-answering model instance using the get_qa_model function
    qa = get_qa_model()

    # Convert the documents list to a list of Document objects
    document_objects = [qa.retriever._doc_from_dict(doc) for doc in documents]

    # Call the question-answering model using the __call__ method
    result = qa(question, document_objects)

    # Return the answer from the result
    return result['result']
