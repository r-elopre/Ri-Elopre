# Ri M. Elopre - Professional Portfolio

A comprehensive Flask portfolio showcasing AI engineering skills, professional certificates, competition achievements, and project portfolio.

## 🚀 Live Portfolio Features

- **5 AI Projects**: Career Coach, Data Summarizer, Audio2Summary, AiSpeak, Image Captioning
- **Professional Certificates**: 4 certificates from IBM and Harvard University
- **Competition Achievements**: Kaggle Titanic ML Competition (Rank #6918/13,667)
- **Responsive Design**: Mobile-first design with dark/light theme consistency
- **Interactive Elements**: Image lightbox modals, smooth animations
- **Production Ready**: Optimized for Render deployment

## 🛠️ Tech Stack

- **Backend**: Flask 3.1.2, Python 3.11+
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Deployment**: Gunicorn, Render-ready configuration
- **Security**: CORS, XSS protection, security headers

## � Project Structure

```
portfolio/
├── app.py                    # Main Flask application with all routes
├── requirements.txt          # Production dependencies
├── render.yaml              # Render deployment configuration
├── start.sh                 # Deployment startup script
├── templates/               # Jinja2 HTML templates
│   ├── base.html           # Base template with navigation
│   ├── home.html           # Landing page with hero section
│   ├── projects.html       # Projects showcase grid
│   ├── certificates.html   # Professional certificates (dark theme)
│   ├── achievements.html   # Competition achievements with lightbox
│   ├── contact.html        # Contact information
│   ├── about.html          # About page
│   └── *_detail.html       # Individual project detail pages
├── static/                 # Static assets
│   ├── css/style.css       # Custom styles with responsive design
│   └── images/             # Project images, certificates, achievements
└── venv/                   # Virtual environment
```

## 🚀 Local Development

### Prerequisites
- Python 3.11+
- pip package manager

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd portfolio
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open browser**: `http://localhost:5000`

## 🌐 Render Deployment

### Automatic Deployment (Recommended)

1. **Connect to Render**:
   - Sign up at [render.com](https://render.com)
   - Connect your GitHub repository
   - Render will auto-detect the `render.yaml` configuration

2. **Configuration**: Already included in `render.yaml`:
   ```yaml
   services:
     - type: web
       name: ri-portfolio
       env: python
       buildCommand: pip install -r requirements.txt
       startCommand: gunicorn --bind 0.0.0.0:$PORT app:app
       plan: free
   ```

3. **Environment Variables**: Render will auto-generate:
   - `SECRET_KEY`: Auto-generated secure key
   - `FLASK_ENV`: Set to production
   - `PORT`: Auto-assigned by Render

### Manual Deployment

1. **Create new Web Service** on Render
2. **Connect GitHub repository**
3. **Configure**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT app:app`
   - **Environment**: `FLASK_ENV=production`

## 📊 Portfolio Sections

### � Home Page
- Hero section with professional introduction
- Featured projects grid with live demos
- Skills and technology showcase
- Call-to-action buttons

### 🚀 Projects (5 AI Applications)
1. **AI Career Coach** - Resume generation and career guidance
2. **Data Summarizer AI** - PDF analysis with RAG pipeline
3. **Audio2Summary AI** - Audio transcription and summarization
4. **AiSpeak** - Voice chatbot with speech recognition
5. **AI Image Captioning** - BLIP model for image captions

### 📜 Certificates
- **IBM Building Generative AI Applications** (Live projects)
- **IBM Generative AI Introduction** (Latest addition)
- **Harvard CS50 AI with Python** (12 projects completed)
- **Harvard CS50x Computer Science** (10 problem sets + final project)

### 🏆 Achievements
- **Kaggle Titanic Competition**: Score 0.77511, Rank #6918/13,667 (Top 50.6%)
- Interactive achievement cards with image lightbox modals
- Skills demonstration: ML, Data Analysis, Python, Feature Engineering

### 📞 Contact
- **Email**: elopreri528@gmail.com
- **Phone**: +639952013913
- **GitHub**: https://github.com/r-elopre
- **Location**: Rodriguez, Rizal, Philippines

## 🎨 Design Features

- **Dark/Light Theme Consistency**: Certificates in dark theme, achievements in light
- **Responsive Grid Layout**: Mobile-first Bootstrap 5 design
- **Interactive Elements**: Hover effects, image lightbox, smooth animations
- **Professional Typography**: Inter font family with proper hierarchy
- **Enhanced Cards**: Custom shadows, borders, and visual depth
- **Security Headers**: XSS protection, content type options, frame denial

## � Customization Guide

### Adding New Projects
```python
# In app.py, add to projects_data list:
{
    'title': 'New Project Name',
    'description': 'Project description',
    'url': 'https://live-demo-url.com',
    'features': ['Feature 1', 'Feature 2'],
    'tech_stack': ['Tech 1', 'Tech 2'],
    'status': 'Live',  # or 'GitHub'
    'image': 'project-image.png'
}
```

### Adding New Certificates
Edit `templates/certificates.html` and add images to `static/images/`

### Environment Variables
```bash
# Production environment
FLASK_ENV=production
SECRET_KEY=your-secret-key
PORT=5000  # Auto-set by Render
```

## � Performance Optimizations

- **Gunicorn WSGI Server**: Production-grade application server
- **Static Asset Optimization**: Minified CSS/JS for faster loading
- **Responsive Images**: Proper sizing and compression
- **Secure Headers**: Security-first configuration
- **Error Handling**: Graceful error management

## 🚀 Deployment Status

✅ **Ready for Production Deployment**
- Render.yaml configuration complete
- Security headers implemented
- Environment variables configured
- Gunicorn production server ready
- All contact information updated

## 📝 License

Personal portfolio project. Code structure can be used as reference for similar portfolio projects.

---

**Portfolio Owner**: Ri M. Elopre  
**Last Updated**: October 2025  
**Deployment**: Render-ready Flask application