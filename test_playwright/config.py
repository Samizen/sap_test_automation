import os
from dotenv import load_dotenv

load_dotenv()

class User_details:
    user=os.getenv("USERNAME")
    password=os.getenv("PASSWORD")
    bni_url=os.getenv("BnI_URL")
    


