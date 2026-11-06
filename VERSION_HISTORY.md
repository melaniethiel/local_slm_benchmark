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

## Planned future versions

### v0.2 - Basic benchmark script and speed tracking
- write a Python script using the `ollama` library to test models
- measure response time, total tokens, and tokens per second
- print clean comparison tables in the terminal

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
