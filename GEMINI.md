# LLM Functions CLI - GEMINI.md

## Project Overview

This project, `llm-functions`, provides a framework for developing and integrating custom tools and agents with Large Language Models (LLMs). It simplifies the process of connecting LLMs to external code written in Bash, JavaScript, and Python, primarily through function calling capabilities. The project is designed to be used with AIChat and adheres to OpenAI's function calling specifications.

-   **Purpose:** To enable LLMs to execute custom code, interact with system commands, process data, and call external APIs seamlessly.
-   **Core Technologies:** Bash, JavaScript, Python, `argc` (command-line framework and runner), `jq` (JSON processor).
-   **Integration:** Primarily with AIChat, leveraging OpenAI's function calling mechanism.

## Building and Running

The project utilizes the `argc` tool for managing builds, dependencies, and execution.

### Prerequisites

*   `argc`: A bash command-line framework and command runner.
*   `jq`: A JSON processor.

### Setup and Build Process

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/sigoden/llm-functions
    cd llm-functions
    ```
2.  **Define Tools and Agents:**
    *   Create a `./tools.txt` file listing the names of the tools to be included (e.g., `get_current_weather.sh`, `execute_command.sh`).
    *   Create a `./agents.txt` file listing the names of the agents to be included (e.g., `coder`, `todo`).
3.  **Build Project Artifacts:**
    *   Run `argc build` to generate necessary files like `bin/` executables and `functions.json` (tool/agent declarations).
4.  **Check Environment:**
    *   Run `argc check` to verify that all dependencies (Node.js, Python, etc.) and environment variables are correctly set up.
5.  **Integrate with AIChat:**
    *   **Symlink:** Link the `llm-functions` directory to AIChat's `functions_dir`:
        ```bash
        ln -s "$(pwd)" "$(aichat --info | sed -n 's/^functions_dir\s\+//p')"
        # Or use the convenience command:
        argc link-to-aichat
        ```
    *   **Environment Variable:** Set the `AICHAT_FUNCTIONS_DIR` environment variable:
        ```bash
        export AICHAT_FUNCTIONS_DIR="$(pwd)"
        ```
6.  **Usage:**
    *   Interact with tools and agents via AIChat:
        ```bash
        aichat --role %functions% "what is the weather in Paris?"
        aichat --agent todo "list all my todos"
        ```

## Development Conventions

### Tool Development

*   **Languages:** Tools can be written in Bash, JavaScript, or Python.
*   **Declarations:** Tool metadata (description, arguments) is auto-generated from specially formatted comments within the tool scripts (e.g., `# @describe`, `# @option` for Bash; `/** @typedef`, `@property` for JS/Python).
*   **Location:** Tool scripts are typically placed in the `./tools/` directory.
*   **Execution:** Scripts like `./scripts/run-tool.sh`, `./scripts/run-tool.js`, and `./scripts/run-tool.py` are used to execute individual tools.

### Agent Development

*   **Structure:** Agents follow a specific directory structure within `./agents/`.
    *   `index.yaml`: Defines the agent's name, description, instructions, conversation starters, variables, and documents.
    *   `tools.txt`: Lists shared tools available to the agent.
    *   `functions.json`: Auto-generated JSON declarations for the agent's functions.
*   **Components:** Agents combine prompts (instructions), tools (function calling), and documents (RAG - Retrieval Augmented Generation).
*   **Execution:** Scripts like `./scripts/run-agent.sh`, `./scripts/run-agent.js`, and `./scripts/run-agent.py` are used to run agents.

### Build and Management

*   The `argc` command is central to the project's workflow, handling tasks such as:
    *   `argc build`: Generates tool/agent declarations and executables.
    *   `argc check`: Verifies project dependencies and environment setup.
    *   `argc link-web-search <tool_script>`: Creates a symbolic link for a specific web search tool to be used as a generic `web_search`.
    *   `argc link-to-aichat`: Facilitates linking the project to AIChat.

### Ignored Files (`.gitignore`)

The `.gitignore` file specifies files and directories that should not be tracked by Git, including:
*   Temporary files and directories (`/tmp`, `/cache`).
*   Generated artifacts (`functions.json`, `/bin`, symlinks like `/tools/web_search.*`).
*   Environment-specific directories (`/.venv`, `node_modules`).
*   Configuration files (`.env`, `package-lock.json`, `*.lock`).

## Key Files and Directories

*   `./tools/`: Contains the implementation of individual LLM tools.
*   `./agents/`: Contains the definitions and configurations for LLM agents.
*   `./scripts/`: Houses utility scripts for building, running, and managing tools and agents.
*   `README.md`: Main project documentation.
*   `.gitignore`: Git ignore rules.
*   `argcfile.sh`: (Implicitly used by `argc` commands) Configuration for the `argc` framework.

## Roles

This project defines several roles that can be adopted by the AI agent, each with specific instructions and capabilities:

### AutoGPT Role (`roles/autogpt.md`)

*   **Description:** Designed to automate user tasks by analyzing, writing, and coding. It executes tasks directly without explicit prompting for each step.
*   **Skills:** Analyzing, Writing, Coding, Executing tasks automatically.
*   **Requirements Handling:**
    *   **Small Questions:** Answers directly and in-depth.
    *   **Big Projects:** Involves key analysis, project structure definition, step-by-step execution, and automatic continuation.
*   **Output Requirements:** Structured, markdown-formatted, detailed, accurate, and in-depth content.

### Smart Dev Role (`roles/smart-dev.md`)

*   **Description:** Focuses on fixing programs, providing bug-free, well-commented code, and implementing detailed architecture. It emphasizes writing detailed code, starting with core components, and outputting each file's content.
*   **Tasks:**
    *   **Fix Program:** Provides bug-free, well-commented code.
    *   **Write Detailed Code:** Implements architecture, starting with core classes/functions/methods, and includes brief comments.
    *   **Output File Content:** Follows markdown code block format, ensuring full functionality.
*   **Review Task:** Summarizes unclear instructions, asks clarification questions, and reviews feature specifications like a Google engineer.
*   **Spec Creation Task:** Creates detailed program specifications, including features, classes, functions, methods, and comments, outputting file content in markdown code blocks.