from flask import Flask, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

@app.route('/')
def home():
    """Landing page with personal information and summary"""
    personal_info = {
        'name': 'Ri M. Elopre',
        'title': 'Aspiring AI Engineer | Full-Stack Developer (Django)',
        'location': 'Rodriguez, Rizal',
        'phone': '+639952013913',
        'email': 'your-email@example.com',  # You can update this later
        'github': 'https://github.com/your-username',  # You can update this later
        'summary': """Versatile and results-oriented professional with strong exposure to Full-Stack Development and AI Engineering. All my projects are meticulously documented to cater to different types of viewers:

For those who want in-depth technical details — each repository contains a comprehensive README outlining architecture, methodology, and implementation steps.

For those who prefer a high-level, visually engaging overview — I've prepared professional PowerPoint presentations, featured at the top of each README, summarizing the project's purpose, workflow, and results in a concise, compelling format.

Whether you're here for the deep technical dive or a quick, insightful snapshot, my project documentation is designed to deliver both clarity and impact."""
    }
    
    return render_template('home.html', info=personal_info)

@app.route('/projects')
def projects():
    """Projects showcase page"""
    projects_data = [
        {
            'title': 'AI Career Coach',
            'description': 'Comprehensive career development platform with AI-powered resume generation, polishing, and career guidance.',
            'url': 'https://ri-career-coach-ai.onrender.com/advisor',
            'features': [
                'Full Resume Generator with ATS-friendly output',
                'Resume Polisher with quantified impact statements',
                'Cover Letter Generator tailored to job descriptions', 
                'Career Advisor with actionable guidance'
            ],
            'tech_stack': ['Python', 'AI/ML', 'Web Development'],
            'status': 'Live',
            'image': 'resume.png'
        },
        {
            'title': 'Data Summarizer AI',
            'description': 'AI-powered PDF analysis tool that enables users to upload documents and ask intelligent questions about their content.',
            'url': 'https://ri-data-summarizer-ai.onrender.com/',
            'features': [
                'PDF Upload & Processing with 16MB limit',
                'RAG Pipeline with LangChain integration',
                'Conversational AI with context retention',
                'Source citations with page references'
            ],
            'tech_stack': ['Flask', 'LangChain', 'OpenAI GPT-3.5', 'FAISS', 'PyPDF'],
            'status': 'Live',
            'image': 'data.jpg'
        },
        {
            'title': 'Audio2Summary AI',
            'description': 'Professional Flask web application that transforms audio files into intelligent summaries using OpenAI\'s Whisper and GPT-3.5 Turbo APIs.',
            'url': 'https://ri-audio2summary-ai.onrender.com/',
            'features': [
                'Audio transcription with OpenAI Whisper',
                'Intelligent summarization with GPT-3.5 Turbo',
                'Multi-stage processing pipeline',
                'Export and copy functionality'
            ],
            'tech_stack': ['Flask', 'OpenAI Whisper', 'OpenAI GPT-3.5', 'Audio Processing'],
            'status': 'Live',
            'image': 'audio.png'
        },
        {
            'title': 'AiSpeak',
            'description': 'Production-ready AI-powered voice chatbot that enables natural conversations through both text and voice input, featuring enterprise-level security and modern web technologies.',
            'url': 'https://aispeak-ri.onrender.com/',
            'features': [
                'Voice-to-text conversation with Web Speech API',
                'Text-to-speech response generation',
                'Real-time chat with OpenAI GPT-3.5-turbo',
                'Enterprise-level security with rate limiting'
            ],
            'tech_stack': ['Flask 3.1.0', 'OpenAI GPT-3.5', 'Web Speech API', 'Gunicorn'],
            'status': 'Live',
            'image': 'aispeak.mp4'
        }
    ]
    
    return render_template('projects.html', projects=projects_data)

@app.route('/projects/data-summarizer')
def data_summarizer_detail():
    """Detailed page for Data Summarizer AI project"""
    project = {
        'title': 'Data Summarizer AI',
        'description': 'AI-powered PDF analysis tool that enables users to upload documents and ask intelligent questions about their content using advanced RAG (Retrieval-Augmented Generation) pipeline.',
        'image': 'data.jpg',
        'user_flow': {
            'Step 1: Initial Access': {
                'description': 'Clean chat interface with upload functionality',
                'features': [
                    'User opens the web application',
                    'Sees a clean chat interface with upload area',
                    'Receives welcome message: "Hi! Upload a PDF and ask me anything about it."'
                ]
            },
            'Step 2: PDF Upload Process': {
                'description': 'Advanced PDF processing with AI pipeline',
                'features': [
                    'User clicks upload area or drags & drops PDF file',
                    'Frontend validates file type (PDF only) and size (16MB limit)',
                    'PyPDF Loader extracts raw text',
                    'Text Splitter chunks content (1000 chars, 200 overlap)',
                    'OpenAI Embeddings converts chunks to vectors',
                    'FAISS Vector Store indexes embeddings for retrieval'
                ]
            },
            'Step 3: Question & Answer Cycle': {
                'description': 'Intelligent RAG pipeline for contextual answers',
                'features': [
                    'User types question in chat input',
                    'Similarity Search finds 4 most relevant chunks',
                    'ConversationalRetrievalChain combines question + context',
                    'GPT-3.5-turbo generates contextual answer',
                    'Source tracking identifies which PDF sections were used'
                ]
            },
            'Step 4: Conversational Continuity': {
                'description': 'Memory-enabled conversation system',
                'features': [
                    'System maintains conversation memory via ConversationBufferMemory',
                    'Users can ask follow-up questions with full context retention',
                    'Each response includes source citations showing PDF page/chunk references'
                ]
            },
            'Step 5: Session Management': {
                'description': 'Secure and isolated session handling',
                'features': [
                    'All data stored in memory (no permanent storage)',
                    'Session-based isolation (multiple users don\'t interfere)',
                    'Clean session termination discards all PDF data'
                ]
            }
        },
        'tech_stack': {
            'Backend': ['Flask', 'Python'],
            'AI/ML': ['LangChain', 'OpenAI GPT-3.5-turbo', 'OpenAI Embeddings', 'FAISS'],
            'Processing': ['PyPDF', 'Text Splitter'],
            'Management': ['Flask Sessions', 'python-dotenv']
        }
    }
    
    return render_template('data_summarizer_detail.html', project=project)

@app.route('/projects/career-coach')
def career_coach_detail():
    """Detailed page for AI Career Coach project"""
    project = {
        'title': 'AI Career Coach',
        'url': 'https://ri-career-coach-ai.onrender.com/advisor',
        'description': 'A comprehensive AI-powered career development platform that helps users create, polish, and optimize their professional documents.',
        'user_flow': {
            'Landing Page (/)': {
                'description': 'Full Resume Generator with comprehensive form fields',
                'features': [
                    'Name, Role, Contact Info (required)',
                    'Experience, Skills, Education (required)', 
                    'Summary, Certifications, Projects/Links (optional)',
                    'AI generates complete, ATS-friendly resume',
                    'Copy generated text or Download as PDF'
                ]
            },
            'Resume Polisher (/polish)': {
                'description': 'Improve existing resume content with AI analysis',
                'features': [
                    'Position name (target role)',
                    'Resume section/content to improve',
                    'Polish instructions (specific guidance)',
                    'Quantified impact statements',
                    'Role-specific keywords',
                    'Professional tone enhancement'
                ]
            },
            'Cover Letter Generator (/cover-letter)': {
                'description': 'Create tailored cover letters for specific positions',
                'features': [
                    'Company name and position targeting',
                    'Job description analysis',
                    'Resume content integration',
                    'Tailored 250-400 word cover letters',
                    'Company-specific language matching'
                ]
            },
            'Career Advisor (/advisor)': {
                'description': 'Get personalized career guidance and development recommendations',
                'features': [
                    'Target position analysis',
                    'Job description gap analysis',
                    'Skills development roadmap (30-60 day focus)',
                    'Resume improvement suggestions',
                    'Project ideas for skill building'
                ]
            }
        }
    }
    
    return render_template('career_coach_detail.html', project=project)

@app.route('/about')
def about():
    """About page with more detailed information"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')

@app.route('/projects/audio2summary')
def audio2summary_detail():
    """Detailed page for Audio2Summary AI project"""
    project = {
        'title': 'Audio2Summary AI',
        'description': 'Professional Flask web application that transforms audio files into intelligent summaries using OpenAI\'s Whisper (transcription) and GPT-3.5 Turbo (summarization) APIs.',
        'image': 'audio.png',
        'user_flow': {
            'Phase 1: Initial Interaction': {
                'Landing': 'User sees professional header with Audio2Summary AI branding',
                'Call-to-Action': 'Clear upload section with drag-and-drop zone',
                'Requirements': 'Visible constraints (2 min max, audio formats, 25MB limit)'
            },
            'Phase 2: File Selection': {
                'Multiple Options': 'Drag-and-drop OR click to browse',
                'Real-time Validation': 'File type and size checking',
                'Visual Feedback': 'File info display with name, size, remove option',
                'State Management': 'Upload button enabled only when valid file selected'
            },
            'Phase 3: Processing Experience': {
                'Animated UI': 'Spinner + audio wave visualization',
                'Progress Tracking': '7-stage progress bar with descriptive text',
                'Real-time Updates': 'Status messages for each processing stage',
                'Estimated Timing': 'Smart delays based on actual API processing times'
            },
            'Phase 4: Results Consumption': {
                'Structured Output': 'Transcript, Summary, Action Items sections',
                'Metadata Display': 'Duration, word count, timestamp',
                'Copy Functions': 'Individual section copying to clipboard',
                'Export Options': 'Download complete text report',
                'Next Actions': 'Process another file OR try again'
            },
            'Phase 5: Error Handling': {
                'Graceful Failures': 'User-friendly error messages',
                'Recovery Options': 'Try Again button',
                'State Reset': 'Clean return to upload state'
            }
        },
        'tech_details': {
            'OpenAI Whisper': 'Audio → Text transcription',
            'GPT-3.5 Turbo': 'Text → Intelligent summaries',
            'API Management': 'Timeout handling, retry logic',
            'Error Handling': 'Rate limiting, quota management'
        },
        'features': [
            'Audio transcription with OpenAI Whisper',
            'Intelligent summarization with GPT-3.5 Turbo',
            'Multi-stage processing pipeline',
            'Export and copy functionality'
        ],
        'tech_stack': ['Flask', 'OpenAI Whisper', 'OpenAI GPT-3.5', 'Audio Processing'],
        'live_url': 'https://ri-audio2summary-ai.onrender.com/'
    }
    return render_template('audio2summary_detail.html', project=project)

@app.route('/projects/aispeak')
def aispeak_detail():
    """Detailed page for AiSpeak project"""
    project = {
        'title': 'AiSpeak',
        'description': 'Production-ready AI-powered voice chatbot that enables natural conversations through both text and voice input, featuring enterprise-level security and modern web technologies.',
        'image': 'aispeak.mp4',
        'user_flow': {
            '1. Initial Page Load': {
                'Page Load': 'User visits URL → Flask serves index.html',
                'Asset Loading': 'CSS/JS assets load → Voice permissions requested',
                'Initialization': 'Web Speech API setup and ready state'
            },
            '2. Text Input Flow': {
                'Input Processing': 'User types message → Client-side validation → Sanitization',
                'Server Processing': 'Rate limit check → POST /chat → Server validation',
                'AI Response': 'OpenAI API → Response sanitization → Display + TTS'
            },
            '3. Voice Input Flow': {
                'Voice Activation': 'User clicks microphone → Web Speech API activates',
                'Speech Processing': 'Speech-to-text conversion → Auto-populate text field',
                'Response Flow': 'Follows text input flow for processing'
            },
            '4. Error Handling Flow': {
                'Rate Limiting': 'Rate limit exceeded → 429 response → User notification',
                'API Failures': 'API failure → 500 response → Error message',
                'Graceful Degradation': 'Retry timer displayed → Fallback options'
            }
        },
        'tech_details': {
            'Framework': 'Flask 3.1.0 (Python web framework)',
            'AI Engine': 'OpenAI GPT-3.5-turbo (API version 1.60.2)',
            'Environment': 'python-dotenv 1.0.0',
            'Production Server': 'Gunicorn 21.2.0 (WSGI server)',
            'Security': 'Custom XSS protection, CSRF, rate limiting',
            'Data Structures': 'Collections (deque, defaultdict) for rate limiting'
        },
        'features': [
            'Voice-to-text conversation with Web Speech API',
            'Text-to-speech response generation',
            'Real-time chat with OpenAI GPT-3.5-turbo',
            'Enterprise-level security with rate limiting'
        ],
        'tech_stack': ['Flask 3.1.0', 'OpenAI GPT-3.5', 'Web Speech API', 'Gunicorn'],
        'live_url': 'https://aispeak-ri.onrender.com/'
    }
    return render_template('aispeak_detail.html', project=project)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)