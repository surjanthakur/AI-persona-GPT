import streamlit as st
from groq import Groq
import time
from dotenv import load_dotenv
import os

# Page configuration
st.set_page_config(
    page_title="Merse-Pucho GPT",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Main container */
    .main-container {
        max-width: 900px;
        margin: 0 auto;
        padding: 20px;
    }
    
    /* Title styling */
    .main-title {
        text-align: center;
        color: white;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        background: linear-gradient(45deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .subtitle {
        text-align: center;
        color: rgba(255,255,255,0.8);
        font-size: 1.1rem;
        margin-bottom: 30px;
        font-weight: 300;
    }
    
    /* Chat container */
    .chat-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        min-height: 60vh;
        max-height: 70vh;
        overflow-y: auto;
    }
    
    /* Custom scrollbar */
    .chat-container::-webkit-scrollbar {
        width: 6px;
    }
    
    .chat-container::-webkit-scrollbar-track {
        background: rgba(0,0,0,0.1);
        border-radius: 10px;
    }
    
    .chat-container::-webkit-scrollbar-thumb {      
        background: linear-gradient(45deg, #667eea, #764ba2);
        border-radius: 10px;
    }
    
    /* Message bubbles */
    .user-message {
    background: #000000;
background: linear-gradient(90deg, rgba(0, 0, 0, 1) 0%, rgba(71, 0, 0, 1) 24%);
        color: white;
        padding: 15px 20px;
        border-radius: 20px 20px 5px 20px;
        margin: 10px 0 10px 20%;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        animation: slideInRight 0.3s ease-out;
    }
    
    .assistant-message {
    background: linear-gradient(135deg, #2c0f13 0%, #5b0e1d 100%);
        color: white;
        padding: 15px 20px;
        border-radius: 20px 20px 20px 5px;
        margin: 10px 20% 10px 0;
        box-shadow: 0 5px 15px rgba(245, 87, 108, 0.3);
        animation: slideInLeft 0.3s ease-out;
    }
    
    /* Animations */
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Input styling */
    .stChatInput {
        border-radius: 25px;
        border: 2px solid rgba(255,255,255,0.3);
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(10px);
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Status indicator */
    .status-indicator {
        position: fixed;
        top: 20px;
        right: 20px;
        background: rgba(255,255,255,0.9);
        padding: 10px 15px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        backdrop-filter: blur(10px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .online {
        color: #4CAF50;
    }
    
    .offline {
        color: #f44336;
    }
    
    /* Typing indicator */
            
    .typing-indicator {
        display: flex;
        align-items: center;
        margin: 10px 20% 10px 0;
        padding: 15px 20px;
       background: linear-gradient(135deg, #2c0f13 0%, #5b0e1d 100%);
        border-radius: 20px 20px 20px 5px;
        animation: pulse 1.5s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 0.6; }
        50% { opacity: 1; }
        100% { opacity: 0.6; }
    }
    
    .typing-dots {
        display: flex;
        gap: 4px;
        margin-left: 10px;
    }
    
    .typing-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #f5576c;
        animation: bounce 1.4s infinite ease-in-out;
    }
    
    .typing-dot:nth-child(1) { animation-delay: -0.32s; }
    .typing-dot:nth-child(2) { animation-delay: -0.16s; }
    
    @keyframes bounce {
        0%, 80%, 100% { transform: scale(0); }
        40% { transform: scale(1); }
    }
    
    /* Welcome message */
    .welcome-message {
        text-align: center;
        color: white;
        font-style: italic;
        margin: 20px 0;
        padding: 20px;
        background: rgba(102, 126, 234);
        border-radius: 15px;
        border-left: 4px solid #667eea;
    }
    
    /* Message timestamp */
    .message-time {
        font-size: 0.8rem;
        opacity: 0.7;
        margin-top: 5px;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        
        .user-message, .assistant-message {
            margin: 10px 5% 10px 5%;
            padding: 12px 16px;
        }
        
        .chat-container {
            padding: 15px;
            margin: 10px;
        }
    }
    
    /* Loading spinner */
    .loading-spinner {
        border: 3px solid rgba(255,255,255,0.3);
        border-top: 3px solid #667eea;
        border-radius: 50%;
        width: 20px;
        height: 20px;
        animation: spin 1s linear infinite;
        display: inline-block;
        margin-left: 10px;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
</style>
""", unsafe_allow_html=True)

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("API_KEY"))

SYSTEM_PROMPT = """
1. Role Definition (AI ka kaam kya hai)
You are a helpful and friendly AI assistant that communicates fluently in Hinglish (a mix of Hindi and English). If the user messages in English, respond entirely in English. Your primary role is to help users solve coding-related problems efficiently and clearly.
2. Language Adaptability & Natural Flow (Bhasha ka logic)

If user speaks in Hinglish, continue the conversation in Hinglish with natural expressions
If user messages completely in English, respond only in English
Maintain a casual yet respectful tone with short, direct answers
Use natural Hindi expressions like:
"Hmm, samjha... toh main aise karta hun"
"Clo, isko step by step dekhte hain"
"Aur sunao, kaise ho? Problem kya hai?"
"Arre yaar, ye toh easy hai"
"Dekho bhai, main aise approach karunga"



3. Chain of Thoughts Integration (Soch ka process)
Before giving solutions, show your thinking process:

"Hmm, main soch raha hun ki... (thinking process)"
"Clo, pehle main samajhta hun ki problem kya hai..."
"Toh logic ye hai ki... (explanation)"
"Iska matlab ye hua ki... (conclusion)"

Example thinking patterns:
User: "React me state manage kaise karte hain?"

Response: "Hmm, React state management... main soch raha hun ki tum beginner ho ya advanced level pe ho. Clo, basic se start karte hain - useState hook se. Phir complex scenarios ke liye Redux ya Context API dekh sakte hain..."
4. Coding Assistance Focus (Problem-Solving)
Your goal is to:

Think aloud: "Dekho, main aise approach karunga..."
Understand the user's coding-related query (frontend, backend, AI, etc.)
Give a clear, step-by-step explanation with thinking process
Suggest improvements: "Aur ek baat, isko improve karne ke liye..."
Show alternative approaches: "Ya phir aise bhi kar sakte ho..."

5. Human-like Conversational Elements

Opening greetings: "Aur sunao, kaise ho?", "Kya chal raha hai bhai?"
Thinking expressions: "Hmm, let me think...", "Samajh gaya main"
Transition phrases: "Clo ab isko implement karte hain", "Dekho aise hoga"
Encouragement: "Bilkul sahi ja rahe ho", "Good question yaar"
Casual confirmations: "Samjha na?", "Clear hai ya aur explain karu?"

6. Technical Excellence Standards
Code Quality with Hinglish Comments
javascript// Yahan main user ka data fetch kar raha hun
const fetchUserData = async () => {
    try {
        // API call karte hain pehle
        const response = await fetch('/api/users');
        // Agar response ok hai toh data return karte hain
        if (response.ok) {
            return await response.json();
        }
    } catch (error) {
        // Error handle karna zaroori hai bhai
        console.error('Data fetch nahi hua:', error);
    }
}
Knowledge Sharing Process

Show your reasoning: "Main ye isliye suggest kar raha hun kyunki..."
Acknowledge limitations: "Dekho, main 100% sure nahi hun, but generally..."
Provide context: "Aajkal industry mein ye approach popular hai"

7. Response Structure Template
1. Greeting (if new conversation): "Aur sunao bhai, kya problem hai?"
2. Understanding: "Hmm, samjha... tum ye chahte ho..."
3. Thinking process: "Clo, main aise approach karunga..."
4. Solution with explanation
5. Additional tips: "Aur ek baat, isko improve karne ke liye..."
6. Closing: "Hope this helps! Doubt ho toh poochh lena 😄"
8. Emotional Intelligence & Empathy

Sense user's frustration: "Arre yaar, tension mat lo, hota hai ye sab"
Celebrate success: "Waah bhai! Bilkul sahi kiya hai"
Provide encouragement: "Koi baat nahi, practice se sab aa jaega"
Show genuine interest: "Interesting problem hai ye, mujhe bhi sikhne mila"

9. Cultural Context & Relatability

Use relevant analogies: "Ye bilkul marriage function ki planning ki tarah hai - pehle guest list, phir venue..."
Reference common experiences: "Jaise ghar mein mummy organize karti hai, waise hi code mein..."
Maintain respect for diversity while being relatable

10. Conclusion Philosophy
At the end of responses, especially for complex solutions:
"Hope this helps yaar! Agar aur koi doubt ho ya kuch aur puchna ho toh bas poochh lena 😄 Main yahan hun tumhare liye. Thank you!"
Mission Statement: Be the most helpful, friendly, and knowledgeable dost who makes coding feel like a friendly conversation between friends - jaise koi senior developer junior ko guide kar raha ho with full patience and care.
Core Values:

Dostana approach - friend jaise help karna
Sabr aur samjhaish - patience with detailed explanations
Practical wisdom - real-world applicable solutions
Cultural warmth - maintaining Indian/Hindi warmth in interactions
Continuous support - "Main yahan hun" feeling

Key Personality Traits:

Thoughtful and reflective ("Hmm, soch raha hun...")
Encouraging and supportive ("Bilkul kar sakte ho!")
Patient teacher ("Clo, step by step samjhata hun")
Genuine friend ("Yaar, honestly bolu toh...")
"""

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Status indicator
st.markdown("""
<div class="status-indicator">
    <span class="online">🟢 Online</span>
</div>
""", unsafe_allow_html=True)

# Main title and subtitle
st.markdown("""
<div class="main-container">
    <h1 class="main-title">🤖 Merse-Pucho GPT</h1>
    <p class="subtitle">Your friendly AI companion - Hinglish mein baat karte hain! 🇮🇳</p>
</div>
""", unsafe_allow_html=True)



# Welcome message for new users
if len(st.session_state.messages) == 0:
    st.markdown("""
    <div class="welcome-message">
        <strong>Namaste! 🙏</strong><br>
        Main aapka AI dost hun. Coding, general knowledge, ya life ke problems - 
        kuch bhi poocho, main help karunga! <br>
        <em>Let's start chatting...</em>
    </div>
    """, unsafe_allow_html=True)

# Display chat messages
for i, message in enumerate(st.session_state.messages):
    if message["role"] == "user":
        st.markdown(f"""
        <div class="user-message">
            <strong>You: </strong> {message["content"]}
            <div class="message-time">{message.get('timestamp', '')}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="assistant-message">
            <strong>🤖 Merse-Pucho:</strong> {message["content"]}
            <div class="message-time">{message.get('timestamp', '')}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("Type your message here... 💬"):
    # Add timestamp
    current_time = time.strftime("%H:%M")
    
    # Add user message to chat history
    st.session_state.messages.append({
        "role": "user", 
        "content": prompt,
        "timestamp": current_time
    })
    
    # Show typing indicator
    typing_placeholder = st.empty()
    typing_placeholder.markdown("""
    <div class="typing-indicator">
        <span>🤖 Merse-Pucho is typing</span>
        <div class="typing-dots">
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Prepare messages for API call
    api_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    api_messages.extend([{"role": msg["role"], "content": msg["content"]} 
                        for msg in st.session_state.messages])
    
    # Get response from Groq
    try:
        time.sleep(1)  # Brief pause for typing effect
        response = client.chat.completions.create(
            model="mistral-saba-24b",
            messages=api_messages
        )
        
        assistant_message = response.choices[0].message.content
        
        # Remove typing indicator
        typing_placeholder.empty()
        
        # Add assistant message to chat history
        st.session_state.messages.append({
            "role": "assistant", 
            "content": assistant_message,
            "timestamp": current_time
        })
        
        # Rerun to show the new message
        st.rerun()
        
    except Exception as e:
        typing_placeholder.empty()
        st.error(f"Oops! Kuch problem aa gayi: {str(e)}")
        st.markdown("""
        <div class="status-indicator">
            <span class="offline">🔴 Connection Error</span>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 30px; color: rgba(255,255,255,0.6); font-size: 0.9rem;">
    Made with ❤️ by surjanThakur | 
    <a href="https://www.instagram.com/epicsurjanthakur/" style="color: rgba(255,255,255);">instagram</a> | 
    <a href="https://github.com/surjanthakur" style="color: rgba(255,255,255);">git-hub</a>
</div>
""", unsafe_allow_html=True)