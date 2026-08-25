from model_provider import generate

# System context prepended to every user prompt
SYSTEM_CONTEXT = "You are a helpful assistant. Respond concisely."


# Format the user question with system context and call the model
def handle_question(user_question: str) -> str:
    prompt = f"{SYSTEM_CONTEXT}\n\nUser question: {user_question}"
    return generate(prompt)