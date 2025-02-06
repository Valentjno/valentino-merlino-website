import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Valentino Merlino - AI Trustworthy Expert | Researcher", 
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM STYLES ---
st.markdown(
    """
    <style>
        /* Softer Dark Theme */
        .stApp {
            background-color: #f4f4f7; /* Light gray-blue */
            color: #222222; /* Dark text */
        }

        /* Containers */
        .stMarkdown, .stDataFrame, .stTextInput, .stTextArea, .stButton {
            background: rgba(0, 0, 0, 0.03);
            border-radius: 10px;
            padding: 10px;
        }

        /* Headers */
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #2A3D66; /* Deep blue */
        }

        .subtitle {
            font-size: 24px;
            font-weight: bold;
            color: #005A8D; /* Medium blue */
        }

        /* Footer */
        .footer {
            font-size: 14px;
            color: gray;
            text-align: center;
            padding-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- HEADER SECTION ---
st.markdown('<div class="container">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])

with col1:
    st.image("https://media.licdn.com/dms/image/v2/C4D03AQHBGiAnsLA9Wg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1601298916699?e=1744243200&v=beta&t=NenGp1ROj_yZmLWZq6Z-6OloUOUm60RAx-9RSTbg4iQ", 
             caption="Valentino Merlino", 
             use_container_width=True)

with col2:
    st.markdown('<p class="title">AI Security Expert | Researcher</p>', unsafe_allow_html=True)
    st.write("Passionate about AI Ethics, Red Teaming, and Secure AI Systems.")
    st.markdown("""
    - 🎓 **PhD candidate in AI Security**  
    - 🏆 **Expert in AI Red Teaming & Adversarial Testing**  
    - 📖 **Published Researcher in IoT Security and Adversarial Machine Learning**
    """)

# --- SOCIAL LINKS ---
st.markdown('<p class="subtitle">🔗 Connect with Me</p>', unsafe_allow_html=True)
st.markdown("""
- 🏢 [LinkedIn](https://linkedin.com/in/yourusername)  
- 🧑‍💻 [GitHub](https://github.com/yourusername)  
- 📚 [Google Scholar](https://scholar.google.com/citations?user=yourID)  
- 🏴‍☠️ [HackTheBox](https://www.hackthebox.com/user/yourprofile) | [Crucible](https://www.crucible.io/profile/yourusername)  
- 📧 **Email**: [valentino.merlino@example.com](mailto:valentino.merlino@example.com)
""")

# --- ABOUT SECTION ---
st.markdown('<p class="subtitle">👨‍💻 About Me</p>', unsafe_allow_html=True)
st.write("""
I am a dedicated researcher focused on **AI security, adversarial testing, and ethical AI development**.  
My work explores **bias mitigation, AI robustness, and security vulnerabilities** in modern machine learning systems.  
I collaborate with academia, industry, and AI red teaming communities to ensure AI is **fair, accountable, and resilient**.
""")

# --- AI RED TEAMING SECTION ---
st.markdown('<p class="subtitle">🛡️ AI Red Teaming</p>', unsafe_allow_html=True)
st.write("""
- **Adversarial Attacks & Defense**: Conducting penetration testing against AI models.  
- **Bias & Fairness Audits**: Evaluating AI systems for **algorithmic bias and ethical risks**.  
- **Red Team Simulations**: Participating in AI **attack simulations & vulnerability assessments**.
""")

# --- MEMBERSHIPS & STANDARDS SECTION ---
st.markdown('<p class="subtitle">🏛️ Standards & Committees</p>', unsafe_allow_html=True)
st.write("""
- **ISO/IEC JTC 1/SC 42 - Artificial Intelligence**  
- **CEN-CENELEC JTC 21 ‘Artificial Intelligence’**  
- **OWASP AI EXCHANGE**  
""")

# --- RESEARCH & PUBLICATIONS ---
st.markdown('<p class="subtitle">📄 Published Papers</p>', unsafe_allow_html=True)
st.write("""
- 📝 **"Ethical AI: A Framework for Fairness and Accountability"** – Journal of AI Ethics, 2024  
- 🔬 **"Adversarial Robustness in NLP: Mitigation Strategies"** – International Conference on Machine Learning, 2023  
- 📊 **"Bias in Large Language Models: Detection & Correction"** – AI Policy Journal, 2022  
""")

# --- PROJECTS & CONTRIBUTIONS ---
st.markdown('<p class="subtitle">🔬 Research & Projects</p>', unsafe_allow_html=True)
st.write("""
- **Trustworthy AI Framework** – Developed a framework for evaluating AI models based on **fairness, robustness, and transparency**.  
- **Security Testing in Generative AI** – Analyzed **GPT-like models for prompt injection and adversarial manipulation**.  
- **AI Explainability** – Worked on **XAI techniques to make neural networks interpretable** for decision-making in healthcare.  
""")

# --- FOOTER ---
st.write("---")
st.markdown('<p class="footer">© 2025 Valentino Merlino | AI Security Expert </p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
