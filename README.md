# ⌚ Omnitrix AI Interface  
### A Character-Based LLM Chatbot using Streamlit + Ollama

Omnitrix AI Interface is a themed character chatbot inspired by the Omnitrix system.  
It runs locally using Ollama models and provides an immersive green-themed sci-fi UI built with Streamlit.

The bot speaks as an Omnitrix AI system with configurable model selection and temperature control.

---

## 🚀 Features

- 🟢 Custom Omnitrix-themed UI
- 🤖 Local LLM via Ollama
- 🔄 Model Switching (Gemma3 / Llama3)
- 🌡 Adjustable Temperature (Energy Level)
- 🧠 Custom System Prompt Control
- 💬 Chat History (Session State)
- ⚡ 4-Line Controlled Response Mode
- ♻️ Reboot / Clear Chat Option
- 💻 Fully Local (No API Keys Required)

---

## 🏗 How It Works

1. User enters command
2. System prompt defines Omnitrix personality
3. Selected Ollama model processes request
4. Response is limited to 4 lines
5. Chat history stored in session state
6. Messages displayed in reversed order (newest first)

---

## 🧰 Requirements

- Python 3.10+
- Ollama installed
- Streamlit
- Ollama Python package

---

## 📦 Install Dependencies

Create virtual environment (recommended):

```bash
python -m venv project
project\Scripts\activate
```

Install required packages:

```bash
pip install streamlit
pip install ollama
```

---

## 🧠 Install Ollama Models

Make sure Ollama is installed.

Pull required models:

```bash
ollama pull gemma3:latest
ollama pull llama3:latest
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

(or replace `app.py` with your filename)

The interface will open in your browser.

---

## 🎛 Sidebar Controls

| Control | Function |
|----------|----------|
| Alien Species | Select LLM Model |
| Energy Level | Adjust temperature |
| Reboot Omnitrix | Clear chat history |

---

## 🧪 Example Input

```
Scan for nearby alien DNA signatures.
```

Example behavior:
- Technical tone
- Heroic personality
- Maximum 4 lines
- Omnitrix-style response

---

## 🎨 UI Design Highlights

- Neon green sci-fi theme
- Custom CSS styling
- Radial glowing buttons
- Reversed chat order display
- Styled sidebar panel

---

## 🛠 Core Technologies

- Streamlit (Frontend)
- Ollama (Local LLM Engine)
- Gemma3 / Llama3 (Models)
- Python Session State Management

---

## 💡 Customization

You can modify:

- Default system prompt
- Maximum response length
- UI theme colors
- Available models
- Temperature range

---

## 📜 License

For educational and experimental use.

---

## 👤 Author

Your Name  
GitHub: https://github.com/yourusername
