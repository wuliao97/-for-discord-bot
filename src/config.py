import os
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "config", '.env')
dotenv.load_dotenv(dotenv_path)

TOKEN = os.environ.get("token")
API_TOKEN = os.environ.get("apitoken")


BASE = "https://spla3.yuu26.com/api/"
