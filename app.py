from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book-call', methods=['GET', 'POST'])
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

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)