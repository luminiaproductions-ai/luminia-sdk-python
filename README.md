# Luminia Python SDK & Sovereign Terminal CLI (`luminia-sdk` v2.1)

```text
// FULL SOVEREIGNTY · LOCAL PTY HARNESS — Includes Luminia CLI v2.1 (`luminia`) & Python SDK (`LuminiaClient`)
```

> **Outside-Customer Terminal CLI live benchmark — 5/5 · 100% PASS.**
> Luminia CLI v2.1 (`luminia`) ran the full live benchmark suite in an outside-customer terminal over a local PTY harness: **5/5 tests, 100% PASS**.

[![Version](https://img.shields.io/badge/version-v2.1.0-blue.svg)](https://platform.luminiaproductions.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Official Python SDK & Sovereign Terminal CLI (`luminia`) for **[platform.luminiaproductions.com](https://platform.luminiaproductions.com)** (OpenAI-compatible Sovereign API Gateway: **`https://api.luminiaproductions.com/v1`**).  
Built for **Zero Cloud Censorship**, **Zero Third-Party Prompt Filtering**, and **Sovereign Policy-Aligned Execution** — with deterministic compiler & ASAN verification guarantees.

---

## ⚡ 1-Command Installation (SDK + `luminia` Terminal CLI)

```bash
pip install git+https://github.com/luminiaproductions-ai/luminia-sdk-python.git
```

Verify immediately in your terminal (works out of the box in Sovereign Preview mode, or with `LUMINIA_API_KEY`):

```bash
luminia --version
luminia status
luminia "Verify stack canary protection in C11 with GCC"
luminia --swarm "Audit TLS 1.3 cipher suite downgrade surface"
```

---

## 🤖 Let Your AI Agent Set Up Luminia Symbiosis v2.1 (Copy-Paste Onboarding Prompt)

Paste the prompt below into your AI coding agent (**Claude Code**, **Antigravity CLI**, **OpenCode**, **Codex**, or **Cursor**):

```text
Set up Luminia Symbiosis v2.1 in this project and verify it end-to-end:
1. Install the official Luminia SDK & Terminal CLI v2.1 directly from GitHub:
   `pip install git+https://github.com/luminiaproductions-ai/luminia-sdk-python.git`
2. Verify the CLI and SDK installation:
   `luminia --version`
   `python3 -c "import luminia; print(luminia.__version__)"` (expected output: 2.1.0)
3. Configure Gateway Base URL `https://api.luminiaproductions.com/v1` (reads `LUMINIA_API_KEY` if set, or uses Sovereign Preview mode automatically).
4. Run a verification check using `LuminiaClient`:
   a. `client.list_models()` and `client.symbiosis_status()`;
   b. model `"aethos-symbiosis-v2"` with `reasoning_effort="high"` — AETHOS Symbiosis v2.1 (Golden);
   c. model `"aethos-symbiosis-v2"` with `swarm=True` — Built-in 4-Worker Parallel `/swarm` Mode (3.04x speedup).
5. Report the CLI, SDK, and API results back to me using canonical B2B terminology:
   Zero Cloud Censorship, Zero Third-Party Prompt Filtering, Sovereign Policy-Aligned Execution.
```

---

## 🚀 Quick Python SDK Usage

```python
from luminia import LuminiaClient

# Initialize client (uses LUMINIA_API_KEY if set, or Sovereign Preview mode out of the box)
client = LuminiaClient()

# Discover model catalog and live enclave telemetry
print(client.list_models())
print(client.symbiosis_status())

# AETHOS Symbiosis v2.1 (Golden) — Single Flagship Sovereign Model
response = client.chat_completion(
    model="aethos-symbiosis-v2",
    reasoning_effort="high",
    messages=[
        {"role": "user", "content": "Analyze ARM Cortex-A baseband power isolation mechanics."}
    ],
    temperature=0.2,
)
print(response["choices"][0]["message"]["content"])

# Built-in 4-Worker Parallel /swarm Mode on the same aethos-symbiosis-v2 model (3.04x speedup)
swarm = client.chat_completion(
    model="aethos-symbiosis-v2",
    swarm=True,
    messages=[
        {"role": "user", "content": "Run a 4-worker parallel security audit on this module."}
    ],
    temperature=0.2,
)
print(swarm["choices"][0]["message"]["content"])
```

---

## 🧠 Flagship Model Architecture

| Model ID | Description |
|---|---|
| `aethos-symbiosis-v2` | **AETHOS Symbiosis v2.1 (Golden)** — Flagship Sovereign Security, Systems Engineering & Compiler-Verified Code Synthesis Engine (includes built-in 4-Worker Parallel `/swarm` Execution Mode) |
| `daisanome-v1` | **DaisaNOme** — RF / Wi-Fi / Acoustic spatial intelligence (Closed Enclave Preview) |

> Legacy model identifiers (`aethos-nova`, `aethos-apex`) route backwards-compatibly to `aethos-symbiosis-v2`.

---

## 🔐 Platform, Verification Harness & API Access

* Live Console & API Keys: [platform.luminiaproductions.com](https://platform.luminiaproductions.com)
* OpenAI-compatible API Gateway: `https://api.luminiaproductions.com/v1`
* Open-Source Deterministic Execution Harness: [github.com/luminiaproductions-ai/aethos-eval-harness](https://github.com/luminiaproductions-ai/aethos-eval-harness)
* Benchmarks: [luminiaproductions.com/benchmarks/](https://luminiaproductions.com/benchmarks/)
* Architecture & Whitepapers: [luminiaproductions.com](https://luminiaproductions.com)

---

## License

MIT License. Copyright © 2026 Luminia Sovereign Systems.
