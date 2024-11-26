from together import Together

client = Together(api_key="e67312ea13b803e4e1e4c557a78af68af3394f1ef8c856dfd940ffbf04be6bff")

def stream_chat_response(content: str):
    stream = client.chat.completions.create(
        model="meta-llama/Llama-3-8b-chat-hf",
        messages=[{"role": "user", "content": content}],
        stream=True,
    )

    # Streaming the response and printing as it arrives
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="", flush=True)

# Call the wrapper function this is an example
stream_chat_response("tell me about new york")