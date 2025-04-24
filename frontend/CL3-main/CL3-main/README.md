 Library Management System

Project Overview
Library Management System is a web application that uses the Django framework in Python. It offers a convenient method of managing books, users, and transactions within a library. The system is able to automate book lending, reminders for due dates, and user account management.

Libraries usually have problems with hand-keeping books and ineffective tracking systems. The project was developed to:
- Automate book management and lending processes.
- Enhance the efficiency of book searches and transactions.
- Minimize manual errors in book borrowing and returns.
- Offer a simple-to-use interface for librarians and users.

 Tech Stack
- Backend: Django (Python)
- rontend: HTML, CSS, JavaScript
- Database: SQLite (default), can be changed to PostgreSQL/MySQL

 How to Set Up the Project
 1️⃣ Clone the Repository

 git clone https://github.com/pratik152IT/CL3.git

2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows


 3️⃣ Install Dependencies

pip install -r requirements.txt


4️⃣ Apply Migrations & Create Superuser

python manage.py migrate
python manage.py createsuperuser


 5️⃣ Run the Development Server

python manage.py runserver

Go to 'http://127.0.0.1:8000/' in your browser.

 Features
- User authentication (Admin, Librarians, Students)
- Book catalog management (Add, Update, Delete books)
- Borrowing and return system with due dates
- Calculation for fine on overdue books
- Search for users and books

 Application of Django in the Project
Django provides a powerful and scalable backend for handling user authentication, database interactions, and API requests. Some key Django features used:
Django ORM for database management
Django Admin Panel for managing books and users
Django Authentication for user roles
Django Views & Templates for rendering the frontend


 Improvements in Future
- Introduce an API for integration with mobile devices
- Introduce an AI-based book recommendation system
- Introduce a barcode reader to identify books
- Implement email reminders for due dates
- Enhance UI using React or Vue.js to provide an improved user interface

 Contributing
You can contribute! Just fork this repository and submit a pull request.

 License
This is an open-source project and released under the MIT License.

---	
Happy Coding! 

Output:

![image](https://github.com/user-attachments/assets/16ba868d-8293-47e4-9931-363c8b7d0026)

![image](https://github.com/user-attachments/assets/c7d6b0af-928c-405f-9aa4-428eadfae981)





