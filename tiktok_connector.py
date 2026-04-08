"""
TikTok Live Comment Connector
Connects to a TikTok Live stream and forwards comments to the chatbot via HTTP.

Usage:
    python tiktok_connector.py

Make sure the Flask app (app.py) is running first.
"""

import asyncio
import aiohttp
from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent, ConnectEvent, DisconnectEvent

# TikTok username to connect to (without @)
TIKTOK_USERNAME = "garudafood_officialstore"

# Chatbot endpoint
CHATBOT_URL = "http://127.0.0.1:5000/live_comment"

client = TikTokLiveClient(unique_id=TIKTOK_USERNAME)


@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    print(f"Connected to @{TIKTOK_USERNAME} live!")


@client.on(DisconnectEvent)
async def on_disconnect(event: DisconnectEvent):
    print("Disconnected from live.")


@client.on(CommentEvent)
async def on_comment(event: CommentEvent):
    username = event.user.nickname or event.user.unique_id
    comment = event.comment.strip()

    if not comment:
        return

    print(f"[{username}]: {comment}")

    # Forward to chatbot
    try:
        async with aiohttp.ClientSession() as session:
            await session.post(CHATBOT_URL, json={
                "username": username,
                "text": comment,
            })
    except Exception as e:
        print(f"Failed to forward comment: {e}")


if __name__ == "__main__":
    print(f"Connecting to @{TIKTOK_USERNAME} live...")
    client.run()
