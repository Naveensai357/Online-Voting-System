# Online Voting System
Election1
A simple web-based election/voting system built with Flask, Flask-SocketIO, and Flask-Login. This project provides both admin and client interfaces for managing and participating in elections, with real-time updates using WebSockets.
Features
Admin Panel: Manage users, elections, and view results.
Client Voting: Users can vote via a web form.
Real-Time Updates: Uses WebSockets for live updates.
User Authentication: Admins are authenticated using Flask-Login.
Modular Codebase: Uses Flask Blueprints for clean separation of admin and client logic.
Project Structure
Election1-main/
admin_frontend.py # Admin interface and routes
client_frontend.py # Client (voter) interface and routes
db.py # Database models and session management
main.py # Main app entry point
requirements.txt # Python dependencies
templates/
vote_form.html # Voting form template
vote_consumer.py # WebSocket event handling
Getting Started
Prerequisites
Python 3.8+
pip
Installation
Clone the repository:
git clone https://github.com/yourusername/Election1.git
cd Election1-main
Install dependencies:
pip install -r requirements.txt
Set up environment variables:
Create a .env.local file in the root directory.
Add the following (replace with your own secret key if desired):
SECRET_KEY=your_secret_key_here
Run the application:
python main.py
The app will be available at http://localhost:8000
Usage
Visit /admin for the admin interface.
Visit /client for the client (voter) interface.
The root / route displays the voting form.
Technologies Used
Flask
Flask-SocketIO
Flask-Login
SQLAlchemy
Python-dotenv
License
This project is licensed under the MIT License.
