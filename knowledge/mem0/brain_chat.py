from mem0 import MemoryClient
from dotenv import load_dotenv
import os

load_dotenv(".env")

client = MemoryClient(api_key=os.getenv("MEM0_API_KEY"))
user_id = "me"

# Base memory profile
profile_facts = [
    "My name is Mohammed Hadi.",
    "I am Indian and have strong connections to the UAE and Dubai.",
    "I am a 3rd-year B.Tech Data Science & Engineering student at MIT Manipal.",
    "I am in the 2027 graduating batch.",
    "I like direct, casual, practical answers.",
    "I am interested in AI, Data Science, business, finance, and entrepreneurship.",
    "I am interested in crypto, blockchain, Web3, and trading.",
    "I use ChatGPT as a technical assistant, tutor, and business brainstorming partner.",
    "I like travel, road trips, and scenic destinations in India.",
    "I am actively applying for internships and career opportunities.",
]

# Load profile once if not already present
for fact in profile_facts:
    client.add([{"role": "user", "content": fact}], user_id=user_id)

print("Mem0 brain started. Type 'exit' to quit.\n")

while True:
    user_msg = input("You: ").strip()
    if not user_msg:
        continue
    if user_msg.lower() in ["exit", "quit"]:
        print("Brain: Goodbye!")
        break

    client.add([{"role": "user", "content": user_msg}], user_id=user_id)

    memories = client.search(user_msg, filters={"user_id": user_id})
    results = memories.get("results", [])
    memory_texts = [item.get("memory") for item in results if item.get("memory")]

    if memory_texts:
        print("Brain remembers:")
        for m in memory_texts[:5]:
            print("-", m)
    else:
        print("Brain: I don't have a matching memory yet, but I stored it.")

    print()
