"""
app.py — a simple web chat UI for the Socratic tutor, built with Chainlit.

This reuses the Socratic agent already running in Microsoft Foundry. Chainlit
turns the functions below into a polished chat website.

Run:
    pip install chainlit "azure-ai-projects>=2.1.0" azure-identity
    az login
    chainlit run app.py -w
Then open the URL it prints (usually http://localhost:8000).
"""

import asyncio

import chainlit as cl
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# My Foundry project + deployed agent (same values as call_agent.py).
ENDPOINT = "https://socratic-tutor-resource.services.ai.azure.com/api/projects/socratic-tutor"
AGENT_NAME = "Socratic"
AGENT_VERSION = "3"

# Connect to Foundry once, when the app starts.
project_client = AIProjectClient(endpoint=ENDPOINT, credential=DefaultAzureCredential())
client = project_client.get_openai_client()


def ask_agent(conversation):
    """Blocking call to the Foundry agent. Runs in a worker thread so the
    web page stays responsive (and can show a loading indicator)."""
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
    return response.output_text


@cl.on_chat_start
async def start():
    # Each new visitor gets a fresh, empty conversation.
    cl.user_session.set("conversation", [])
    await cl.Message(
        content=(
            "Hi! I'm **Socratic**, your algebra tutor. Show me a problem or a "
            "solution you're unsure about, and I'll help you work out where it "
            "went wrong — I won't just hand you the answer. 😊"
        )
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    conversation = cl.user_session.get("conversation")
    conversation.append({"role": "user", "content": message.content})

    # Show an instant placeholder so the student knows it's working.
    thinking = cl.Message(content="Looking at your steps… 🤔")
    await thinking.send()

    try:
        # Run the blocking call off the main loop so the UI stays live.
        reply = await asyncio.to_thread(ask_agent, conversation)
    except Exception as error:
        reply = f"Sorry, I had trouble reaching the tutor: {error}"

    conversation.append({"role": "assistant", "content": reply})
    cl.user_session.set("conversation", conversation)

    # Replace the placeholder with the real answer.
    thinking.content = reply
    await thinking.update()
