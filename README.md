# 🌌 **MultiverseMD** — Markdown-powered, Git-backed Conversations for LLMs

> _"Not just conversations—explore parallel conversational realities."_ ⚡ Inspired by **The Multiverse of Madness**

---

## 🚀 What is **multiversemd**?

**multiversemd** is your Markdown-first, Git-powered companion designed for managing and branching conversations with Large Language Models (LLMs). It leverages simple Markdown files and powerful branching logic to let you explore parallel paths effortlessly.

- **Markdown-based conversations**: Clear, readable Markdown pairs (`*_user.md` and `*_llm.md` files).
- **Branching edits**: Easily branch off conversations when editing older messages.
- **Git-enabled**: Track your conversational paths using the robust and familiar Git framework.

Think of it as navigating conversational timelines—like using Git for your chats, with effortless branching and merging of conversational realities.

---

## 🌟 Key Features (Planned):

- 📑 **Markdown-only approach**: Conversation history clearly structured and human-readable.
- 🔀 **Seamless Branch Management**: Auto-detect and manage conversation branching when older messages are edited.
- 🛠 **Real-time sidebar companion (REPL)**: Immediate command and configuration management through conversational interface.
- 🚦 **Persona Templates**: Easily adjust system messages, summary strategies, and context rules 'on-the-fly.'
- 📊 **Token & Model Tracking**: Instant visibility into tokens consumed and model usage.
- 🌐 **Multi-model Support**: Generate responses concurrently from multiple models and seamlessly compare them.

---

## 📂 File Structure

Each conversation ("session") is stored in a single folder, identified by a random-generated 4-character code:

```bash
session_rngb/
├── chat_rngb_001_aa_user.md
├── chat_rngb_001_aa_llm.md
├── chat_rngb_002_aa_user.md
├── chat_rngb_002_aa_llm.md
├── chat_rngb_003_aa_user.md
├── chat_rngb_003_aa_llm.md
├── chat_rngb_004_aa_user.md
└── chat_rngb_004_aa_llm.md
```

### 🔀 Branching logic example:

- If you edit an older message (e.g., **chat_rngb_003_aa_user.md**) after newer messages already exist, the branching logic kicks in automatically:
```bash
# After branching because chat_rngb_003_aa_user.md was edited:
session_rngb/
├── chat_rngb_001_aa_user.md
├── chat_rngb_001_aa_llm.md
├── chat_rngb_002_aa_user.md
├── chat_rngb_002_aa_llm.md
├── chat_rngb_003_aa_user.md      # original
│   └── chat_rngb_003_ab_llm.md   # newly branched response
└── chat_rngb_004_ab_user.md      # new branch continues here
```

---

## 💻 Conversational REPL Companion (Sidebar Assistant)

**Meet "Chronos"**— your conversational companion right in your terminal.

🔮 **Key features**:
- **Interactive configuration**: Change personas (system prompts), summarization rules, and context length through natural language prompts.
- **Real-time model control**: Switch between LLM models instantly or even run multiple models side by side.
- **Token & context transparency**: See exactly how many tokens your last interaction consumed.
- **Persona & summary management**: Easily change or reference summary prompts and personas stored in dedicated config files.

Example interactions you can have with Chronos:

```plaintext
> switch model to gpt-4-turbo
✅ Switched model to gpt-4-turbo.

> activate additional model mistral-13b
✨ Activated mistral-13b. Generating replies using gpt-4-turbo, mistral-13b.

> use assistant persona from ./personas/tech_advisor.md
🎭 Assistant persona updated to tech_advisor.

> set summary context to last 3 messages with ./prompts/summary_prompt.md
📝 Updated summarization: last 3 messages, summary_prompt.md applied.
```

---

## ⚡ Performance Targets (Planned)

| Action                          | Performance Goals |
|---------------------------------|-------------------|
| 🚀 Cold Start Init              | < 5 seconds       |
| ⏩ Warm Response Viewing         | < 1 second        |

---

## 🧰 Tech stack & Dependencies (Planned)

| Tool/Framework    | Purpose                            |
|-------------------|------------------------------------|
| **Python 3.10+**  | Core backend language              |
| **Git**           | Conversation version control       |
| **watchdog**      | Filesystem watcher integration     |
| **python-frontmatter** | YAML frontmatter parsing      |
| **GitPython**     | Git backend interaction            |
| **tiktoken**      | Token-count management precision   |
| **anytree**       | Conversation branch visualization  |

---

## 🗺 Implementation Roadmap 

Current Status: 🚧 Initial Planning (this is the very first doc!)

| Phase | Features                                 | Status       |
|-------|------------------------------------------|--------------|
| 1     | Core filesystem & markdown storage       | 📝 Planned   |
| 2     | Conversational CLI Companion ("Chronos") | 📝 Planned   |
| 3     | Branching, summarization, context mgmt   | 📝 Planned   |
| 4     | Multi-model integration                  | 📝 Planned   |
| 5     | VSCode integration & visualization tools | 📝 Planned   |

---

## 🍻 Contribute!

We're just getting started. If you're as geeked out on Markdown, Git, and conversational AI as we are, join us!

1. Fork this repo.
2. Propose features or improvements via issues.
3. Open pull requests—no contribution too big or small.  
4. Earn eternal gratitude in all branches of the multiverse 🙌.

---

## 📖 Licensing

Licensed under the MIT license - free to branch, merge, and remix conversational timelines at will!

---

> _"Every decision branches into new possibilities—make yours count."_ 🌟 — Inspired by Isaac Asimov

**multiversemd**: Git-based conversational exploration made excitingly easy. 🌌✨