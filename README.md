# Online Voting System
# 🗳️ Online Voting System

A web-based **Online Voting System** that allows authorized users to cast votes digitally—eliminating physical polling stations. Built using PHP/MySQL with role-based access and simple security features.

---

## 🔍 Project Overview

This system enables administrators to register voters and create elections. Once registered, voters receive unique credentials to securely log in and participate in voting. Votes are recorded in a MySQL database to ensure integrity and authenticity :contentReference[oaicite:0]{index=0}.

---

## 🔑 Features

- **User Roles**:
  - **Admin**: Manages elections, registers voters, views results
  - **Voter**: Logs in using voter ID, casts vote
- **Registration Workflow**: Admin-only registration ensures only authorized users can vote
- **Secure Login**: Voter ID and password-based authentication
- **Voting Process**: Voter selects preferred candidate and submits securely
- **Result Tallying**: Admin dashboard displays real-time results
- **Database Storage**: Votes and user data persisted via MySQL
- **Simple Web UI**: PHP, HTML, CSS/Bootstrap frontend with intuitive flow

---

## 🧭 Demo Flow

1. **Admin Login**
   - Register new voters (Name, Email, Password)
   - Create or configure elections
2. **Voter Login**
   - Sign in with credentials
   - View available elections
   - Cast vote for selected candidate
3. **Admin Dashboard**
   - View election results
   - Monitor voter participation

---

## 📂 Project Structure


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


Technologies Used:
Flask, 
Flask-SocketIO, 
Flask-Login, 
SQLAlchemy, 
Python-dotenv.
