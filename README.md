# Merse Puch GPT 🤖

A powerful AI persona chatbot built with Groq API that can generate code and engage in human-like conversations. Built with Streamlit for an intuitive web interface.

## Features ✨

- **Code Generation**: Generate code in multiple programming languages
- **Human-like Conversations**: Natural, engaging dialogue powered by advanced AI
- **Custom Persona**: Unique "Merse Puch" personality with specialized responses
- **Fast Performance**: Powered by Groq API for lightning-fast responses
- **User-friendly Interface**: Clean Streamlit web app for easy interaction

## Technologies Used 🛠️

- **Groq API**: High-performance AI inference
- **Streamlit**: Web application framework
- **Python**: Core programming language
- **Custom System Prompts**: Tailored persona behavior

## Installation 🚀

1. **Clone the repository**
   ```bash
   git clone https://github.com/surjanthakur/AI-persona-GPT.git
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

## Usage 💬
2. Start chatting with Merse Puch GPT
3. Ask for code generation, explanations, or engage in general conversation
4. The AI will respond in character with helpful and human-like responses

## Example Interactions 💭

**Code Generation:**
```
User: "Generate a Python function to calculate fibonacci numbers"
Merse Puch GPT: [Provides clean, commented code with explanation]
```

**General Conversation:**
```
User: "How are you today?"
Merse Puch GPT: [Responds naturally with personality]
```

## Configuration ⚙️

The system prompt and persona behavior can be customized in the configuration file. Key settings include:

- Response style and tone
- Code generation preferences
- Personality traits
- Special capabilities

## Project Structure 📁

```
merse-puch-gpt/
├── main.py                 # Main Streamlit application
├── config/
│   ├── system_prompt.txt  # Custom persona system prompt
│   └── settings.py        # Configuration settings
├── utils/
│   ├── groq_client.py     # Groq API client wrapper
│   └── helpers.py         # Utility functions
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
└── README.md             # This file
```

## API Key Setup 🔑

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in to your account
3. Generate a new API key
4. Add it to your `.env` file

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting 🔧

**Common Issues:**

- **API Key Error**: Ensure your Groq API key is correctly set in the `.env` file
- **Module Not Found**: Run `pip install -r requirements.txt` to install dependencies
- **Streamlit Port Conflict**: Use `streamlit run app.py --server.port 8502` for alternate port

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- [Groq](https://groq.com/) for providing fast AI inference
- [Streamlit](https://streamlit.io/) for the excellent web framework
- The open-source community for inspiration and tools

## Contact 📧

- **Developer**: [surjanthakur]
- **Email**: your.tsurjan506@gmail.com
-  instagram : https://www.instagram.com/epicsurjanthakur/
---

**Made with ❤️ and AI**

*Merse Puch GPT - Where code meets conversation!*
