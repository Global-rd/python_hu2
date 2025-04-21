import os
from dotenv import load_dotenv
load_dotenv()

API_BASE_URL=os.environ.get("API_BASE_URL")
PATH_COINMARKETS=os.environ.get("PATH_COINMARKETS")
VS_CURRENCY=os.environ.get("VS_CURRENCY")
RESULTS_PER_PAGE=os.environ.get("RESULTS_PER_PAGE")
ORDER=os.environ.get("ORDER")
