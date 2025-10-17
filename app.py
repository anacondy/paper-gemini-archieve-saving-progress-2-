from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Sample database of exam papers
papers_db = [
    {
        'id': 1,
        'title': 'Physics 2024 Midterm',
        'subject': 'Physics',
        'year': 2024,
        'type': 'Midterm',
        'tags': ['physics', '2024', 'midterm'],
        'filename': 'physics_2024_midterm.pdf'
    },
    {
        'id': 2,
        'title': 'Mathematics 2023 Final',
        'subject': 'Mathematics',
        'year': 2023,
        'type': 'Final',
        'tags': ['mathematics', '2023', 'final', 'calculus'],
        'filename': 'math_2023_final.pdf'
    },
    {
        'id': 3,
        'title': 'Chemistry 2024 Quiz',
        'subject': 'Chemistry',
        'year': 2024,
        'type': 'Quiz',
        'tags': ['chemistry', '2024', 'quiz', 'organic'],
        'filename': 'chemistry_2024_quiz.pdf'
    },
    {
        'id': 4,
        'title': 'Computer Science 2023 Midterm',
        'subject': 'Computer Science',
        'year': 2023,
        'type': 'Midterm',
        'tags': ['computer science', '2023', 'midterm', 'algorithms'],
        'filename': 'cs_2023_midterm.pdf'
    },
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload_page():
    return render_template('upload.html')

@app.route('/api/search')
def search():
    query = request.args.get('q', '').lower()
    
    if not query:
        return jsonify([])
    
    # Search through papers
    results = []
    for paper in papers_db:
        # Search in title, subject, type, and tags
        if (query in paper['title'].lower() or 
            query in paper['subject'].lower() or
            query in paper['type'].lower() or
            any(query in tag for tag in paper['tags']) or
            str(paper['year']) in query):
            results.append(paper)
    
    return jsonify(results)

@app.route('/api/upload', methods=['POST'])
def upload_paper():
    try:
        # Get form data
        uploader_name = request.form.get('uploader_name')
        paper_title = request.form.get('paper_title')
        subject = request.form.get('subject')
        year = request.form.get('year')
        paper_type = request.form.get('paper_type')
        tags = request.form.get('tags', '')
        
        # Get checkboxes
        verified = request.form.get('verified') == 'on'
        public = request.form.get('public') == 'on'
        
        # Get uploaded file
        file = request.files.get('paper_file')
        
        if not all([uploader_name, paper_title, subject, year, paper_type]):
            return jsonify({'success': False, 'error': 'Missing required fields'}), 400
        
        filename = None
        if file and file.filename:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Create new paper entry
        new_paper = {
            'id': len(papers_db) + 1,
            'title': paper_title,
            'subject': subject,
            'year': int(year),
            'type': paper_type,
            'tags': [tag.strip() for tag in tags.split(',') if tag.strip()],
            'filename': filename,
            'uploader': uploader_name,
            'verified': verified,
            'public': public
        }
        
        papers_db.append(new_paper)
        
        return jsonify({'success': True, 'paper': new_paper})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
