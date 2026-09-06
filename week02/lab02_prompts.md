# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

I installed the GitHub Copilot CLI on my system and successfully authenticated the tool using the official browser authentication flow.
Version: 1.0.82

### Antigravity CLI

I installed the Antigravity CLI on my system and successfully authenticated the tool using the official authentication flow.
Version: 1.1.23

## Shared task

### Shared prompt

```text
Are you able to help plan a script that can read a file containing an annual financial report that can help predict projections for the next year?
```

### Copilot CLI observations

From what I noticed, when I prompted Copilot if it could make a simple script, it laid out what it would do and the full capabilities of what the script would do without giving me any actual code. After stating what the script would be capable of, it gave more insight and suggestions on how to actually set it up and separate certain documents as well as what to test before continuing. While I did question how exactly it would set everything up, I like the clarity that it provides in what to look over and verify initially and continuously as I build upon the idea.

### Antigravity CLI observations

When I asked Antigravity the exact same prompt, I preferred the interactive approach that it took after the initial prompt. The time to think was a bit longer, but completely transparent. Instead of a generic thinking indicator, Antigravity actively showed its chain of reasoning when generating an answer. What I really liked about Antigravity is that it asked follow-up questions to ensure the implementation did not become overly complex and to clarify exactly what was needed from the script. Even in planning mode, Antigravity generated an implementation plan artifact with the proposed design, explaining how the script will work hypothetically and how each component fits together.

### Comparison

Between the two CLIs, I found that both provided valuable perspectives with contrasting styles. I originally had the impression that Antigravity is geared heavily toward end-to-end automation and deep Python workflows, whereas GitHub Copilot is more beginner-friendly and oriented toward conversational scaffolding. When comparing both tools on the same prompt, Copilot CLI gave a concise structural outline and immediate next steps without writing unrequested code, whereas Antigravity CLI was more curious, asking clarifying follow-up questions and offering a concrete implementation artifact to review before making changes. Both approaches provided clarity, but Antigravity gave stronger upfront verification and planning artifacts. For day-to-day development, combining both agents offers a balanced workflow where Antigravity handles structured multi-step planning while Copilot provides fast terminal feedback.

## Test-guided implementation

Running the automated pytest suite against the initial codebase immediately revealed missing module errors and provided a clear specification for each function contract. For make_greeting, the behavioral tests verified that both single-word and multi-word names work properly, and specifically enforced that an empty string must format directly as 'Hello, !' without extraneous spacing or fallback values. For is_even, using the standard modulo operator number % 2 == 0 satisfied all test cases seamlessly across positive integers, odd numbers, zero, and negative values like -4 and -3, confirming Python's modulo behavior with negative dividends. For count_vowels, inspecting test_lab02.py highlighted two critical edge cases: case insensitivity (such as in 'OpenAI' containing uppercase and lowercase vowels) and ensuring that the letter 'y' is strictly excluded (as demonstrated by 'rhythms' evaluating to zero). Implementing a set lookup over lowercased characters satisfied all behavioral constraints without unnecessary complexity or external dependencies.

## Preferred tool combination

In evaluating my development workflow, each tool offers distinct advantages depending on the programming phase. Browser chat tools like ChatGPT or Copilot Web are fantastic for high-level architectural brainstorming, conceptual explanations, and exploring general paradigms before writing any code. GitHub Copilot embedded in VS Code provides inline code completions and fast auto-suggestions for repetitive syntax or boilerplate methods right inside the editor. On the command line, Copilot CLI serves well for quick terminal commands and concise script outlines, but Antigravity CLI stands out for agentic planning, multi-step reasoning, transparent thought traces, and file creation with thorough plans. My current preferred combination is using Antigravity CLI for planning and decomposing complex tasks, paired with GitHub Copilot inside VS Code for real-time code editing. However, if I am working on an isolated task that requires rapid, single-line terminal command lookups without generating project artifacts, I would shift toward using standard Copilot CLI or direct browser chat for quick reference.
