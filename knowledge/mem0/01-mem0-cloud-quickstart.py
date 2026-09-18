from mem0 import MemoryClient
from dotenv import load_dotenv
import os

load_dotenv(".env")

# --------------------------------------------------------------
# Initialize Mem0 client (Cloud)
# --------------------------------------------------------------

client = MemoryClient(api_key=os.getenv("m0-MuCZbS4ixotUgvMndROAV0GKkIZI2oegIogutlhJ"))

# --------------------------------------------------------------
# Message sequence
# --------------------------------------------------------------

messages = [
    {
        "role": "user",
        "content": "Hi, I'm Hadi. I love my mom!.",
    },
    {
        "role": "assistant",
        "content": "Hello Hadi! I've noted that you love your mom. I'll keep this in mind for any discussions or recommendations related to family or personal relationships.",
    },
]

client.add(messages, user_id="default_user")

# --------------------------------------------------------------
# Search for related memories
# --------------------------------------------------------------

query = "What shall we build today?"

# --------------------------------------------------------------
# Search for related memories
# --------------------------------------------------------------

response = client.search(query, filters={"user_id": "default_user"})
print(response)
