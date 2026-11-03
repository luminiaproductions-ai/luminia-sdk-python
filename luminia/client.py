import os
import json
import requests
from typing import Optional, Dict, Any, Generator

DEFAULT_BASE_URL = "https://platform.luminiaproductions.com/api/v1"

class LuminiaClient:
    """Synchronous client for Luminia Sovereign Platform."""
    def __init__(self, api_key: Optional[str] = None, base_url: str = DEFAULT_BASE_URL):
        self.api_key = api_key or os.getenv("LUMINIA_API_KEY")
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}" if self.api_key else "",
            "Content-Type": "application/json",
            "User-Agent": "luminia-python-sdk/1.0.0",
        })

    def chat_completion(
        self,
        messages: list,
        model: str = "aethos-sovereign-v1",
        temperature: float = 0.2,
        stream: bool = False,
    ) -> Dict[str, Any]:
        """Send a completion request to the Sovereign AETHOS engine."""
        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "stream": stream,
        }
        
        response = self.session.post(url, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()

class AsyncLuminiaClient:
    """Asynchronous client stub for Luminia Sovereign Platform."""
    def __init__(self, api_key: Optional[str] = None, base_url: str = DEFAULT_BASE_URL):
        self.api_key = api_key or os.getenv("LUMINIA_API_KEY")
        self.base_url = base_url.rstrip("/")
