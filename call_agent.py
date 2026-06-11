"""
call_agent.py — an interactive command-line client for the Socratic algebra tutor.

Connects to the Socratic agent running in Microsoft Foundry and lets you chat
with it from the terminal. Type a math problem or a wrong solution, and the
tutor responds Socratically. It remembers the conversation, so the back-and-forth
works like a real tutoring session. Type 'quit' to exit.

Setup:
    pip install "azure-ai-projects>=2.1.0" azure-identity
    az login
"""

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# My Foundry project endpoint (from Foundry > project > Overview).
ENDPOINT = "https://socratic-tutor-resource.services.ai.azure.com/api/projects/socratic-tutor"

# The deployed agent I want to talk to.
AGENT_NAME = "Socratic"
AGENT_VERSION = "3"


def main() -> None:
    # Authenticate using my `az login` session — no API keys stored in code.
    project_client = AIProjectClient(
        endpoint=ENDPOINT,
        credential=DefaultAzureCredential(),
    )

    # Foundry serves the agent through an OpenAI-compatible client.
    client = project_client.get_openai_client()

    # Keep the running conversation so the tutor remembers earlier turns.
    conversation = []

    print("Socratic tutor. Type a problem or a wrong solution. Type 'quit' to exit.\n")

    while True:
        student = input("You: ").strip()
        if student.lower() in {"quit", "exit"}:
            print("Goodbye — keep practicing!")
            break
        if not student:
            continue

        conversation.append({"role": "user", "content": student})

        try:
            response = client.responses.create(
                input=conversation,
                extra_body={
                    "agent_reference": {
                        "name": AGENT_NAME,
                        "version": AGENT_VERSION,
                        "type": "agent_reference",
                    }
                },
            )
            reply = response.output_text
            conversation.append({"role": "assistant", "content": reply})
            print(f"\nSocratic: {reply}\n")
        except Exception as error:
            print(f"\n[Something went wrong talking to the agent: {error}]\n")


if __name__ == "__main__":
    main()
