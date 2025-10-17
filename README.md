# 📚 Previous Year Papers Archive

> A sleek, terminal-inspired exam paper repository with instant search and easy upload functionality

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An elegant web application for archiving and searching previous year exam papers with a beautiful terminal-style interface. Built with simplicity and user experience in mind.

## ✨ Features

### 🖥️ Terminal-Style Interface
- Authentic terminal aesthetic with green phosphor theme
- Monospace Fira Code font for that retro coding feel
- Smooth animations and transitions

### 🔍 Powerful Search
- **Ctrl+K** quick search - Just like your favorite code editor!
- Real-time search results as you type
- Search by title, subject, year, tags, or paper type
- Smart keyword matching

### 📤 Easy Upload
- Intuitive upload form with all necessary fields
- Smart navigation: Type "upload" in search to go directly to upload page
- Support for PDF file uploads (up to 16MB)
- Tag system for improved search accuracy
- Verification and visibility controls

### 🎯 Key Capabilities
- Browse exam papers by subject, year, and type
- Tag-based organization for precise filtering
- Uploader attribution for each paper
- Public/private visibility options
- Responsive design that works on all devices

## 📸 Screenshots

### Main Interface
![Homepage - Terminal Interface](https://github.com/user-attachments/assets/d7e7af7b-260a-4f97-9b57-cfcdd1cb2d35)
*The main terminal-style interface with command hints*

### Search Modal
![Search Functionality](https://github.com/user-attachments/assets/f95dabe7-0cbb-4801-aac1-71cf1500f2c9)
*Quick search with Ctrl+K - Find papers instantly*

### Upload Page
![Upload Paper Form](https://github.com/user-attachments/assets/8c063ac1-8c89-4d29-91ff-73acb9fb65b2)
*Comprehensive upload form with all paper details*

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/anacondy/paper-gemini-archieve-saving-progress-2-.git
   cd paper-gemini-archieve-saving-progress-2-
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

That's it! 🎉 The application is now running locally.

## 📖 Usage Guide

### Searching for Papers

1. **Open Search Modal**
   - Press `Ctrl+K` (or `Cmd+K` on Mac)
   - The search modal will appear instantly

2. **Enter Your Query**
   - Type keywords like "Physics 2024", "calculus", "midterm", etc.
   - Results appear in real-time as you type

3. **Select a Paper**
   - Click on any result or press `Enter` to view details
   - Paper information displays in the terminal output

4. **Close Search**
   - Press `Esc` to close the search modal

### Uploading Papers

#### Method 1: Via Search (Recommended)
1. Press `Ctrl+K` to open search
2. Type "upload" (case-insensitive)
3. Press `Enter` to navigate to upload page

#### Method 2: Direct URL
Navigate directly to: `http://localhost:5000/upload`

### Filling the Upload Form

**Required Fields:**
- **Your Name**: Uploader identification
- **Paper Title**: Descriptive title (e.g., "Physics 2024 Midterm")
- **Subject**: Course subject (e.g., "Physics")
- **Year**: Academic year (e.g., 2024)
- **Paper Type**: Select from dropdown (Midterm, Final, Quiz, Practice, Assignment)

**Optional Fields:**
- **Tags**: Comma-separated keywords to improve searchability
  - Example: `calculus, derivatives, integrals, limits`
- **PDF File**: Upload the actual exam paper (optional)

**Options:**
- ✅ **Verification checkbox**: Mark if this is an authentic exam paper
- ✅ **Public availability**: Make paper searchable (checked by default)

Click **Submit Paper** to add it to the database!

## 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| **Backend** | Flask 3.0.0 (Python) |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |
| **Styling** | Custom CSS with terminal theme |
| **Font** | Fira Code (Google Fonts) |
| **Server** | Werkzeug 3.0.1 |

## 📁 Project Structure

```
paper-gemini-archieve-saving-progress-2-/
├── app.py                 # Flask application and API routes
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html        # Main page template
│   └── upload.html       # Upload page template
├── static/
│   ├── style.css         # Terminal-style CSS
│   └── script.js         # Frontend JavaScript logic
├── uploads/              # Directory for uploaded files
├── README.md            # This file
├── QUICKSTART.md        # Quick reference guide
└── LICENSE              # MIT License

```

## 🎨 Features in Detail

### Terminal Aesthetic
- **Green phosphor theme**: Authentic retro terminal look
- **Command-line style output**: Papers displayed as terminal output
- **Smooth animations**: Professional fade-in effects
- **Responsive design**: Works beautifully on mobile and desktop

### Search Intelligence
- **Multi-field search**: Searches across title, subject, type, year, and tags
- **Partial matching**: Find papers with incomplete queries
- **Real-time results**: See results as you type
- **No results handling**: Clear messaging when no papers match

### Upload System
- **Form validation**: Ensures all required fields are filled
- **File size limit**: 16MB maximum for uploaded PDFs
- **Success feedback**: Clear confirmation messages
- **Error handling**: Helpful error messages if upload fails

## 🔧 Configuration

### Upload Settings
Edit `app.py` to customize:
```python
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
```

### Port Configuration
Change the port in `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Change port here
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/features/copilot">
        <img src="https://github.githubassets.com/images/modules/site/copilot/copilot.png" width="100px;" alt="GitHub Copilot"/><br />
        <sub><b>GitHub Copilot</b></sub>
      </a><br />
      <sub>AI Pair Programmer</sub>
    </td>
    <td align="center">
      <a href="https://github.com/anacondy">
        <img src="https://github.com/anacondy.png" width="100px;" alt="anacondy"/><br />
        <sub><b>@anacondy</b></sub>
      </a><br />
      <sub>Developer</sub>
    </td>
  </tr>
</table>

---

<div align="center">

**Made with care by [GitHub Copilot](https://github.com/features/copilot) & [@anacondy](https://github.com/anacondy)**

*Built with ❤️ using Flask and vanilla JavaScript*

</div> 