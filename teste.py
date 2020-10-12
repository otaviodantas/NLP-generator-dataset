import os
from dotenv import load_dotenv

# os.path.expanduser()
load_dotenv('config.env')

print(os.environ.get("WORDKEY"))
