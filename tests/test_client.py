from unittest.mock import MagicMock

import luminia
from luminia.client import DEFAULT_BASE_URL, AsyncLuminiaClient, LuminiaClient


def test_version_and_default_gateway():
    assert luminia.__version__ == "2.1.0"
    assert DEFAULT_BASE_URL == "https://api.luminiaproductions.com/v1"
    client = LuminiaClient(api_key="test-key")
    assert client.base_url == "https://api.luminiaproductions.com/v1"
    assert client.session.headers["Authorization"] == "Bearer test-key"
    async_client = AsyncLuminiaClient(api_key="test-key")
    assert async_client.base_url == "https://api.luminiaproductions.com/v1"


def test_unauthenticated_omits_blank_bearer_header(monkeypatch):
    monkeypatch.delenv("LUMINIA_API_KEY", raising=False)
    client = LuminiaClient()
    assert "Authorization" not in client.session.headers


def test_chat_completion_and_status_payloads():
    client = LuminiaClient(api_key="test-key")
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"choices": [{"message": {"content": "ok"}}]}
    mock_resp.raise_for_status.return_value = None
    client.session.post = MagicMock(return_value=mock_resp)
    client.session.get = MagicMock(return_value=mock_resp)

    out = client.chat_completion(
        messages=[{"role": "user", "content": "audit"}],
        reasoning_effort="high",
        max_tokens=256,
    )
    assert out["choices"][0]["message"]["content"] == "ok"
    client.session.post.assert_called_once()
    call_url = client.session.post.call_args.args[0]
    call_json = client.session.post.call_args.kwargs["json"]
    assert call_url == "https://api.luminiaproductions.com/v1/chat/completions"
    assert call_json["model"] == "aethos-symbiosis-v2"
    assert call_json["reasoning_effort"] == "high"
    assert call_json["max_tokens"] == 256

    client.list_models()
    assert client.session.get.call_args_list[0].args[0] == "https://api.luminiaproductions.com/v1/models"
    client.symbiosis_status()
    assert client.session.get.call_args_list[1].args[0] == "https://api.luminiaproductions.com/api/symbiosis/status"
