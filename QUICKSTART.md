# Quick Start Guide

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the Flask server:
```bash
python app.py
```

Open your browser and navigate to: `http://localhost:5000`

## Usage

### Searching Papers

1. Press `Ctrl+K` (or `Cmd+K` on Mac) to open the search modal
2. Type your search query (e.g., "Physics 2024", "calculus", etc.)
3. Press `Enter` to view paper details or click on a result
4. Press `Esc` to close the search modal

### Uploading Papers

**Method 1: Via Search**
1. Press `Ctrl+K` to open search
2. Type "upload" or "UPLOAD" (case-insensitive)
3. Press `Enter` to navigate to the upload page

**Method 2: Direct URL**
- Navigate to `http://localhost:5000/upload`

### Fill Upload Form

Required fields:
- Your Name (Uploader)
- Paper Title
- Subject
- Year
- Paper Type (select from dropdown)

Optional fields:
- Tags (comma-separated) - helps improve search accuracy
- Upload PDF file
- Verification checkbox
- Public availability checkbox

### Tags System

Tags are crucial for improving search accuracy:
- Add multiple tags separated by commas
- Examples: "calculus, integrals, derivatives"
- Papers with matching tags appear in search results
- Tags are displayed in search results for easy identification

## Features

✅ Terminal-style interface with green theme
✅ Ctrl+K quick search
✅ Case-insensitive "upload" keyword detection
✅ Comprehensive upload form
✅ Tag-based search enhancement
✅ Real-time search results
✅ Form validation
✅ Success/error messages

## Tech Stack

- Flask 3.0.0
- Vanilla JavaScript
- HTML5/CSS3
- Fira Code font (terminal aesthetic)
