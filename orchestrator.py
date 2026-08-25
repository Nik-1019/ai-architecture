from model_provider import generate

# System context prepended to every user prompt
SYSTEM_CONTEXT = "You are a helpful assistant. Respond concisely."

# System context for summarization requests
SUMMARIZE_CONTEXT = "You are a summarization assistant. Summarize the text below in 2-3 sentences."

# Format the user question with system context and call the model
def handle_question(user_question: str) -> str:
    prompt = f"{SYSTEM_CONTEXT}\n\nUser question: {user_question}"
    return generate(prompt)

# Format the text to summarize with its system context and call the model
def handle_summarize(text: str) -> str:
    prompt = f"{SUMMARIZE_CONTEXT}\n\nText: {text}"
    return generate(prompt)