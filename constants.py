# Import the "os" module to access operating system functionalities
import os

# Import the "load_dotenv" function from the "dotenv" module to load environment variables from a file
from dotenv import load_dotenv

# Import the "Settings" class from the "chromadb.config" module to configure Chroma settings
from chromadb.config import Settings

# Load environment variables from a .env file in the current directory
load_dotenv()

# Define the folder path for storing the database (retrieved from the "PERSIST_DIRECTORY" environment variable)
PERSIST_DIRECTORY = os.environ.get('PERSIST_DIRECTORY')

# Define the Chroma settings using the "Settings" class with specific configurations
CHROMA_SETTINGS = Settings(
        chroma_db_impl='duckdb+parquet',  # Set the Chroma database implementation to DuckDB with Parquet storage
        persist_directory=PERSIST_DIRECTORY,  # Set the directory for persisting the Chroma database
        anonymized_telemetry=False  # Set anonymized telemetry to False
)
