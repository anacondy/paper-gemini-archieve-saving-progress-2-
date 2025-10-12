import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader, PdfWriter

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def sanitize(text):
    return "".join(c for c in text if c.isalnum() or c in (' ', '_', '-')).rstrip()


@app.route('/')
def terminal_ui():
    return render_template('index.html')


@app.route('/admin')
def upload_form():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    # MODIFIED: Added semester and exam_type to the list of required fields
    required_fields = ['admin_name', 'class', 'subject', 'semester', 'exam_year', 'exam_type']
    if 'file' not in request.files or not all(field in request.form for field in required_fields):
        return "<h1>Missing form data. <a href='/admin'>Please try again.</a></h1>"

    file = request.files['file']

    # Get all the metadata from the form
    admin_name = request.form['admin_name']
    class_name = request.form['class']
    subject = request.form['subject']
    semester = request.form['semester']
    exam_year = request.form['exam_year']
    exam_type = request.form['exam_type']

    if file.filename == '' or not all([admin_name, class_name, subject, semester, exam_year, exam_type]):
        return "<h1>All fields are required. <a href='/admin'>Please try again.</a></h1>"

    if file and allowed_file(file.filename):
        # --- FINAL FILE NAMING LOGIC ---
        safe_class = sanitize(class_name)
        safe_subject = sanitize(subject)
        safe_semester = sanitize(semester)
        safe_year = sanitize(exam_year)
        safe_exam_type = sanitize(exam_type)
        safe_admin = sanitize(admin_name)
        original_filename = secure_filename(file.filename)

        # Create the new, final, structured filename
        new_filename = f"[{safe_class}]_[{safe_subject}]_[Sem-{safe_semester}]_[{safe_year}]_[{safe_exam_type}]_[{safe_admin}]_[{original_filename}]"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)

        file.save(filepath)

        try:
            reader = PdfReader(filepath)
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)

            # MODIFIED: Add all new metadata to the PDF properties
            writer.add_metadata({
                "/Author": admin_name,
                "/Title": f"{class_name} - {subject} (Semester {semester})",
                "/Subject": subject,
                "/Keywords": f"{class_name}, {exam_year}, Semester {semester}, {exam_type}"
            })

            with open(filepath, "wb") as f:
                writer.write(f)

        except Exception as e:
            print(f"Could not write metadata. Error: {e}")

        # MODIFIED: New success message with a "Go to Home Page" button
        return f"""
            <style>
                body {{ font-family: sans-serif; background-color: #1a1a1a; color: #e0e0e0; padding: 40px; }}
                h1 {{ color: #4CAF50; }}
                p {{ color: #bbb; }}
                a {{ display: inline-block; margin-top: 20px; padding: 10px 15px; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 4px; }}
                a:hover {{ background-color: #45a049; }}
            </style>
            <h1>File Uploaded Successfully!</h1>
            <p>Metadata has been written directly into the PDF properties.</p>
            <p><strong>Saved as:</strong> {new_filename}</p>
            <a href="/">Go to Home Page</a>
        """
    else:
        return "<h1>Invalid file type. Only PDFs are allowed. <a href='/admin'>Try again</a></h1>"


if __name__ == '__main__':
    app.run(debug=True)
