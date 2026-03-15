ARC — Autonomous Reasoning Core (v2)
_____________________________________

ARC is a local-first, voice-operated OS assistant built for fast execution, low latency, and precision.
It combines offline speech recognition, a locally hosted LLM, and real-time speech synthesis into a continuous voice interaction loop.

ARC is not designed as a chatbot.
It behaves more like an operating-system interface: concise, intentional, and optimized for action.


Core Principles
________________

Local-first (no cloud dependency)

Voice-native by design

Action over conversation

Deterministic, measurable behavior

Latency-aware system design

Experiment-driven architecture

What’s New in v2 (Context Awareness)

Version 2 introduces context awareness as an engineering problem, not a prompt trick.


Key additions:
_______________

Sliding-window working memory

Explicit session memory logging

Token and latency instrumentation

Empirical analysis of long-context behavior

Measured trade-offs between context size and latency

ARC v2 intentionally exposes its internal metrics to understand how conversational context affects performance.


High-Level Architecture
________________________

Microphone
 → Audio Capture (PyAudio)
 → Speech Detection (RMS + Silence)
 → Speech Recognition (Vosk)
 → Context Assembly
 → Local LLM (Ollama / LLaMA 3.1)
 → Speech Synthesis (pyttsx3)
 → Debug Metrics (tokens, latency, context size)


Context & Memory Model (v2)
___________________________

ARC v2 separates conversation flow from memory.


 → Working Context

Sliding window of recent turns

Used to maintain short-term coherence

Size is configurable (experimentally tested up to ~70 turns)


 → Session Memory

Condensed log of completed windows

Intended for debugging, recall, and future memory strategies

Not automatically injected into every response


 → Key Insight

Long, unbounded context windows significantly increase latency due to prompt re-evaluation.
ARC v2 treats context size as a measurable performance constraint, not a convenience.


 → Experimental Findings

From sustained conversation tests:

Prompt tokens grow linearly with context window size

Latency correlates strongly with prompt tokens, not response length

Voice UX degrades sharply beyond ~1500–2000 prompt tokens

Large sliding windows create diminishing returns in response quality

These findings directly inform ARC’s move toward summarization-based memory in future versions.


 → Assistant Personality

ARC blends characteristics inspired by:

J.A.R.V.I.S. — precision and efficiency

F.R.I.D.A.Y. — calm, supportive tone

TARS — subtle, dry wit


 → Behavioral traits:

Concise, calm, technical

Minimal verbosity

Emotionally aware, without simulation

Optimized for speech output

Designed to avoid rambling or over-explaining


 → Configuration

Audio
SAMPLE_RATE = 16000
RMS_THRESHOLD = 180
SILENCE_TIMEOUT = 1.8


 → Speech Recognition

Vosk (offline)

Tested with vosk-model-small-en-in-0.4


 → Language Model

LLaMA 3.1 via Ollama

Local inference only


 → Speech Output

pyttsx3 (Windows SAPI)

Adjustable speaking rate


 → Debug & Instrumentation

ARC exposes internal metrics per turn:

Prompt tokens

Response tokens

Total tokens

Latency (seconds)

Context window size

Session memory size

These metrics are logged live and exported for analysis (CSV / Excel).


Installation Requirements & Setup
__________________________________

Python 3.9+

Windows

Microphone

Ollama installed and running

Install Dependencies
pip install pyaudio vosk pyttsx3 ollama colorama

Download Vosk Model

https://alphacephei.com/vosk/models

Place the model path in the configuration section.

Running ARC
python ARC_context_awareness.py


On startup:

ASCII banner is displayed

ARC enters continuous listening mode

Audio cues indicate state changes


Known Limitations (v2)

No persistent memory across sessions

No intent routing or system command execution

Context is re-evaluated per LLM call (no KV-cache reuse)

Long contexts increase latency significantly

Context summarization is experimental



===================
Roadmap
v3 (Planned)
===================


Summarized context injection

Ephemeral memory layer

Intent detection

Explicit memory recall commands

Reduced prompt re-evaluation cost

===================
Future - possibly
===================

Persistent memory

Streaming responses

System-level command execution

Modular plugin architecture


Philosophy
___________

ARC is an experiment in building assistants as systems, not personalities.

Latency, determinism, and clarity matter more than sounding human.
Every design decision is informed by measurement, not assumption.

ARC is not a chatbot.
It is an operating-system interface.