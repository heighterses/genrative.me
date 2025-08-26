# Troubleshooting Guide - genrative.me Application

## Common Issues and Solutions

### 1. Port Already in Use

**Error Message:**
```
Address already in use
Port 5000/8000 is in use by another program
```

**Solutions:**
- **Option A:** Kill the process using the port
  ```bash
  lsof -ti:8000 | xargs kill -9
  ```

- **Option B:** Use a different port
  Edit `app.py` and change the last line:
  ```python
  app.run(debug=True, host='0.0.0.0', port=3000)  # Use port 3000 instead
  ```

- **Option C:** Disable macOS AirPlay Receiver (for port 5000)
  System Preferences → Sharing → Uncheck "AirPlay Receiver"

### 2. Python Command Not Found

**Error Message:**
```
bash: python: command not found
```

**Solution:**
Use `python3` instead of `python`:
```bash
python3 app.py
```

### 3. Flask Module Not Found

**Error Message:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solutions:**
1. Make sure virtual environment is activated:
   ```bash
   source venv/bin/activate
   ```
   You should see `(venv)` in your terminal prompt.

2. Install requirements again:
   ```bash
   pip install -r requirements.txt
   ```

### 4. Externally Managed Environment

**Error Message:**
```
error: externally-managed-environment
```

**Solution:**
This is exactly why we use virtual environments. Make sure you:
1. Created the virtual environment: `python3 -m venv venv`
2. Activated it: `source venv/bin/activate`
3. Then install packages: `pip install -r requirements.txt`

### 5. Permission Denied

**Error Message:**
```
Permission denied
```

**Solutions:**
- Make sure you're in the correct directory:
  ```bash
  cd /Users/user/Desktop/genrative.me
  ```
- Check file permissions:
  ```bash
  ls -la app.py
  ```

### 6. Virtual Environment Issues

**Problem:** Virtual environment not working properly

**Solutions:**
- Delete and recreate virtual environment:
  ```bash
  rm -rf venv
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

### 7. Browser Can't Connect

**Problem:** Browser shows "This site can't be reached"

**Check:**
1. Flask server is running (check terminal for "Running on..." message)
2. Correct URL: `http://localhost:8000` (not https)
3. Correct port number matches what's in app.py

### 8. Page Loads But Looks Broken

**Problem:** HTML loads but no styling/JavaScript

**Solutions:**
- Check if static files exist:
  ```bash
  ls -la static/css/style.css
  ls -la static/js/main.js
  ```
- Clear browser cache (Cmd+Shift+R on Mac)
- Check browser console for errors (F12 → Console tab)

### 9. Template Not Found Error

**Error Message:**
```
TemplateNotFound: index.html
```

**Solution:**
- Check if templates directory exists:
  ```bash
  ls -la templates/
  ```
- Make sure you're running from the correct directory:
  ```bash
  pwd  # Should show /Users/user/Desktop/genrative.me
  ```

### 10. Requirements.txt Not Found

**Error Message:**
```
No such file or directory: 'requirements.txt'
```

**Solution:**
- Make sure you're in the project directory:
  ```bash
  cd /Users/user/Desktop/genrative.me
  ls -la requirements.txt
  ```

## Diagnostic Commands

### Check Current Directory
```bash
pwd
```

### List Project Files
```bash
ls -la
```

### Check Python Version
```bash
python3 --version
```

### Check if Virtual Environment is Active
```bash
which python
# Should show path with 'venv' if activated
```

### Check Running Processes on Port
```bash
lsof -i :8000
```

### Check Flask Installation
```bash
pip list | grep -i flask
```

## Emergency Reset

If everything is broken, start fresh:

```bash
cd /Users/user/Desktop/genrative.me
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

## Getting Help

1. **Check the main README:** `/Users/user/Desktop/genrative.me/README.md`
2. **Verify file structure:** Make sure all files are present
3. **Check terminal output:** Look for specific error messages
4. **Test step by step:** Run each command individually

## Success Indicators

You know everything is working when:
- Terminal shows: `Running on http://0.0.0.0:8000`
- Browser loads the DataFlow Academy page at `http://localhost:8000`
- Page has dark theme with blue/purple gradients
- All sections load properly (Hero, Courses, etc.)

---

**Still having issues? Double-check that you're following the steps in the exact order from the main README.md guide.**
