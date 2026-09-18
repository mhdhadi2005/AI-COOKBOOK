from mem0 import MemoryClient
from dotenv import load_dotenv
import os

load_dotenv(".env")

api_key = os.getenv("MEM0_API_KEY")
if not api_key:
    raise ValueError("MEM0_API_KEY is missing. Add your key to the .env file in this folder.")

client = MemoryClient(api_key=api_key)
user_id = "me"


def direct_yes_no_answer(question, memory_texts):
    q = question.lower().strip().rstrip("?!.")

    if q in {"who am i", "what is my name", "what's my name"}:
        for memory in memory_texts:
            m = memory.lower()
            if "name is mohammed hadi" in m or "name is mohammed" in m:
                return "You are Mohammed Hadi."
        return "I don't know your name yet."

    if not ("do i" in q or "do you know if i" in q or "am i" in q or "did i" in q):
        return None

    for memory in memory_texts:
        m = memory.lower()
        if "love pizza" in m or "loves pizza" in m or "like pizza" in m:
            return "Yes — you love pizza."
        if "favorite color is blue" in m or "favourite color is blue" in m:
            return "Yes — your favorite color is blue."
        if "name is mohammed hadi" in m or "name is mohammed" in m:
            return "Yes — your name is Mohammed Hadi."
    return "I don't know for sure yet."


client = MemoryClient(api_key=api_key)
user_id = "me"

print("Mem0 chat started. Type 'exit' to quit.\n")
print("I remember facts about you and can recall them later.\n")

while True:
    user_msg = input("You: ").strip()
    if not user_msg:
        continue
    if user_msg.lower() in ["exit", "quit"]:
        print("Assistant: Goodbye!")
        break

    client.add(
        [{"role": "user", "content": user_msg}],
        user_id=user_id,
    )

    memories = client.search(user_msg, filters={"user_id": user_id})
    results = memories.get("results", [])
    memory_texts = [item.get("memory") for item in results if item.get("memory")]

    direct_answer = direct_yes_no_answer(user_msg, memory_texts)
    if direct_answer:
        response = direct_answer
    elif memory_texts:
        response = "I remember: " + "; ".join(memory_texts[:3])
    else:
        response = "I don't have a relevant memory yet, but I stored what you said."

    print(f"Assistant: {response}\n")
