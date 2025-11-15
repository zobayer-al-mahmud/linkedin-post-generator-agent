**Sample Video**

[Desktop 2025.11.14 - 22.31.46.01.webm](https://github.com/user-attachments/assets/332cd2ac-7ed7-49ca-b030-0c13bb0b7cf1)




# 🤖 LinkedIn Post Generator - AI Agent

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991.svg)](https://github.com/marketplace/models)

AI agent that generates professional LinkedIn posts using GitHub Models (OpenAI GPT-4o-mini).

## ✨ Features

- 📝 Automated 2-4 paragraph LinkedIn posts
- 🌐 Multi-language support (100+ languages)
- 💼 Professional tone
- 📊 Word & character count analytics
- ⚡ Only 2 dependencies

## 🚀 Quick Start

```bash
# Install
pip install -r requirements.txt

# Configure (edit .env)
GITHUB_TOKEN=your_github_token_here

# Run
python linkedin_agent.py
```

## 💻 Usage

### CLI Mode

```bash
python linkedin_agent.py
```

### Python API

```python
from linkedin_agent import LinkedInPostAgent

agent = LinkedInPostAgent()
post = agent.generate_post("AI in Healthcare", "English")
print(post)
```

## 📖 Example Output

**Input:** Topic: "Remote Work", Language: "English"

**Output:**
```
As we navigate through 2025, remote work has evolved from a temporary 
solution to a permanent fixture in the modern workplace...

[2-4 professional paragraphs]
```

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| `ValueError: GitHub token not found` | Add `GITHUB_TOKEN` to `.env` file |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |

## 📚 Tech Stack

- Python 3.8+
- OpenAI SDK (>=1.30.0)
- GitHub Models API
- GPT-4o-mini model

---

**Built with GitHub Models 🚀**
