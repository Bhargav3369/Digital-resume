"""
Database initialization script with Bhargav's resume data.
"""
from datetime import date
from api.database import engine, Base, SessionLocal
from api.models import Profile, Research, Education, Skill, Project


def init_db():
    """Initialize database with tables and sample data."""
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(Profile).first():
            print("Database already initialized. Skipping...")
            return
        
        # Create Profile
        profile = Profile(
            full_name="Madala Venkata Bhargav",
            title="AI/ML Engineer | Undergraduate",
            bio="AI/ML Engineer (Undergraduate) pursuing a B.Tech in Artificial Intelligence at Mahindra University with a strong foundation in machine learning, deep learning, reinforcement learning, and Generative AI systems. Experienced in building end-to-end ML pipelines and research-driven systems across NLP, computer vision, and human-in-the-loop learning. Actively seeking opportunities to apply research and engineering skills to real-world AI problems.",
            email="bhargavmadala2358@gmail.com",
            linkedin_url="https://www.linkedin.com/in/bhargav-madala",
            github_url="https://github.com/Bhargav3369",
            location="Hyderabad, Telangana, India"
        )
        db.add(profile)
        
        # Create Research
        research = Research(
            title="Learning Robotic Arm Control with Minimal Human Feedback",
            description="Designed a human-in-the-loop reinforcement learning pipeline for robotic arm control. Implemented a CACLA-based Actor-Critic model for continuous action spaces. Applied selective human feedback and reward shaping to improve learning stability under sparse supervision.",
            start_date=date(2025, 10, 1),
            end_date=None,  # Ongoing
            institution="Mahindra University",
            status="Ongoing",
            publication_url="/reports/robotic-arm-control.pdf"
        )
        db.add(research)
        
        # Create Education entries
        education_data = [
            {
                "degree": "B.Tech in Artificial Intelligence",
                "institution": "Mahindra University",
                "location": "Hyderabad, India",
                "start_date": date(2022, 7, 1),
                "end_date": date(2026, 5, 31),
                "gpa": 7.5,
                "description": "Undergraduate degree in Artificial Intelligence"
            },
            {
                "degree": "MPC (11th-12th)",
                "institution": "Deeksha College",
                "location": "Hyderabad, India",
                "start_date": date(2020, 6, 1),
                "end_date": date(2022, 5, 31),
                "gpa": 97.2,
                "description": "Mathematics, Physics, Chemistry"
            },
            {
                "degree": "Class 10",
                "institution": "Maharishi Vidya Mandir",
                "location": "Hyderabad, India",
                "start_date": date(2019, 6, 1),
                "end_date": date(2020, 5, 31),
                "gpa": 86.0,
                "description": "Secondary Education"
            }
        ]
        
        for edu in education_data:
            education = Education(**edu)
            db.add(education)
        
        # Create Skills
        skills_data = [
            # Programming Languages
            {"name": "Python", "category": "Programming Languages", "proficiency": "Advanced", "order": 1},
            {"name": "Java", "category": "Programming Languages", "proficiency": "Intermediate", "order": 2},
            {"name": "C", "category": "Programming Languages", "proficiency": "Intermediate", "order": 3},
            {"name": "SQL", "category": "Programming Languages", "proficiency": "Intermediate", "order": 4},
            {"name": "JavaScript", "category": "Programming Languages", "proficiency": "Intermediate", "order": 5},
            
            # Frameworks & Libraries
            {"name": "PyTorch", "category": "Frameworks & Libraries", "proficiency": "Advanced", "order": 1},
            {"name": "TensorFlow", "category": "Frameworks & Libraries", "proficiency": "Advanced", "order": 2},
            {"name": "Scikit-learn", "category": "Frameworks & Libraries", "proficiency": "Advanced", "order": 3},
            {"name": "Spring Boot", "category": "Frameworks & Libraries", "proficiency": "Intermediate", "order": 4},
            {"name": "React.js", "category": "Frameworks & Libraries", "proficiency": "Intermediate", "order": 5},
            
            # Machine Learning & AI
            {"name": "Supervised Learning", "category": "Machine Learning & AI", "proficiency": "Advanced", "order": 1},
            {"name": "Unsupervised Learning", "category": "Machine Learning & AI", "proficiency": "Advanced", "order": 2},
            {"name": "Deep Learning", "category": "Machine Learning & AI", "proficiency": "Advanced", "order": 3},
            {"name": "Reinforcement Learning", "category": "Machine Learning & AI", "proficiency": "Advanced", "order": 4},
            {"name": "Large Language Models", "category": "Machine Learning & AI", "proficiency": "Advanced", "order": 5},
            {"name": "Natural Language Processing", "category": "Machine Learning & AI", "proficiency": "Advanced", "order": 6},
            {"name": "Sentence Similarity", "category": "Machine Learning & AI", "proficiency": "Advanced", "order": 7},
            {"name": "Information Extraction", "category": "Machine Learning & AI", "proficiency": "Advanced", "order": 8},
            {"name": "Text Summarization", "category": "Machine Learning & AI", "proficiency": "Advanced", "order": 9},
            {"name": "Embeddings", "category": "Machine Learning & AI", "proficiency": "Advanced", "order": 10},
            {"name": "AI Agents", "category": "Machine Learning & AI", "proficiency": "Advanced", "order": 11},
            
            # Computer Vision
            {"name": "Convolutional Neural Networks", "category": "Computer Vision", "proficiency": "Advanced", "order": 1},
            {"name": "U-Net", "category": "Computer Vision", "proficiency": "Advanced", "order": 2},
            {"name": "Attention Mechanisms", "category": "Computer Vision", "proficiency": "Advanced", "order": 3},
            {"name": "Image Colorization", "category": "Computer Vision", "proficiency": "Advanced", "order": 4},
            
            # Tools & Systems
            {"name": "Git", "category": "Tools & Systems", "proficiency": "Advanced", "order": 1},
            {"name": "REST APIs", "category": "Tools & Systems", "proficiency": "Advanced", "order": 2},
            {"name": "OpenAI API", "category": "Tools & Systems", "proficiency": "Advanced", "order": 3},
            {"name": "Gemini API", "category": "Tools & Systems", "proficiency": "Advanced", "order": 4},
            {"name": "Mistral API", "category": "Tools & Systems", "proficiency": "Intermediate", "order": 5},
            {"name": "Operating Systems", "category": "Tools & Systems", "proficiency": "Intermediate", "order": 6},
            {"name": "Databases", "category": "Tools & Systems", "proficiency": "Intermediate", "order": 7},
            {"name": "Computer Networks", "category": "Tools & Systems", "proficiency": "Intermediate", "order": 8},
            {"name": "Object-Oriented Programming", "category": "Tools & Systems", "proficiency": "Advanced", "order": 9},
        ]
        
        for skill in skills_data:
            db.add(Skill(**skill))
        
        # Create Projects
        projects_data = [
            {
                "title": "MU-CONNECT",
                "description": "Developed a university-based social media platform to improve communication among students, faculty, and clubs. Implemented authentication, user profiles, post sharing, and event management modules. Followed software engineering practices including requirement analysis, UML-based design, and system testing.",
                "tech_stack": "React.js, Spring Boot, PostgreSQL, REST APIs",
                "github_url": "https://github.com/Anunay6827/MU-Connect",
                "start_date": date(2024, 11, 1),
                "end_date": date(2024, 12, 31),
                "featured": True
            },
            {
                "title": "Banking System",
                "description": "Developed an OOP-based banking system using Spring Boot. Supported account creation, transactions, and fund transfers. Emphasized modular design and scalability.",
                "tech_stack": "Spring Boot, Java, REST APIs, Object-Oriented Design",
                "github_url": "https://github.com/chaturvarma/BankingSystem",
                "start_date": date(2024, 6, 1),
                "end_date": date(2024, 6, 30),
                "featured": False
            },
            {
                "title": "CMDCRAFT",
                "description": "Built a Generative AI-powered command-line assistant to convert natural language instructions into executable system commands. Designed prompt templates and validation logic for secure command execution. Integrated OpenAI and Gemini APIs with contextual follow-up handling.",
                "tech_stack": "Python, OpenAI API, Gemini API, Natural Language Processing",
                "github_url": "https://github.com/Anunay6827/unihack-pre-hack",
                "start_date": date(2025, 8, 1),
                "end_date": date(2025, 8, 31),
                "featured": True
            },
            {
                "title": "Automated Interview System",
                "description": "Built an NLP-driven interview system with dynamic follow-up question generation. Used embedding-based sentence similarity for candidate evaluation and scoring. Automated concise interview summarization for recruiters.",
                "tech_stack": "Python, NLP, Embeddings, Sentence Similarity, Text Summarization",
                "github_url": "https://github.com/Anunay6827/Automated-Interview-System",
                "featured": True
            },
            {
                "title": "Image Colorization using Deep Learning",
                "description": "Developed a U-Net-based image colorization model with attention mechanisms. Used perceptual loss with VGG16 and LAB color space preprocessing for improved visual quality.",
                "tech_stack": "PyTorch, U-Net, Attention Mechanisms, Computer Vision, VGG16",
                "github_url": "https://github.com/Bhargav3369/Image_Colorization",
                "featured": True
            }
        ]
        
        for proj in projects_data:
            db.add(Project(**proj))
        
        db.commit()
        print("✅ Database initialized successfully with Bhargav's resume data!")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error initializing database: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("Initializing database...")
    init_db()
