# Luminia Python SDK (`luminia-sdk`)

[![PyPI version](https://img.shields.io/badge/pypi-v1.0.0-blue.svg)](https://platform.luminiaproductions.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Official Python SDK for **[platform.luminiaproductions.com](https://platform.luminiaproductions.com)**.  
Built for sovereign, zero-false-refusal inference with hardware-enforced telemetry guarantees.

---

## ⚡ Installation
```bash
pip install luminia-sdk
```

---

## 🚀 Quick Usage

```python
from luminia import LuminiaClient

# Initialize client (uses LUMINIA_API_KEY environment variable or argument)
client = LuminiaClient(api_key="lum_live_...")

# Execute sovereign inference
response = client.chat_completion(
    model="aethos-sovereign-v1",
    messages=[
        {"role": "user", "content": "Analyze ARM Cortex-A baseband power isolation mechanics."}
    ],
    temperature=0.2
)

print(response["choices"][0]["message"]["content"])
```

---

## 🔐 Platform & API Access
* Generate API keys: [platform.luminiaproductions.com/keys](https://platform.luminiaproductions.com)
* Architecture & Whitepapers: [luminiaproductions.com](https://luminiaproductions.com)

---

## License
MIT License. Copyright © 2026 Luminia Sovereign Systems.
