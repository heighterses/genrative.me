# Guide to Run "genrative.me" Application

This guide provides step-by-step instructions to run the DataFlow Academy Flask application located at `/Users/user/Desktop/genrative.me`.

## Prerequisites

- macOS system
- Python 3 installed
- Terminal access

## Quick Start (For Experienced Users)

```bash
cd /Users/user/Desktop/genrative.me
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open: http://localhost:8000

## Detailed Step-by-Step Instructions

### Step 1: Open Terminal
- Press `Cmd + Space` and type "Terminal"
- Or go to Applications → Utilities → Terminal

### Step 2: Navigate to Project Directory
```bash
cd /Users/user/Desktop/genrative.me
```

### Step 3: Create Virtual Environment (First Time Only)
```bash
python3 -m venv venv
```
This creates a folder called `venv` with isolated Python environment.

### Step 4: Activate Virtual Environment
```bash
source venv/bin/activate
```
You should see `(venv)` appear at the beginning of your terminal prompt.

### Step 5: Install Dependencies (First Time Only)
```bash
pip install -r requirements.txt
```
This installs Flask and other required packages.

### Step 6: Run the Application
```bash
python app.py
```

### Step 7: Access the Website
Open your web browser and go to:
```
http://localhost:8000
```

You should see the DataFlow Academy landing page with:
- Dark theme with neon blue/purple gradients
- Hero section with "Become a Data Engineer in 1–3 Months"
- Course overview sections
- Booking consultation forms

## For Future Runs

After the initial setup, you only need these commands:

```bash
cd /Users/user/Desktop/genrative.me
source venv/bin/activate
python app.py
```

## Stopping the Application

To stop the Flask server:
- Press `Ctrl + C` in the terminal

To deactivate the virtual environment:
```bash
deactivate
```

## Project Structure

```
genrative.me/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── venv/                 # Virtual environment (created after setup)
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Main landing page
│   └── thank_you.html    # Thank you page
├── static/
│   ├── css/
│   │   └── style.css     # Styling
│   ├── js/
│   │   └── main.js       # JavaScript
│   └── images/           # Image assets
└── README.md
```

## Troubleshooting

### Common Issues and Solutions

**1. "python: command not found"**
- Use `python3` instead of `python`

**2. "Address already in use" or Port 5000/8000 busy**
- Edit `app.py` and change the port number in the last line:
  ```python
  app.run(debug=True, host='0.0.0.0', port=3000)  # Change to any available port
  ```

**3. "ModuleNotFoundError: No module named 'flask'"**
- Make sure virtual environment is activated (you should see `(venv)` in terminal)
- Run `pip install -r requirements.txt` again

**4. "externally-managed-environment" error**
- This is why we use virtual environment - make sure you activated it with `source venv/bin/activate`

**5. Permission denied errors**
- Make sure you're in the correct directory: `/Users/user/Desktop/genrative.me`

### Alternative Port Numbers
If port 8000 is busy, try these ports:
- 3000
- 8080
- 9000
- 5001

### Checking if App is Running
- Look for output like: `Running on http://0.0.0.0:8000`
- Open the URL in your browser
- You should see the DataFlow Academy landing page

## Features of the Application

Once running, you'll have access to:

- **Modern Landing Page**: Dark theme with animated elements
- **Course Sections**: 1-month, 2-month, and 3-month programs
- **Booking System**: Consultation booking forms
- **Responsive Design**: Works on desktop and mobile
- **Interactive Elements**: Smooth scrolling and hover effects

## Development Notes

- The app runs in debug mode for development
- Changes to Python files require restarting the server
- Changes to HTML/CSS/JS files are reflected immediately
- Server logs appear in the terminal

## Contact & Support

For issues with this guide or the application:
- Check the main project README at `/Users/user/Desktop/genrative.me/README.md`
- Ensure all files are present in the project directory
- Verify Python 3 is properly installed on your system

---

**Happy coding! Your DataFlow Academy application should now be running successfully.**
