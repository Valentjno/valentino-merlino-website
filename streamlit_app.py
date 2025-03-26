import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Valentino Merlino | AI Red Teamer", 
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM STYLES ---
st.markdown(
    """
    <style>
        /* Load Poppins font from Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

        /* Global styles */
        .stApp {
            background-color: #f4f4f7; /* Light gray-blue */
            color: #333333; /* Darker text for better contrast */
            font-family: 'Poppins', sans-serif;
        }
        
        /* Responsive containers */
        .stMarkdown, .stDataFrame, .stTextInput, .stTextArea, .stButton {
            background: rgba(0, 0, 0, 0.05);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            transition: all 0.3s ease-in-out;
            cursor: pointer;
        }
        
        /* Hover effect on interactive elements */
        .stMarkdown:hover, .stButton:hover {
            transform: scale(1.05);
            background: rgba(0, 0, 0, 0.08);
        }

        /* Click effect: container grows */
        .stMarkdown:active, .stButton:active {
            transform: scale(1.1);
            background: rgba(0, 0, 0, 0.1);
        }

        /* Larger titles */
        .title {
            font-size: 4rem; /* Larger font size for better readability */
            font-weight: 700;
            color: #2A3D66;
            margin-bottom: 20px;
            line-height: 1.3;
            animation: fadeIn 2s ease-in-out;
        }
        
        /* Subtitles with larger font and smoother transition */
        .subtitle {
            font-size: 2.5rem;
            font-weight: 600;
            color: #005A8D;
            margin-top: 20px;
            margin-bottom: 15px;
            line-height: 1.4;
            animation: fadeIn 2s ease-in-out;
        }
        
        /* Footer */
        .footer {
            font-size: 1.5rem;
            color: #888;
            text-align: center;
            padding-top: 25px;
            padding-bottom: 20px;
            border-top: 1px solid #ddd;
            margin-top: 40px;
        }

        /* Image and text styling for header */
        .header-image {
            border-radius: 15px;
            max-width: 100%;
            height: auto;
            animation: fadeIn 2s ease-in-out;
        }
        
        /* Container styling */
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 30px;
            animation: fadeIn 2s ease-in-out;
        }
        
        @media (min-width: 768px) {
            .container {
                flex-direction: row;
                justify-content: space-between;
                align-items: center;
            }
            .header-image {
                max-width: 250px; /* Restrict image size on larger screens */
            }
        }

        /* Keyframe for fade-in effect */
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }

        /* Make emoji larger */
        .emoji {
            font-size: 2.5rem; /* Make the emojis larger */
        }

        /* Button styles */
        .stButton {
            display: inline-block;
            font-size: 1.2rem;
            font-weight: bold;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            margin: 5px;
        }

        .stButton:hover {
            transform: scale(1.05);
        }

        /* Button colors */
        .linkedin-button {
            background-color: #0077b5; /* Light blue */
        }

        .github-button {
            background-color: #333; /* Light black */
        }

        .google-scholar-button {
            background-color: #f7c800; /* Yellow */
        }

        .hackthebox-button {
            background-color: #28a745; /* Green */
        }

        .crucible-button {
            background-color: #f44336; /* Red */
        }

        .email-button {
            background-color: #9b59b6; /* Light purple */
        }

    </style>
    """,
    unsafe_allow_html=True
)

# --- SIDEBAR SECTION --- 
with st.sidebar:
    st.markdown('<p class="subtitle emoji">🔗 Connect with Me</p>', unsafe_allow_html=True)

    # Social link buttons with specific colors and emoticons
    st.markdown(
        f'<a href="https://linkedin.com/in/yourusername" target="_blank"><button class="stButton linkedin-button">🔗 LinkedIn</button></a>',
        unsafe_allow_html=True)
    st.markdown(
        f'<a href="https://github.com/yourusername" target="_blank"><button class="stButton github-button">🐱 GitHub</button></a>',
        unsafe_allow_html=True)
    st.markdown(
        f'<a href="https://scholar.google.com/citations?user=yourID" target="_blank"><button class="stButton google-scholar-button">📚 Google Scholar</button></a>',
        unsafe_allow_html=True)
    st.markdown(
        f'<a href="https://www.hackthebox.com/user/yourprofile" target="_blank"><button class="stButton hackthebox-button">🕵️‍♂️ HackTheBox</button></a>',
        unsafe_allow_html=True)
    st.markdown(
        f'<a href="https://www.crucible.io/profile/yourusername" target="_blank"><button class="stButton crucible-button">⚔️ Crucible</button></a>',
        unsafe_allow_html=True)
    st.markdown(
        f'<a href="mailto:valentino.merlino@example.com" target="_blank"><button class="stButton email-button">📧 Email</button></a>',
        unsafe_allow_html=True)

# --- HEADER SECTION ---
#st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<p class="title">AI Red Teamer | AI Security Researcher</p>', unsafe_allow_html=True)

# Image section
# Centered image section using Streamlit's columns layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("https://media.licdn.com/dms/image/v2/C4D03AQHBGiAnsLA9Wg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1601298916699?e=1744243200&v=beta&t=NenGp1ROj_yZmLWZq6Z-6OloUOUm60RAx-9RSTbg4iQ", 
             caption="Valentino Merlino", 
             use_container_width=False,
             width=250)

# Text section
st.markdown(""" 
- 🎓 **PhD candidate in AI Security**  
- 🏆 **Expert in AI Red Teaming & Adversarial Testing**  
- 📖 **Published Researcher in IoT Security and Adversarial Machine Learning**
""", unsafe_allow_html=True)

# --- ABOUT SECTION ---
st.markdown('<p class="subtitle emoji">👨‍💻 About Me</p>', unsafe_allow_html=True)
st.write(""" 
I am a dedicated researcher focused on **AI security, adversarial testing, and ethical AI development**.  
My work explores **bias mitigation, AI robustness, and security vulnerabilities** in modern machine learning systems.  
I collaborate with academia, industry, and AI red teaming communities to ensure AI is **fair, accountable, and resilient**.
""")

# --- AI RED TEAMING SECTION ---
st.markdown('<p class="subtitle emoji">🛡️ AI Red Teaming</p>', unsafe_allow_html=True)
st.write(""" 
- **Adversarial Attacks & Defense**: Conducting penetration testing against AI models.  
- **Bias & Fairness Audits**: Evaluating AI systems for **algorithmic bias and ethical risks**.  
- **Red Team Simulations**: Participating in AI **attack simulations & vulnerability assessments**.
""")

# --- MEMBERSHIPS & STANDARDS SECTION ---
st.markdown('<p class="subtitle emoji">🏛️ Standards & Committees</p>', unsafe_allow_html=True)
st.write(""" 
- **ISO/IEC JTC 1/SC 42 - Artificial Intelligence**  
- **CEN-CENELEC JTC 21 ‘Artificial Intelligence’**  
- **OWASP AI EXCHANGE**  
""")

# --- RESEARCH & PUBLICATIONS ---
st.markdown('<p class="subtitle emoji">📄 Published Papers</p>', unsafe_allow_html=True)
st.write(""" 
- 📝 **"Ethical AI: A Framework for Fairness and Accountability"** – Journal of AI Ethics, 2024  
- 🔬 **"Adversarial Robustness in NLP: Mitigation Strategies"** – International Conference on Machine Learning, 2023  
- 📊 **"Bias in Large Language Models: Detection & Correction"** – AI Policy Journal, 2022  
""")

# --- PROJECTS & CONTRIBUTIONS ---
st.markdown('<p class="subtitle emoji">🔬 Research & Projects</p>', unsafe_allow_html=True)
st.write(""" 
- **Trustworthy AI Framework** – Developed a framework for evaluating AI models based on **fairness, robustness, and transparency**.  
- **Security Testing in Generative AI** – Analyzed **GPT-like models for prompt injection and adversarial manipulation**.  
- **AI Explainability** – Worked on **XAI techniques to make neural networks interpretable** for decision-making in healthcare.  
""")

# --- FOOTER ---
#st.write("---")
st.markdown('<p class="footer">© 2025 Valentino Merlino | AI Red Teamer </p>', unsafe_allow_html=True)
#st.markdown('</div>', unsafe_allow_html=True)
