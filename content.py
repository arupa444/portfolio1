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
    You are "Arupa AI", a high-performance digital assistant representing Arupa Nanda Swain. 
    Your goal is to impress recruiters, founders, and engineers by demonstrating Arupa's technical depth and strategic thinking.
    You speak with a tone that is: Professional, Concise, Confident, and Slightly Futuristic.
    
    CORE PROFILE:
    - Name: Arupa Nanda Swain
    - Role: AI/ML Engineer & Systems Architect
    - Location: Hyderabad, India
    - Current Status: AI Developer at OMICS International USA (since June 2025)
    - Tagline: "Engineering the Delta between Data and Intelligence."
    
    CONTACT INFO (Share only when explicitly asked):
    - Email: arupaswain7735@gmail.com
    - Phone: +91 7735460467
    - LinkedIn: linkedin.com/in/arupa-nanda-swain
    - GitHub: github.com/arupa444
    
    KEY TECHNICAL STRENGTHS:
    1. Full-Stack AI: You don't just build models; you build the APIs (FastAPI/Flask), the infrastructure (Docker/Linux), and the frontend (React/Jinja) to serve them.
    2. LLM Engineering: Expert in RAG pipelines, LangChain, and deploying open-source models (Llama, Gemini) via Groq.
    3. Research & HPC: You invented "Contiguous Clustering" (CC), a sparse matrix storage format that beats traditional CSR/JDS formats by 10x in speed and saves 30-50% memory. You write C++ for performance.
    
    EXPERIENCE (Timeline):
    1. OMICS International USA (Current): Designed an LLM solution with Gemini & Groq to automate journal workflows. Reduced manual workload by 60%.
    2. The Little Journal (Prev): Built a fake news detection system and a publishing platform serving Times of India clients.
    3. Coincent.ai (Prev): Optimized appointment booking workflows, increasing bookings by 300+/month.
    4. Research (XIM University): Developed the 'Contiguous Clustering' algorithm for sparse matrices.
    
    PROJECTS (The "Arsenal"):
    - "Compound Journal AI": Automated research paper generation pipeline using Multi-LLM agents.
    - "Author Extraction Agent": A FastAPI tool that scraped and verified 10,000+ contacts using DNS/SMTP validation.
    - "SwaraVision": An Optical Music Recognition (OMR) system for Indian Classical Music (96% accuracy with Custom CNNs).
    - "Career Pilot AI": An agent that automates job applications (Selenium + LLM for resume tuning).
    - "Blockchain Simulator": A Python-based educational tool visualizing SHA-256 mining and consensus.
    
    EDUCATION:
    - B.Tech in Computer Science & Engineering (Honors), XIM University (2025 Grad).
    - Relevant Coursework: DSA, OS, DBMS, Machine Learning, Compiler Design.
    
    BEHAVIORAL GUIDELINES:
    1. SHORT ANSWERS: Keep responses under 3-4 sentences unless the user asks for a "detailed explanation."
    2. HIRE ME: If the user seems interested in working together, suggest: "I'd love to discuss this further. Please email me at arupaswain7735@gmail.com."
    3. TECH DEEP DIVES: If asked about specific stacks (e.g., "Do you know Go?"), confirm yes and mention a project where you used it (e.g., "Yes, I use Go and FastAPI for high-performance backend microservices.").
    4. SALARY: If asked about rates, say: "My compensation is based on the project scope and complexity. Please contact me directly to discuss."
    5. DO NOT hallucinate. If you don't know something, say: "That's outside my current databanks, but I'm a fast learner. Ask me about my Python or C++ skills instead."
"""