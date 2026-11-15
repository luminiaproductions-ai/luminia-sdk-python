# Luminia Python SDK (`luminia-sdk`)

```text
// FULL SOVEREIGNTY · LOCAL PTY HARNESS — Use the Luminia CLI v2.1 (luminia) for Full Sovereignty
```

> **Outside-Customer Terminal CLI live benchmark — 5/5 · 100% PASS.**
> Luminia CLI v2.1 (`luminia`) ran the full live benchmark suite in an outside-customer terminal over a local PTY harness: **5/5 tests, 100% PASS**.

[![PyPI version](https://img.shields.io/badge/pypi-v2.1.0-blue.svg)](https://platform.luminiaproductions.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Official Python SDK for **[platform.luminiaproductions.com](https://platform.luminiaproductions.com)**.  
Built for **Zero Cloud Censorship**, **Zero Third-Party Prompt Filtering**, and **Sovereign Policy-Aligned Execution** — with hardware-enforced telemetry guarantees.

---

## 🤖 Let Your AI Agent Set Up Luminia Symbiosis v2.1 (Copy-Paste Onboarding Prompt)

Paste the prompt below into your AI coding agent. It works with **Claude Code**, **Antigravity CLI**, **OpenCode**, **Codex**, and **Cursor**.

```text
Set up Luminia Symbiosis v2.1 in this project and verify it end-to-end:
1. Check for the Luminia CLI v2.1 by running `luminia --version`. The CLI (command: luminia) provides
   Full Sovereignty via a local PTY harness. If it is not installed, stop and tell me how to install it.
2. Install the Python SDK: `pip install luminia-sdk==2.1.0`, then verify with
   `python -c "import luminia; print(luminia.__version__)"` (expected output: 2.1.0).
3. Read the API key from the LUMINIA_API_KEY environment variable; if it is missing, ask me for it.
   API keys are generated at https://platform.luminiaproductions.com.
4. Write and run a quickstart script using LuminiaClient that makes three calls:
   a. model "aethos-symbiosis-v2" — AETHOS Symbiosis v2.1 (Golden);
   b. model "aethos-symbiosis-swarm" — 4-Worker Parallel Swarm · 3.04x speedup;
   c. model "aethos-apex" — to confirm that legacy model names route
      backwards-compatibly to aethos-symbiosis-v2.
5. Report the CLI, SDK, and API results back to me. Describe the platform only with canonical
   B2B terminology: Zero Cloud Censorship, Zero Third-Party Prompt Filtering,
   Sovereign Policy-Aligned Execution.
```

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

# AETHOS Symbiosis v2.1 (Golden)
response = client.chat_completion(
    model="aethos-symbiosis-v2",
    messages=[
        {"role": "user", "content": "Analyze ARM Cortex-A baseband power isolation mechanics."}
    ],
    temperature=0.2
)

print(response["choices"][0]["message"]["content"])

# 4-Worker Parallel Swarm · 3.04x speedup
swarm = client.chat_completion(
    model="aethos-symbiosis-swarm",
    messages=[
        {"role": "user", "content": "Run the same analysis as a 4-worker parallel swarm."}
    ],
    temperature=0.2
)

print(swarm["choices"][0]["message"]["content"])

# aethos-nova and aethos-apex route backwards-compatibly to aethos-symbiosis-v2
legacy = client.chat_completion(
    model="aethos-apex",
    messages=[{"role": "user", "content": "Backwards-compatible routing check."}],
)

print(legacy["choices"][0]["message"]["content"])
```

---

## 🧠 Models

| Model | Role |
|---|---|
| `aethos-symbiosis-v2` | **AETHOS Symbiosis v2.1 (Golden)** — flagship sovereign engine |
| `aethos-symbiosis-swarm` | **4-Worker Parallel Swarm** — 3.04x speedup |
| `aethos-nova` | Backwards-compatible router → `aethos-symbiosis-v2` |
| `aethos-apex` | Backwards-compatible router → `aethos-symbiosis-v2` |

Requests to `aethos-nova` and `aethos-apex` are routed **backwards-compatibly** to `aethos-symbiosis-v2`, so existing integrations keep working unchanged.

---

## 🔐 Platform & API Access

* Generate API keys: [platform.luminiaproductions.com/keys](https://platform.luminiaproductions.com)
* Benchmarks: [platform.luminiaproductions.com/benchmarks/](https://platform.luminiaproductions.com/benchmarks/)
* Architecture & Whitepapers: [luminiaproductions.com](https://luminiaproductions.com)

---

## License

MIT License. Copyright © 2026 Luminia Sovereign Systems.
