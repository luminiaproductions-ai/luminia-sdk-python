import os
from typing import Any, Dict, Optional

import requests

DEFAULT_BASE_URL = "https://api.luminiaproductions.com/v1"


def _gateway_origin(base_url: str) -> str:
    """Return scheme+host origin from a `/v1`-suffixed API base URL."""
    cleaned = base_url.rstrip("/")
    if cleaned.endswith("/v1"):
        return cleaned[:-3]
    return cleaned


class LuminiaClient:
    """Synchronous client for the Luminia Sovereign Intelligence Platform."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 60.0,
    ):
        self.api_key = api_key or os.getenv("LUMINIA_API_KEY")
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        headers: Dict[str, str] = {
            "Content-Type": "application/json",
            "User-Agent": "luminia-python-sdk/2.1.0",
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        self.session.headers.update(headers)

    def chat_completion(
        self,
        messages: list,
        model: str = "aethos-symbiosis-v2",
        temperature: float = 0.2,
        stream: bool = False,
        reasoning_effort: Optional[str] = None,
        max_tokens: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Send a completion request to the AETHOS Symbiosis v2.1 engine.

        Default model is "aethos-symbiosis-v2" (AETHOS Symbiosis v2.1 Golden).
        "aethos-symbiosis-swarm" runs the 4-Worker Parallel Swarm (3.04x speedup).
        "aethos-nova" and "aethos-apex" route backwards-compatibly to
        "aethos-symbiosis-v2".
        """
        url = f"{self.base_url}/chat/completions"
        payload: Dict[str, Any] = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "stream": stream,
        }
        if reasoning_effort is not None:
            payload["reasoning_effort"] = reasoning_effort
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens

        response = self.session.post(url, json=payload, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def list_models(self) -> Dict[str, Any]:
        """Fetch available sovereign models from ``GET /v1/models``."""
        url = f"{self.base_url}/models"
        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def symbiosis_status(self) -> Dict[str, Any]:
        """Fetch live enclave status from ``GET /api/symbiosis/status``."""
        url = f"{_gateway_origin(self.base_url)}/api/symbiosis/status"
        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()


class AsyncLuminiaClient:
    """Asynchronous configuration holder for Luminia Sovereign Platform."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = DEFAULT_BASE_URL,
    ):
        self.api_key = api_key or os.getenv("LUMINIA_API_KEY")
        self.base_url = base_url.rstrip("/")
