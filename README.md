# Genrative.me - Data Engineering EdTech Landing Page

A modern, aesthetic landing page for a niche EdTech startup focused on Data Engineering education. Built with Python Flask backend and modern frontend technologies.

## Features

- **Modern Design**: Dark theme with neon blue/purple gradients and smooth animations
- **Responsive**: Mobile-first design that works on all devices
- **Interactive**: Smooth scrolling, hover effects, and animated elements
- **Conversion Focused**: Multiple CTAs leading to free consultation booking
- **Fast Loading**: Optimized CSS and JavaScript for performance

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Fonts**: Inter & JetBrains Mono from Google Fonts
- **Icons**: Font Awesome 6
- **Styling**: Custom CSS with CSS Grid and Flexbox

## Quick Start

1. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**

   ```bash
   python app.py
   ```

3. **Open in Browser**
   ```
   http://localhost:5000
   ```

## Project Structure

```
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   ├── base.html         # Base template with header/footer
│   ├── index.html        # Main landing page
│   └── thank_you.html    # Thank you page after booking
├── static/
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   ├── js/
│   │   └── main.js       # JavaScript functionality
│   └── images/           # Image assets (empty, ready for logos/graphics)
└── README.md
```

## Key Sections

### Hero Section

- Compelling headline: "Become a Data Engineer in 1–3 Months"
- Animated data pipeline visualization
- Primary CTA button for booking consultation
- Social proof statistics

### Courses Overview

- 3 course tiers (1-month, 2-month, 3-month)
- Feature comparison with pricing
- Individual CTAs for each course

### Why Choose Us

- 4 key differentiators with icons
- Hover animations and visual appeal

### How It Works

- 3-step process explanation
- Clear progression from consultation to enrollment

### Final CTA

- Reinforcement of main value proposition
- Guarantee messaging for trust building

## Customization

### Colors

Update CSS variables in `static/css/style.css`:

```css
:root {
  --primary-bg: #0a0a0f;
  --accent-primary: #00d4ff;
  --accent-secondary: #7c3aed;
  /* ... */
}
```

### Content

- Edit text content in `templates/index.html`
- Update company name/branding in `templates/base.html`
- Modify course details and pricing as needed

### Integrations

- Add calendar booking integration in `app.py` (Calendly, Google Calendar, etc.)
- Connect email service for notifications
- Add analytics tracking (Google Analytics, etc.)

## Deployment

### Local Development

```bash
python app.py
```

### Production (Example with Gunicorn)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Environment Variables

Consider adding these for production:

- `FLASK_ENV=production`
- `SECRET_KEY=your-secret-key`
- Database connection strings
- Email service credentials

## Performance Features

- Optimized CSS with minimal external dependencies
- Lazy loading animations with Intersection Observer
- Efficient JavaScript with event delegation
- Mobile-responsive images and layouts

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## License

This project is created for educational/commercial use. Customize as needed for your specific EdTech business.

## Contact

For questions about this landing page template:

- Email: contact@genrative.me
- GitHub: [https://github.com/heighterses/genrative.me/]

---

**Ready to launch your Data Engineering EdTech business? This landing page template gives you everything you need to start converting visitors into students!**
