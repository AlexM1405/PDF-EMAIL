from flask import Flask, request, jsonify
import fitz  
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the API'})

@app.route('/upload', methods=['POST'])
def upload_and_process_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        email_address = request.form.get('email')  
        
        try:
            pdf_content = extract_first_30_lines(file)
            send_email(email_address, pdf_content)
            return jsonify({'success': True, 'message': f'The email has been successfully sent to {email_address}'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

def extract_first_30_lines(pdf_file):
    try:
        doc = fitz.open(stream=pdf_file.read())
        text_pages = [page.get_text() for page in doc]
        full_text = "\n".join(text_pages)

        lines = full_text.split('\n')
        num_lines_to_extract = min(30, len(lines))
        extracted_lines = lines[:num_lines_to_extract]
        extracted_text = "\n".join(extracted_lines)

        print(f"Extracted text: {extracted_text}")  # Debugging statement
        return extracted_text
    except Exception as e:
        print(f"An error occurred while processing the PDF: {e}")
        return ""


def send_email(to, extracted_text):
    sender_email = "rocketbot418@gmail.com"
    sender_password = "zekkjhlxtgpqkewv"  #Rocketbot122$
  
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to
    msg['Subject'] = 'Extracted PDF Content'
    


    body = MIMEText(extracted_text, 'plain', 'utf-8')
    msg.attach(body)
    
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        print(f"Sending email with body:\n{text}")
        server.sendmail(sender_email, to, text)
        server.quit()
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

if __name__ == '__main__':
    app.run()