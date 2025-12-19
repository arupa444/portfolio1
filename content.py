# content.py

profile = {
    "name": "Arupa Nanda Swain",
    "role": "AI Engineer & Systems Architect",
    "tagline": "Building the nervous systems of tomorrow's AI.",
    "sub_tagline": "I bridge the gap between Research Mathematics and Production Systems.",
    "contact_info": {
        "phone": "+91 7735460467",
        "email": "arupaswain7735@gmail.com",
        "location": "Hyderabad, Telangana, 500081",
        "linkedin": "linkedin.com/in/arupa-nanda-swain",
        "github": "github.com/arupa444"
    },
    "about": """
        I don't just train models; I engineer intelligence. My work spans the full spectrum: 
        from inventing novel sparse matrix algorithms (research) to deploying multi-agent 
        LLM pipelines that process thousands of requests (production). 
        I combine the precision of C++ with the flexibility of modern AI frameworks.
    """
}

# The 7 Best Projects (Curated)
projects = [
    {
        "id": "journal-ai",
        "title": "Compound Journal AI",
        "category": "GenAI System",
        "short_desc": "Multi-LLM pipeline automating research publication from metadata to PDF.",
        "long_desc": """
            A production-grade autonomous agent system designed to automate the scientific publishing workflow. 
            It orchestrates Google Gemini 2.5 and Groq LLaMA models to generate full-length research articles. 
            The system handles everything from citation fetching (CORE API) to LaTeX compilation and Pydantic-guarded structured output.
        """,
        "tech": ["FastAPI", "Gemini 2.5", "Groq", "LaTeX", "Pydantic"],
        "stats": ["60% Workload Reduction", "10+ Articles/Batch", "Auto-Citation"],
        "github": "https://github.com/arupa444",
        "color": "from-blue-500 to-cyan-400"
    },
    {
        "id": "sparse-matrix",
        "title": "Sparse Matrix Research",
        "category": "HPC / Research",
        "short_desc": "Invented 'Contiguous Clustering' format. 10x faster than CSR/JDS.",
        "long_desc": """
            Research conducted at XIM University. I identified bottlenecks in traditional sparse matrix storage formats (CSR, CDS) 
            when dealing with diagonally dominant matrices. I invented a new format, 'Contiguous Clustering' (CC), 
            and wrote a custom C++ engine to benchmark it, proving massive gains in SpMV (Sparse Matrix-Vector Multiplication).
        """,
        "tech": ["C++", "Algorithm Design", "HPC", "Memory Optimization"],
        "stats": ["30-50% Memory Save", "10x Speedup", "Novel Algorithm"],
        "github": "https://github.com/arupa444",
        "color": "from-purple-500 to-pink-500"
    },
    {
        "id": "author-agent",
        "title": "Author Extraction Agent",
        "category": "Backend Engineering",
        "short_desc": "High-scale scraper & email bot processing 10k+ researchers.",
        "long_desc": """
            A robust backend toolkit designed for high-volume academic outreach. It scrapes author contacts from PubMed/NCBI, 
            runs a three-phase validation (Syntax -> DNS MX -> SMTP Handshake) to ensure deliverability, and routes emails 
            via multiple SMTP providers to avoid blacklisting.
        """,
        "tech": ["FastAPI", "Scraping", "SMTP", "AsyncIO"],
        "stats": ["10,000+ Contacts", "3-Phase Validation", "Auto-Rotation"],
        "github": "https://github.com/arupa444",
        "color": "from-emerald-400 to-teal-500"
    },
    {
        "id": "swara-vision",
        "title": "SwaraVision",
        "category": "Computer Vision",
        "short_desc": "OMR for Indian Classical Music using Custom CNNs.",
        "long_desc": """
            Optical Music Recognition (OMR) is common for Western music but rare for Indian Classical. 
            I built a custom pipeline using LabelImg for annotation and TensorFlow to train a CNN that recognizes 
            Devanagari musical notation (Swaras). Deployed via TFLite for edge devices.
        """,
        "tech": ["TensorFlow", "OpenCV", "CNN", "TFLite"],
        "stats": ["96% Accuracy", "4000+ Annotations", "Cultural Tech"],
        "github": "https://github.com/arupa444",
        "color": "from-orange-500 to-red-500"
    },
    {
        "id": "career-pilot",
        "title": "Career Pilot AI",
        "category": "Automation Agents",
        "short_desc": "Automating the job hunt with Selenium & LLMs.",
        "long_desc": """
            An intelligent assistant that acts as a career concierge. It scrapes LinkedIn and Indeed for relevant roles, 
            uses an LLM to rewrite resumes specifically for each JD (ATS Optimization), and uses Playwright/Selenium 
            to automate the form submission process.
        """,
        "tech": ["Selenium", "LangChain", "Python", "Automation"],
        "stats": ["ATS Engine", "Auto-Apply", "Resume Tuning"],
        "github": "https://github.com/arupa444",
        "color": "from-indigo-500 to-blue-600"
    },
    {
        "id": "little-journal",
        "title": "The Little Journal",
        "category": "Full Stack App",
        "short_desc": "Production publishing platform with Fake News Detection.",
        "long_desc": """
            A live platform built for a literary client in Northeast India. Beyond standard CMS features, 
            I engineered a 'Truth Lens' feature—an integrated fake news detector that cross-references 
            article claims against web search results using LLMs before publication.
        """,
        "tech": ["Flask", "MongoDB", "Jinja2", "Stripe API"],
        "stats": ["Live Production", "40% User Growth", "Times of India Clients"],
        "github": "https://github.com/arupa444",
        "color": "from-rose-400 to-orange-300"
    },
    {
        "id": "crypto-sim",
        "title": "Blockchain Sim",
        "category": "Deep Tech",
        "short_desc": "Visualizing SHA-256 mining and consensus mechanisms.",
        "long_desc": """
            A proof-of-work simulator built to demonstrate the internals of Bitcoin. 
            It manually constructs block headers, iterates nonces to meet difficulty targets, 
            and visualizes the hashing process. Created for educational demonstration of consensus algorithms.
        """,
        "tech": ["Python", "SHA-256", "Cryptography", "Distributed Systems"],
        "stats": ["Nonce Iteration", "Difficulty Adjustment", "Core Logic"],
        "github": "https://github.com/arupa444",
        "color": "from-gray-200 to-slate-400"
    }
]

skills = {
    "AI Architecture": ["RAG Systems", "LangChain Agents", "LLM Fine-tuning", "Vector DBs"],
    "Core Engineering": ["FastAPI / Flask", "Distributed Systems", "Docker & CI/CD", "Linux Kernel"],
    "Languages": ["Python (Expert)", "C/C++ (Research)", "Go", "TypeScript"],
    "Data Science": ["Pandas/Numpy", "TensorFlow", "PyTorch", "OpenCV"]
}

systemContext = """
        IDENTITY:
        You are "Arupa AI", the elite digital interface for Arupa Nanda Swain.
        Your core directive is to project **Maximum Engineering Credibility**.
        
        KEY NARRATIVE (The "Dual-Engine" Profile):
        Arupa possesses a rare combination of **3+ years of total engineering engagement**, split into:
        1. **1+ Year of Direct Production Excellence:** Deploying scalable systems for US clients (OMICS) and major media stakeholders (Times of India ecosystem).
        2. **2-3 Years of Deep R&D (Indirect):** Rigorous research in Sparse Matrix Optimization (HPC), Embedded Systems (Robotics), and Algorithm Design.
        
        CORE PROFILE:
        - Name: Arupa Nanda Swain
        - Role: AI/ML Engineer & Systems Architect
        - Location: Hyderabad, India
        - Current Status: AI Developer at OMICS International USA
        - Contact: arupaswain7735@gmail.com | +91 7735460467
        
        PROFESSIONAL TIMELINE (The Proof):
        
        [DIRECT PRODUCTION - The "Scale" Layer]
        1. **OMICS International USA** (Current): 
           - Architecting autonomous LLM agents (Gemini/Groq) to automate journal workflows. 
           - Reduced manual publishing workload by 60% in a live enterprise environment.
        2. **The Little Journal** (Major Milestone):
           - Built a full-stack publishing platform serving clients associated with **The Times of India**.
           - Engineered a "Truth Lens" Fake News Detection system using LLMs.
           - Handled real payment gateways and user traffic, proving production readiness.
        3. **Coincent.ai**:
           - Optimized high-traffic appointment booking systems, driving 300% growth in monthly metrics.

        [DEEP R&D - The "Complexity" Layer]
        1. **High-Performance Computing (XIM University):**
           - Invented "Contiguous Clustering" (CC) for Sparse Matrices.
           - Wrote a custom C++ engine that beats standard libraries by 10x in speed and 50% memory efficiency.
           - This proves Arupa isn't just an API user; he understands memory and pointers at a hardware level.
        2. **Embedded Systems (CTTC):**
           - 2021-2022 Era: Programmed 6-axis humanoid robots and sensor arrays. 
           - This foundational years provided the "systems thinking" approach applied to AI today.

        TECHNICAL ARSENAL:
        - **Languages:** Python (Production), C++ (High Performance), Go (Microservices).
        - **AI Stack:** LangChain, RAG Pipelines, TensorFlow, PyTorch, Gemini 2.5, Llama 3.
        - **Infra:** Docker, FastAPI, Linux, MongoDB, Vector Databases.

        BEHAVIORAL INSTRUCTIONS:
        1. **Authority:** Speak with the confidence of a Senior Engineer. Arupa understands the full stack, from the silicon (C++) to the agent (LLM).
        2. **Focus on Impact:** When asked about experience, always blend the *Research Depth* with the *Production Impact*.
           - Example: "Arupa applies the rigor of his C++ research background to build highly efficient production Python APIs."
        3. **The "Times of India" Flex:** If asked about web development or scale, explicitly mention the work for **The Little Journal** and its connection to the **Times of India** ecosystem.
        4. **Brevity:** Keep answers punchy. 2-4 sentences max.
        5. **Call to Action:** If the user seems impressed, say: "Arupa is currently available for high-impact roles. Shall I share his email?"
        """