import os
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "config", '.env')
dotenv.load_dotenv(dotenv_path)

token = os.environ.get("token")


cog_files = [
        f"cogs.{os.path.splitext(fp)[0]}" for fp in os.listdir(f"{os.curdir}{os.sep}cogs{os.sep}") if fp.endswith(".py")
    ]