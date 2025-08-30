# Initialize the card scanner tool
def init_card_scanner():
    """
    Initializes the card scanner tool and performs additional setup.
    """
    init_card_scanner_tool(
        name="kitenga",
        version="0.1.0",
        description="Whakatauki in motion all the way to the mana filled ocean",
        authors=["Adrian <hemithsphere@gmail.com>"],
        license="MIT",  
        readme="README.md",
        packages=[{"include": "scripts"}]
    )
    print("Card scanner initialized successfully.")
    # Call the Kitenga awakens function to set up the environment
    kitenga_awakens()
# This module initializes the Kitenga API by loading environment variables
# and setting up the card scanner tool. It defines the Kitenga environment
# with its name, version, description, authors, license, readme, and packages.
# The function also checks for required environment variables and prints
# relevant information about the Kitenga environment.
if __name__ == "__main__":
    init_card_scanner()
    print("Kitenga environment initialized successfully.")
    print("🌬️ Kitenga awakens… the awa flows, and the kaitiaki watch.")
    print("The journey begins with the first step into the unknown.")
    print("May the winds guide you, and the waters cleanse your path.")
    print("Kitenga API is ready to serve!")
    print("Card scanner initialized successfully.")
    print("Kitenga environment initialized successfully.")
    # This module initializes the Kitenga API by loading environment variables
    # and setting up the card scanner tool. It defines the Kitenga environment
    # with its name, version, description, authors, license, readme, and packages
    # The function also checks for required environment variables and prints
    # relevant information about the Kitenga environment.

from kitenga_backend.kitenga_api.kitenga_awakens import kitenga_awakens
from kitenga_backend.scripts.init_card_scan import init_card_scanner as init_card_scanner_tool
import os
import pprint   
from dotenv import load_dotenv, find_dotenv
import sys

# Load environment variables from .env file
if not load_dotenv(find_dotenv()):
    print("Error: .env file not found. Please ensure it exists and is properly configured.")
    sys.exit(1)

# Check for required environment variables and raise an error if missing
REQUIRED_ENV_VARS = [
    "SUPABASE_DB_NAME",
    "SUPABASE_DB_HOST",
    "SUPABASE_DB_PORT",
    "SUPABASE_URL",
    "SUPABASE_SERVICE_ROLE_KEY",
    "SUPABASE_ANON_KEY",
    "CARD_SCANNER_API_KEY"
]

missing_vars = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
if missing_vars:
    print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
    sys.exit(1)

# Move hardcoded values to environment variables
MODEL = os.getenv("CARD_SCANNER_MODEL", "latest")
MAX_RESULTS = int(os.getenv("CARD_SCANNER_MAX_RESULTS", 5))

def kitenga_awakens():
    name = "kitenga"
    version = "0.1.0"
    description = "Whakatauki in motion all the way to the mana filled ocean"
    authors = ["Adrian <hemithsphere@gmail.com>"]
    license = "MIT"
    readme = "README.md"
    packages = [{"include": "scripts"}]
    api_key = os.getenv("CARD_SCANNER_API_KEY")

    print(f"Initializing {name} version {version}")
    print(f"Description: {description}")
    print(f"Authors: {', '.join(authors)}")
    print(f"License: {license}")
    print(f"Readme: {readme}")
    print(f"Packages: {pprint.pformat(packages)}")
    print(f"API Key: {api_key}")
    print(f"Model: {MODEL}")
    print(f"Max Results: {MAX_RESULTS}")
    pprint.pprint(os.environ)

# Remove redundant code and ensure proper initialization
if __name__ == "__main__":
    try:
        kitenga_awakens()
        print("Kitenga environment initialized successfully.")
        print("🌬️ Kitenga awakens… the awa flows, and the kaitiaki watch.")
        print("The journey begins with the first step into the unknown.")
        print("May the winds guide you, and the waters cleanse your path.")
        print("Kitenga API is ready to serve!")
    except Exception as e:
        print(f"Error during initialization: {e}")
        sys.exit(1)


