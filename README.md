# Previous Year Papers Archive

Exam paper downloading website with Ctrl+K search functionality and upload capability.

## Features

- **Terminal-style interface** with green theme
- **Ctrl+K search functionality** - Quick search through exam papers database
- **Smart upload navigation** - Type "upload" (case-insensitive) in search to navigate to upload page
- **Upload form** with:
  - Uploader name field
  - Paper details (title, subject, year, type)
  - Tags for better search accuracy
  - Verification and public availability checkboxes
  - File upload support

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

### Search Papers
- Press `Ctrl+K` to open the search modal
- Type your query (e.g., "Physics 2024")
- Press Enter to view paper details
- Press Esc to close the search modal

### Upload Papers
- Press `Ctrl+K` and type "upload" (or "UPLOAD")
- Press Enter to navigate to the upload page
- Fill in the required information:
  - Your name (uploader)
  - Paper title
  - Subject
  - Year
  - Paper type
  - Tags (comma-separated) - helps improve search accuracy
  - Optional: Upload PDF file
- Check verification and visibility options
- Click "Submit Paper"

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Terminal-inspired green theme with Fira Code font


Made with care by Puppy pilot & anacondy 