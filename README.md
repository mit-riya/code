# Codeforces AI

## About Codeforces AI
This is an AI App to get up-to-date information about recent contests on the competitive programming platform, Codeforces. It uses Pathway’s [LLM App features](https://github.com/pathwaycom/llm-app) to build real-time LLM(Large Language Model)-enabled data pipeline in Python and join data from multiple input sources, leverages [OpenAI API Embeddings](https://platform.openai.com/docs/api-reference/embeddings) and [Chat Completion](https://platform.openai.com/docs/api-reference/completions) endpoints to generate AI assistant responses.
## Demo

https://github.com/mit-riya/codeforces_gpt/assets/95142933/90581da5-834d-4da2-8d17-a373b1e7f24c

## Setup

### Step 1: Clone this repo
Clone this repo using

    git clone https://github.com/mit-riya/codeforces_gpt.git

And move to the folder using

    cd codeforces_llm_app

### Step 2: Create .env file

    OPENAI_API_TOKEN={OPENAI_API_KEY}
    HOST=0.0.0.0
    PORT=8080
    EMBEDDER_LOCATOR=text-embedding-ada-002
    EMBEDDING_DIMENSION=1536
    MODEL_LOCATOR=gpt-3.5-turbo
    MAX_TOKENS=200
    TEMPERATURE=0.0

### Step 3: Install all dependencies

Install dependencies using

    pip install --upgrade -r requirements.txt

### Step 4: Run the files

Have 2 terminals, and in each terminal run each of the following commands

    python3 main.py

    streamlit run ui.py
### Step 5: Use the UI interface to start using the tool!

Ask away the questions related to repo or anything else that you want!
