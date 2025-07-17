# 🗳️ Online Voting System

A web-based **Online Voting System** that allows authorized users to cast votes digitally—eliminating physical polling stations. Built using PHP/MySQL with role-based access and simple security features.

---

## 🔍 Project Overview

This system enables administrators to register voters and create elections. Once registered, voters receive unique credentials to securely log in and participate in voting. Votes are recorded in a MySQL database to ensure integrity and authenticity :contentReference[oaicite:1]{index=1}.

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

## 🛠️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Naveensai357/Online-Voting-System.git
   cd Online-Voting-System
Configure environment:

Install XAMPP/LAMP/WAMP stack

Start Apache and MySQL

Import the database:

Open phpMyAdmin or CLI

Create database (e.g., votesystem)

Import db_schema.sql to set up tables

Update DB credentials:

Open config file (e.g., includes/db_connect.php)

Modify DB user/password as needed

Launch the app:

Access http://localhost/Online-Voting-System/

Use Admin panel to register voters and manage elections

👥 User Credentials
Admin

Default credentials to be defined during setup (e.g. in code/config)

Voter

Created by Admin during registration

⚙️ Technologies Used
Backend: PHP 7+

Database: MySQL

Frontend: HTML, CSS, Bootstrap

Server Stack: LAMP

📝 Limitations & Future Enhancements
✔️ Basic credential-based security

🔴 No email verification or password hashing—must be improved for production

🔴 Lacks audit/logging for votes cast

🔄 Possible upgrades:

Password hashing (bcrypt/Argon2)

Token/email-based voter authentication

Audit logs and vote integrity checks

Captcha/anti-bot mechanisms

UI/UX improvements

📁 Screenshots
(Add screenshots of admin UI, voting page, results dashboard in docs/)
