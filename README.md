# Professional Internship Management Portal

🌍 **Live Demo:** [https://amaanitvam-portal.onrender.com/](https://amaanitvam-portal.onrender.com/)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0+-092E20.svg)
![MySQL](https://img.shields.io/badge/MySQL-Supported-4479A1.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3.svg)

## Overview
A comprehensive, production-ready web application designed for organizations and NGOs to manage internship applications efficiently. Built with a robust Django backend and a visually stunning, animated frontend, it offers a seamless experience for both applicants and administrators.

The project features a premium glassmorphism UI, a secure multi-step application form, and a powerful admin dashboard equipped with analytics, interactive charts, and applicant management tools.

## ✨ Key Features

### Public Portal (Applicants)
- **Modern Landing Page**: High-conversion design with hero section, animated statistics, domains, testimonials, and FAQs.
- **Dynamic Animations**: Scroll-triggered animations via AOS and custom floating/hover effects.
- **Smart Application Form**: 
  - Multi-step intuitive interface
  - Client-side and strict server-side validation
  - Drag-and-drop secure resume upload (PDF/DOC/DOCX only)
  - Beautiful SweetAlert2 success notifications

### Admin Dashboard
- **Secure Authentication**: Django-based login system protected with `@superuser_required` decorators.
- **Real-time Analytics**: Counter animations, Chart.js integration (Pie charts for status distribution, Line charts for temporal application trends).
- **Applicant Management (CRUD)**:
  - Advanced live search (by name, email, skills)
  - Status filtering and sorting
  - One-click status updates (Pending/Selected/Rejected)
  - Secure Resume preview and download
  - SweetAlert2 protected record deletion

### 🛡️ Enterprise-Grade Security
- Protection against SQL injection, XSS, and CSRF.
- Secure UUID-based file renaming for uploads to prevent malicious execution and directory traversal.
- HSTS, Strict Referrer Policies, and Secure Cookies configured for production.
- Environment variables (`.env`) for secrets management.

## 🛠️ Tech Stack
- **Backend Architecture**: Python, Django, MySQL
- **Frontend UI/UX**: HTML5, CSS3 (Custom Properties), Bootstrap 5, Vanilla JavaScript
- **Libraries**: AOS (Animate on Scroll), Chart.js, Font Awesome, SweetAlert2
- **Deployment**: Gunicorn, Whitenoise (Static file serving)

## 📁 Project Structure
```text
amaanitvam_portal/
├── core/                # Django project configuration & Security settings
├── internships/         # Main application logic (Models, Views, Forms)
├── media/               # Secure uploaded resumes
├── static/              # CSS styles, JS scripts, and Images
├── templates/           # HTML templates (Public + Dashboard)
├── requirements.txt     # Python dependencies
└── .env                 # Environment secrets
```

## 🚀 Installation & Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/div174/internship-portal.git
   cd internship-portal
   ```

2. **Environment Setup**
   Create a virtual environment and install dependencies:
   ```bash
   python -m venv env
   # Windows:
   env\Scripts\activate
   # Mac/Linux:
   source env/bin/activate
   
   pip install -r requirements.txt
   ```

3. **Database Configuration**
   - Install MySQL and create a database (e.g., `amaanitvam_db`).
   - Copy `.env.example` to `.env` and configure your credentials:
     ```env
     SECRET_KEY=your_secure_secret_key
     DEBUG=True
     DB_NAME=amaanitvam_db
     DB_USER=root
     DB_PASSWORD=your_password
     ```

4. **Run Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser (Admin Account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```
   - Homepage: `http://127.0.0.1:8000/`
   - Admin Login: `http://127.0.0.1:8000/dashboard/login/`

## ☁️ Deployment Guide (Render / Railway)

1. Set `DEBUG=False` in your production environment variables.
2. Add your deployment URL to `ALLOWED_HOSTS`.
3. Set up a managed MySQL database and update the DB credentials.
4. The application uses `Whitenoise` for static files. The build command should be:
   ```bash
   pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
   ```
5. Start command for production:
   ```bash
   gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
   ```

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
