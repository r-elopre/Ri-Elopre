// Portfolio JavaScript Interactions

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initializeNavbar();
    initializeBottomNav();
    initializeAnimations();
    initializeTypingEffect();
    initializeSmoothScrolling();
    initializeLoadingStates();
    initializeContactForm();
});

// Navbar functionality
function initializeNavbar() {
    const navbar = document.querySelector('.navbar');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Add active class to current page nav link
    const currentPath = window.location.pathname;
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath || 
            (currentPath === '/' && link.getAttribute('href').includes('home'))) {
            link.classList.add('active');
        }
    });
    
    // Navbar scroll effect
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
}

// Bottom Navigation functionality
function initializeBottomNav() {
    const bottomNavItems = document.querySelectorAll('.bottom-nav-item');
    const currentPath = window.location.pathname;
    
    // Set active state for current page
    bottomNavItems.forEach(item => {
        const href = item.getAttribute('href');
        if (href === currentPath || (currentPath === '/' && href.includes('home'))) {
            item.classList.add('active');
        }
        
        // Add click animation
        item.addEventListener('click', function(e) {
            // Remove active from all items
            bottomNavItems.forEach(nav => nav.classList.remove('active'));
            // Add active to clicked item
            this.classList.add('active');
            
            // Add ripple effect
            createRippleEffect(this, e);
        });
        
        // Add touch feedback
        item.addEventListener('touchstart', function() {
            this.style.transform = 'scale(0.95)';
        });
        
        item.addEventListener('touchend', function() {
            this.style.transform = 'scale(1)';
        });
    });
}

// Create ripple effect for bottom nav
function createRippleEffect(element, event) {
    const ripple = document.createElement('span');
    const rect = element.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = event.clientX - rect.left - size / 2;
    const y = event.clientY - rect.top - size / 2;
    
    ripple.style.cssText = `
        position: absolute;
        border-radius: 50%;
        background: rgba(59, 130, 246, 0.3);
        transform: scale(0);
        animation: ripple 0.6s linear;
        width: ${size}px;
        height: ${size}px;
        left: ${x}px;
        top: ${y}px;
        pointer-events: none;
    `;
    
    // Add ripple animation keyframes if not exists
    if (!document.querySelector('#ripple-keyframes')) {
        const style = document.createElement('style');
        style.id = 'ripple-keyframes';
        style.textContent = `
            @keyframes ripple {
                to {
                    transform: scale(4);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    element.style.position = 'relative';
    element.style.overflow = 'hidden';
    element.appendChild(ripple);
    
    setTimeout(() => {
        ripple.remove();
    }, 600);
}

// Animation effects
function initializeAnimations() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animatedElements = document.querySelectorAll('.summary-card, .contact-card, .project-card, .tech-card, .flow-card');
    animatedElements.forEach(el => {
        observer.observe(el);
    });
    
    // Card hover effects
    const cards = document.querySelectorAll('.contact-card, .tech-card, .contact-method');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
}

// Typing effect for hero section
function initializeTypingEffect() {
    const typingElement = document.querySelector('.typing-text');
    if (!typingElement) return;
    
    const text = typingElement.textContent;
    typingElement.textContent = '';
    
    let i = 0;
    const typeWriter = () => {
        if (i < text.length) {
            typingElement.textContent += text.charAt(i);
            i++;
            setTimeout(typeWriter, 100);
        }
    };
    
    // Start typing effect after a short delay
    setTimeout(typeWriter, 500);
}

// Smooth scrolling for internal links
function initializeSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Loading states for buttons
function initializeLoadingStates() {
    const externalLinks = document.querySelectorAll('a[target="_blank"]');
    
    externalLinks.forEach(link => {
        link.addEventListener('click', function() {
            const originalText = this.innerHTML;
            this.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Opening...';
            this.classList.add('loading');
            
            // Reset after 2 seconds
            setTimeout(() => {
                this.innerHTML = originalText;
                this.classList.remove('loading');
            }, 2000);
        });
    });
}

// Contact form enhancements (if you add a form later)
function initializeContactForm() {
    const contactForms = document.querySelectorAll('form');
    
    contactForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Add your form submission logic here
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Sending...';
                submitBtn.disabled = true;
                
                // Simulate form submission
                setTimeout(() => {
                    submitBtn.innerHTML = '<i class="fas fa-check me-2"></i>Sent!';
                    setTimeout(() => {
                        submitBtn.innerHTML = originalText;
                        submitBtn.disabled = false;
                    }, 2000);
                }, 1500);
            }
        });
    });
}

// Utility functions
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 100px; right: 20px; z-index: 9999; min-width: 300px;';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        notification.remove();
    }, 5000);
}

// Copy to clipboard functionality (useful for contact info)
function copyToClipboard(text, element) {
    navigator.clipboard.writeText(text).then(() => {
        const originalText = element.innerHTML;
        element.innerHTML = '<i class="fas fa-check me-2"></i>Copied!';
        element.classList.add('btn-success');
        element.classList.remove('btn-primary');
        
        setTimeout(() => {
            element.innerHTML = originalText;
            element.classList.remove('btn-success');
            element.classList.add('btn-primary');
        }, 2000);
        
        showNotification('Copied to clipboard!', 'success');
    }).catch(() => {
        showNotification('Failed to copy to clipboard', 'warning');
    });
}

// Add copy functionality to phone and email links
document.addEventListener('DOMContentLoaded', function() {
    // Add copy buttons for contact info
    const phoneLinks = document.querySelectorAll('a[href^="tel:"]');
    const emailLinks = document.querySelectorAll('a[href^="mailto:"]');
    
    phoneLinks.forEach(link => {
        const copyBtn = document.createElement('button');
        copyBtn.className = 'btn btn-sm btn-outline-secondary ms-2';
        copyBtn.innerHTML = '<i class="fas fa-copy"></i>';
        copyBtn.onclick = (e) => {
            e.preventDefault();
            const phoneNumber = link.href.replace('tel:', '');
            copyToClipboard(phoneNumber, copyBtn);
        };
        link.parentNode.appendChild(copyBtn);
    });
    
    emailLinks.forEach(link => {
        const copyBtn = document.createElement('button');
        copyBtn.className = 'btn btn-sm btn-outline-secondary ms-2';
        copyBtn.innerHTML = '<i class="fas fa-copy"></i>';
        copyBtn.onclick = (e) => {
            e.preventDefault();
            const email = link.href.replace('mailto:', '');
            copyToClipboard(email, copyBtn);
        };
        link.parentNode.appendChild(copyBtn);
    });
});

// Performance optimization
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Optimized scroll handler
const optimizedScrollHandler = debounce(function() {
    // Add any scroll-based functionality here
}, 10);

window.addEventListener('scroll', optimizedScrollHandler);

// Add easter egg for developers
console.log(`
🚀 Welcome to Ri M. Elopre's Portfolio!
📧 Contact: +639952013913
💼 Aspiring AI Engineer | Full-Stack Developer
🔧 Built with Flask, HTML, CSS, and JavaScript

Interested in the code? Check out the GitHub repository!
`);

// Project showcase enhancements
function enhanceProjectCards() {
    const projectCards = document.querySelectorAll('.project-card');
    
    projectCards.forEach(card => {
        // Add click-to-expand functionality
        card.addEventListener('click', function(e) {
            if (!e.target.matches('a, button')) {
                this.classList.toggle('expanded');
            }
        });
        
        // Add keyboard navigation
        card.setAttribute('tabindex', '0');
        card.addEventListener('keypress', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                this.click();
            }
        });
    });
}

// Initialize project enhancements
document.addEventListener('DOMContentLoaded', enhanceProjectCards);

// Add theme toggle functionality (for future use)
function initializeThemeToggle() {
    const themeToggle = document.querySelector('#theme-toggle');
    if (!themeToggle) return;
    
    themeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-theme');
        const isDark = document.body.classList.contains('dark-theme');
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
    
    // Load saved theme
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
    }
}