from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from datetime import datetime

# AWS Elastic Beanstalk expects the Flask app to be named 'application'
application = Flask(__name__)

# Configuration for production
application.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'genrative-secret-key-change-in-production')

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/book-call', methods=['GET', 'POST'])
def book_call():
    if request.method == 'POST':
        # Handle form submission for booking
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        course_interest = data.get('course_interest')
        
        # Here you would integrate with a calendar API (Calendly, Google Calendar, etc.)
        # For now, we'll just return a success response
        
        return jsonify({
            'status': 'success',
            'message': 'Your consultation call has been booked! We will contact you soon.',
            'redirect': '/thank-you'
        })
    
    return render_template('book_call.html')

@application.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@application.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@application.route('/terms-of-service')
def terms_of_service():
    return render_template('terms_of_service.html')

# Health check endpoint for AWS Load Balancer
@application.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy', 
        'timestamp': datetime.utcnow().isoformat(),
        'service': 'genrative-landing-page'
    })

# AWS Beanstalk compatibility
if __name__ == '__main__':
    # For local development only
    application.run(debug=True, host='0.0.0.0', port=8000)