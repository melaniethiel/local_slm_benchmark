# Version History
This file documents the progression of the project so the GitHub repository shows a clear learning timeline.

## Portfolio note
The goal is not just to run models, but to show steady growth in practical software engineering, local AI, and performance benchmarking over time.

## v0.1 - Project setup, Ollama configuration, and model selection

### Added
- Python project created to benchmark local open-source AI models
- selected models across five categories to test:
  - fast small model (`llama3.2:3b`)
  - popular general-purpose models (`llama3.1:8b`, `mistral:7b`, `gemma2:9b`)
  - step-by-step reasoning model (`deepseek-r1:8b`)
  - coding model (`qwen2.5-coder:7b`)
  - vision models (`moondream`, `llava:7b`)
- `.gitignore` file to ignore virtual environments and test logs
- `README.md` with project goals, hardware details, and model comparison table
- `VERSION_HISTORY.md` tracking file for portfolio progress

### Purpose
- set up a working local AI testing environment
- learn how to run open-source models offline using Ollama
- organize models by practical use cases before writing benchmark code
- document hardware choices and memory constraints clearly

### Notes
- this is the baseline version of the project
- models run locally using 4-bit quantization to fit within 8 GB GPU memory
- everything runs offline with zero API costs

---

## v0.2 - Automated benchmark script, speed tracking, and file saving

### Added
- `benchmark.py` automated script using the official `ollama` Python library
- latency and performance tracking: VRAM load time, total duration, tokens generated, and generation speed (tokens/sec)
- automatic markdown export (`benchmark_run_latest.md`) to prevent terminal scrollback truncation
- `initial tests.txt` capturing full outputs and benchmark metrics across 3 initial test runs
- documented empirical hardware findings in `README.md` (cold start latency, 3B vs 8B throughput, DeepSeek reasoning token counts, and 9B VRAM boundaries)

### Purpose
- move from manual CLI testing to reproducible programmatic evaluation
- measure physical hardware constraints and generation speeds accurately
- preserve all model responses without relying solely on terminal buffers

### Notes
- `llama3.2:3b` achieved ~69 tokens/sec, nearly double the ~37 tokens/sec rate of 7B–8B models
- `deepseek-r1:8b` demonstrated significant token expansion (1,379 tokens) due to step-by-step `<think>` reasoning
- `gemma2:9b` experienced reduced speed (~18 tokens/sec) due to memory pressure on an 8 GB graphics card

---

## Planned future versions

### v0.3 - Multi-category test prompts and vision testing
- test models on a standard set of prompts for coding, reasoning, and general questions
- test `moondream` and `llava:7b` using sample images
- compare answer quality side-by-side with speed numbers

### v0.4 - Save results to files and create summary reports
- save benchmark runs to CSV or JSON files
- generate simple markdown reports showing comparison results
- add basic charts comparing model speeds

### v1.0 - Complete benchmark tool
- clean command-line options to choose models, prompt categories, and test runs
- track GPU memory usage during testing
- publish full findings and hardware notes to GitHub
