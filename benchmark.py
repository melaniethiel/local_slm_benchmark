"""
Local SLM Benchmark (v0.2)
A benchmarking script to test and compare open-weights models running
locally via Ollama, measuring latency, token generation speed, and response quality.
"""

# ==============================================================================
# MODULE IMPORTS (External toolboxes we bring into this script)
# ==============================================================================
import sys
import ollama           # Official Python client for local Ollama server
from tabulate import tabulate  # Formats lists/data into clean display tables

# ==============================================================================
# CONFIGURATION VARIABLES (List and string objects)
# ==============================================================================
# List of text models to test in the benchmark
TEXT_MODELS = [
    "llama3.2:3b",
    "mistral:7b",
    "llama3.1:8b",
    "qwen2.5-coder:7b",
    "deepseek-r1:8b",
    "gemma2:9b",
]

# Standard test prompt to evaluate structure, explanation, and speed
# (You can change this to any prompt that fits your personality and interests!)
#TEST_PROMPT = (
#    "Share 3 practical tips for staying focused while working at a computer all day. "
#    "End with a 1-sentence reminder about taking breaks."
#)

TEST_PROMPT = (
    "Give me steps on how to teach a middle-school student how to do long division "
    "End with a motivational quote about an encouraging quote!"
)

# ==============================================================================
# BENCHMARK FUNCTION
# ==============================================================================
# This function runs the benchmark test by looping through each model, 
# feeding it the test prompt and adding results to a comparison display table
def run_benchmark():
    print("=" * 70)
    print(" LOCAL SLM BENCHMARK (v0.2)")
    print("=" * 70)
    print(f"Test Prompt: \"{TEST_PROMPT}\"\n")
    print("Starting benchmark runs...\n")

    # start with empty results and responses dictionaries (results uses a list for tabulate)
    results_table = []
    responses = {}

    # loop through each model using enumerate to track both the counter (1, 2, 3...) and the model name
    for index, model_name in enumerate(TEXT_MODELS, start=1):
        print(f"[{index}/{len(TEXT_MODELS)}] Running {model_name}...", end="", flush=True)

        try:
            # Send the prompt to the local Ollama instance (returns a response object with performance metadata)
            response = ollama.generate(
                model=model_name,
                prompt=TEST_PROMPT,
            )

            # Extract performance counters (Ollama reports durations in nanoseconds)
            # 1 second = 1,000,000,000 nanoseconds (1e9)
            total_duration_sec = response.get("total_duration", 0) / 1e9
            load_duration_sec = response.get("load_duration", 0) / 1e9
            eval_duration_sec = response.get("eval_duration", 0) / 1e9
            eval_count = response.get("eval_count", 0)  # Total output tokens generated

            # Calculate generation speed (tokens per second)
            tokens_per_sec = (eval_count / eval_duration_sec) if eval_duration_sec > 0 else 0.0

            # append results to the duration result table
            results_table.append([
                model_name,
                f"{load_duration_sec:.2f}s",
                f"{total_duration_sec:.2f}s",
                eval_count,
                f"{tokens_per_sec:.1f} tok/s",
            ])

            # add model specific response to the response list
            responses[model_name] = response.get("response", "").strip()

            # high level print duration details for current model
            print(f" Done ({total_duration_sec:.2f}s, {tokens_per_sec:.1f} tok/s)")

        # If error, print failure message and populate error values for results and responses
        except Exception as e:
            print(f" FAILED: {e}")
            results_table.append([model_name, "N/A", "ERROR", 0, "0.0 tok/s"])
            responses[model_name] = f"Error: {e}"

    # Print the comparison table
    print("\n" + "=" * 70)
    print(" BENCHMARK RESULTS")
    print("=" * 70)
    headers = ["Model", "VRAM Load Time", "Total Time", "Tokens Generated", "Generation Speed"]
    # tablefmt="github" formats the table using Markdown pipe syntax (| --- |) so it can be pasted into GitHub
    table_output = tabulate(results_table, headers=headers, tablefmt="github")
    print(table_output)
    print("=" * 70)

    # Display each model's output for qualitative comparison
    print("\n" + "=" * 70)
    print(" MODEL RESPONSES (QUALITY CHECK)")
    print("=" * 70)
    for model_name, text in responses.items():
        print(f"\n--- [{model_name}] ---")
        print(text)
        print("-" * 50)

    # ==========================================================================
    # SAVE RESULTS TO A FILE (Never lose outputs to terminal buffer limits)
    # ==========================================================================
    output_filename = "benchmark_run_latest.md"
    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(f"# Benchmark Run Results\n\n")
            f.write(f"**Prompt**: \"{TEST_PROMPT}\"\n\n")
            f.write(f"## Performance Summary\n\n")
            f.write(table_output + "\n\n")
            f.write(f"## Model Responses\n\n")
            for model_name, text in responses.items():
                f.write(f"### {model_name}\n\n")
                f.write(text + "\n\n")
                f.write("---\n\n")
        print(f"\n[+] Results successfully saved to: {output_filename}")
    except Exception as e:
        print(f"\n[-] Failed to save results file: {e}")

# ==============================================================================
# SCRIPT ENTRYPOINT
# ==============================================================================
# when this file is run as a script, call the main function
if __name__ == "__main__":
    run_benchmark()
