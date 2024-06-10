
CODE-CHALLENGE PDF-to-Email 

instructions
git clone https://github.com/AlexM1405/PDF-EMAIL.git

Install the required Python packages:
pip install -r requirements.txt


START THE APLICATION
python app.py

Access the application in your web browser at http://localhost:5000.
TO SEND A EMIAL THIS URL
https://www.postman.com/
HTTP POST http://localhost:5000/upload

In the request body section below the URL input field
select the "form-data" option.
Enter file in the key field and choose "file" from the dropdown menu on the right.
Click on the "Select Files" button that appears and choose a PDF file from your computer to upload.
then add your email.
the key have to "file" and "email"

NOTE: THE PDF FILE HAVE TO ONLY HAVE TEXT TO WORK 


