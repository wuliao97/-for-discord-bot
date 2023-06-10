import os



cog_files = [
    f"cogs.{os.path.splitext(fp)[0]}" for fp in os.listdir(f"{os.curdir}{os.sep}cogs{os.sep}") if fp.endswith(".py")
]

