# Local SLM Benchmark

A Python project to test and compare open-weights language and vision models running locally on my own computer.

This project started as a way to learn how local AI models work offline, how they fit into graphics card memory (VRAM), and how to measure real-world speed and output quality without paying for cloud APIs.

## Project goal

Build a simple, automated benchmarking tool that can:
- run open-source models offline using Ollama
- test different types of models against the same prompts
- measure response time, tokens per second, and memory fit
- compare smaller models against larger ones to see speed vs. quality trade-offs
- run everything privately with zero API costs

## Hardware and test environment

Running models locally depends heavily on hardware limits:

- **Hardware**: Windows desktop with 8 GB VRAM and 16 GB RAM, which can comfortably support 7B–9B models
- **Test Baseline**: Added a smaller 3B model to see speed and latency differences
- **Model Quantization**: 4-bit (`Q4_K_M`), which compresses model weights so 7B–9B models (~4 GB to 5.5 GB) fit entirely into 8 GB of GPU memory alongside working memory

## Why I chose these models

To see how different model sizes and specialties perform on the same computer, I chose models across five practical categories:

| Model Name | Creator | Best For |
| :--- | :--- | :--- |
| `llama3.2:3b` | Meta | Ultra-Fast Lightweight Responses |
| `llama3.1:8b` | Meta | Best All-Around & Tool Use |
| `qwen2.5-coder:7b` | Alibaba | Best for Code & JSON |
| `deepseek-r1:8b` | DeepSeek | Best for Step-by-Step Logic |
| `gemma2:9b` | Google DeepMind | Best Prose & Creative Writing |
| `mistral:7b` | Mistral AI | Fast & Direct Summaries |
| `moondream` | Vikhyat | Fast & Compact Image Processing |
| `llava:7b` | LLaVA Team | Detailed Image Understanding & Visual Q&A |

### Model Categories
- **Fast small model**: `llama3.2:3b` — lightweight baseline to see speed differences
- **Flagship general-purpose models**: `llama3.1:8b`, `mistral:7b`, `gemma2:9b` — direct comparison of leading 7B–9B models
- **Reasoning models**: `deepseek-r1:8b` — step-by-step reasoning using `<think>` tags
- **Coding specialists**: `qwen2.5-coder:7b` — programming syntax, debugging, and structured data
- **Vision models**: `moondream`, `llava:7b` — image understanding and visual question answering

## Skills demonstrated

This project highlights core skills in:
- Python scripting and local API integration using the `ollama` library
- running open-source AI models offline on local hardware
- managing GPU memory limits and understanding 4-bit model quantization
- measuring benchmark numbers like response latency and tokens per second
- command-line workflows with PowerShell and Git
- writing clear documentation and tracking project versions

## Current status

This version establishes the foundation:
- Ollama installed and running on Windows
- selected test models downloaded and verified
- Python virtual environment and project structure set up
- initial documentation and version history created

## Tech stack

- Python
- Ollama
- Ollama Python library

## Development tools

- VS Code
- Google Antigravity
- Git and GitHub
- Windows PowerShell

## Project structure

- `benchmark.py` — Python script to send prompts, track timing, and display results
- `requirements.txt` — Python dependencies for the project
- `README.md` — project overview, hardware details, and model notes
- `VERSION_HISTORY.md` — version-by-version project progression
- `.gitignore` — ignores virtual environments and test logs

## How it works

1. Ollama runs in the background as a local service on its default port (`http://localhost:11434`).
2. The Python script connects to Ollama and sends test prompts to each model.
3. The script records how long each model took to reply and how many tokens per second it generated.
4. Results are printed in a clean comparison table in the terminal.
5. Everything runs locally on the graphics card with no internet connection required during testing.

## Roadmap

Planned milestones for future versions include:
- writing the first Python benchmark script to test response speed
- creating standard test prompts for general knowledge, reasoning, and coding
- adding image testing for `moondream` and `llava:7b`
- saving test results to CSV or JSON files for easy review
- adding simple charts to compare tokens per second across models
- adding command-line options to run specific models or test categories

## Local setup

This project uses a virtual environment to keep dependencies clean.

1. Check if Ollama is running and see available models:
```powershell
ollama list
```
*(If you see an error that Ollama cannot connect, launch **Ollama** from your Windows Start Menu, or run `ollama serve` in a terminal).*

2. Download all test models in one chained command:
```powershell
ollama pull llama3.2:3b; ollama pull llama3.1:8b; ollama pull qwen2.5-coder:7b; ollama pull deepseek-r1:8b; ollama pull gemma2:9b; ollama pull mistral:7b; ollama pull moondream; ollama pull llava:7b
```

3. Create and activate a virtual environment:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

4. Install Python dependencies:
```powershell
pip install -r requirements.txt
```

5. Run the benchmark script:
```powershell
python benchmark.py
```

## Important note on cost and privacy

All models in this project run 100% locally:
- **No cost**: The models and Ollama are completely free to use. There are no API keys, subscriptions, or token fees.
- **Complete privacy**: Prompts, test data, and images stay on this computer and are never sent over the internet.

## Version history

This repo is intentionally structured as an evolving project rather than a single static script, so the GitHub history and [VERSION_HISTORY.md](VERSION_HISTORY.md) show how the project grows as new skills are learned.
