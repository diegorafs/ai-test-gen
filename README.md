# AI Test Scenario Generator

Automatically generate Gherkin feature files from requirements using AI.

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Generate Gherkin scenarios:
   ```
   python src/generate_gherkin.py
   ```
3. Find the output in `features/generated.feature`

## Extend
- Connect to OpenAI or other LLMs for better results
- Read requirements from markdown, Jira, Confluence, etc.
- Build a web UI for uploading requirements and downloading Gherkin files
