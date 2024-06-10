Technical Test: Python/Node
Objective:
The objective of this technical test is to assess the candidate's proficiency in Python or Node.js and their ability to develop a RESTful API that works with automation libraries
Requirements:
Develop a RESTful API using Node or Python
The API should include the following functionalities:
Receive a PDF file.
Extract the first 30 lines of the PDF.
Send an email with the extracted content to the provided email address.
Instructions:
The candidate can choose between Node and Python.
Include a README.md file with instructions for installing dependencies, running the project, and any other relevant details.
The project should be uploaded to a public GitHub repository.
Delivery time is 3 working days.
Example Endpoint:
Request (Node.js or Python):
http
POST /upload
Content-Type: multipart/form-data

{
    "file": <pdf-file>,
    "email": "example@example.com"
}


​
Expected Response:
{
    "success": true,
    "message": "The email has been successfully sent to example@example.com"
}

