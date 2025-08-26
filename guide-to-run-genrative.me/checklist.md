# Quick Checklist - Running genrative.me Application

## First Time Setup ✅

- [ ] Open Terminal
- [ ] Navigate to project: `cd /Users/user/Desktop/genrative.me`
- [ ] Create virtual environment: `python3 -m venv venv`
- [ ] Activate virtual environment: `source venv/bin/activate`
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Run application: `python app.py`
- [ ] Open browser: `http://localhost:8000`

## Daily Run (After First Setup) ✅

- [ ] Open Terminal
- [ ] Navigate to project: `cd /Users/user/Desktop/genrative.me`
- [ ] Activate virtual environment: `source venv/bin/activate`
- [ ] Run application: `python app.py`
- [ ] Open browser: `http://localhost:8000`

## Pre-Flight Checks ✅

Before running, make sure:
- [ ] You're in the correct directory (`/Users/user/Desktop/genrative.me`)
- [ ] Virtual environment folder exists (`venv/`)
- [ ] Requirements file exists (`requirements.txt`)
- [ ] Main app file exists (`app.py`)
- [ ] Templates folder exists (`templates/`)
- [ ] Static files folder exists (`static/`)

## Success Indicators ✅

You know it's working when:
- [ ] Terminal shows: `Running on http://0.0.0.0:8000`
- [ ] No error messages in terminal
- [ ] Browser loads the page at `http://localhost:8000`
- [ ] Page has dark theme with blue/purple colors
- [ ] "DataFlow Academy" title is visible
- [ ] "Become a Data Engineer in 1–3 Months" headline shows
- [ ] Course sections are visible
- [ ] Booking buttons work

## Quick Commands Reference 📝

```bash
# Navigate to project
cd /Users/user/Desktop/genrative.me

# Activate virtual environment
source venv/bin/activate

# Run the app
python app.py

# Stop the app
Ctrl + C

# Deactivate virtual environment
deactivate
```

## Alternative: Use Quick Start Script 🚀

Instead of manual steps, you can run:
```bash
/Users/user/Desktop/guide-to-run-genrative.me/quick-start.sh
```

## Emergency Commands 🆘

If something goes wrong:
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Reset virtual environment
rm -rf venv && python3 -m venv venv

# Check if you're in right directory
pwd
```

## File Structure Check 📁

Your project should look like this:
```
genrative.me/
├── app.py ✓
├── requirements.txt ✓
├── venv/ ✓ (after setup)
├── templates/
│   ├── base.html ✓
│   ├── index.html ✓
│   └── thank_you.html ✓
├── static/
│   ├── css/style.css ✓
│   ├── js/main.js ✓
│   └── images/ ✓
└── README.md ✓
```

---

**Print this checklist and keep it handy for quick reference!**
