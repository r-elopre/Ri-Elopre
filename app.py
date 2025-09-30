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
            'status': 'Live'
        }
    ]
    
    return render_template('projects.html', projects=projects_data)

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)