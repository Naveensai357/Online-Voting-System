from flask import Flask, render_template_string, redirect
import json
from flask import Blueprint, render_template
from sqlalchemy.orm import Session
from db import SessionLocal, Vote
import dotenv

from flask_login import LoginManager
from db import SessionLocal, User
from flask import request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

admin_bp = Blueprint('admin', __name__)
dotenv.load_dotenv(".env.local")

base_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>VoteSecure Admin</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: #f8f9fa;
            color: #333;
            line-height: 1.6;
        }
        
        .nav {
            background: #fff;
            border-bottom: 1px solid #dee2e6;
            padding: 1rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 2rem;
        }
        
        .logo {
            font-size: 1.5rem;
            font-weight: 600;
            color: #2563eb;
            text-decoration: none;
        }
        
        .nav-links {
            display: flex;
            gap: 1.5rem;
            list-style: none;
        }
        
        .nav-link {
            color: #6b7280;
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 6px;
        }
        
        .nav-link:hover {
            background: #f3f4f6;
            color: #2563eb;
        }
        
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 2rem;
        }
        
        .card {
            background: #fff;
            border-radius: 8px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .btn {
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 6px;
            font-weight: 500;
            text-decoration: none;
            display: inline-block;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .btn-primary { background: #2563eb; color: white; }
        .btn-primary:hover { background: #1d4ed8; }
        .btn-success { background: #059669; color: white; }
        .btn-success:hover { background: #047857; }
        
        .form-group { margin-bottom: 1rem; }
        .form-label { display: block; margin-bottom: 0.5rem; font-weight: 500; }
        .form-input {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #d1d5db;
            border-radius: 6px;
            font-size: 1rem;
        }
        .form-input:focus {
            outline: none;
            border-color: #2563eb;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
        }
        
        .alert {
            padding: 0.75rem 1rem;
            border-radius: 6px;
            margin-bottom: 1rem;
        }
        .alert-success { background: #d1fae5; color: #065f46; border: 1px solid #a7f3d0; }
        .alert-warning { background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }
        .alert-danger { background: #fee2e2; color: #991b1b; border: 1px solid #fecaca; }
    </style>
</head>
<body>
    <nav class="nav">
        <div class="nav-container">
            <a href="/" class="logo">🗳️ VoteSecure</a>
            <ul class="nav-links">
                <li><a href="/" class="nav-link">Dashboard</a></li>
                {% if current_user.is_authenticated %}
                    <li><a href="/admin/logout" class="nav-link">Sign Out</a></li>
                {% else %}
                    <li><a href="/admin/login" class="nav-link">Sign In</a></li>
                {% endif %}
            </ul>
        </div>
    </nav>
    <div class="container">
</body>
</html>
"""

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = SessionLocal()
        email = request.form.get('email')
        password = request.form.get('password')
        user = db.query(User).filter(User.email == email).first()
        db.close()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template_string(base_template + """
        <div style="max-width: 400px; margin: 3rem auto;">
            <div class="card" style="padding: 2rem;">
                <h1 style="text-align: center; margin-bottom: 2rem; color: #2563eb;">Admin Login</h1>
                <form method="POST">
                    <div class="form-group">
                        <label for="email" class="form-label">Email</label>
                        <input type="email" class="form-input" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="password" class="form-label">Password</label>
                        <input type="password" class="form-input" id="password" name="password" required>
                    </div>
                    <button type="submit" class="btn btn-primary" style="width: 100%;">Sign In</button>
                </form>
            </div>
        </div>
    </div>
    """)

@admin_bp.route('/')
@login_required
def dashboard():
    return render_template_string(base_template + """
        <h1 style="text-align: center; margin-bottom: 2rem; color: #1f2937;">Admin Dashboard</h1>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
            <div class="card" style="padding: 2rem;">
                <h3 style="margin-bottom: 1rem; color: #2563eb;">📊 Election Results</h3>
                <p style="color: #6b7280; margin-bottom: 1.5rem;">View voting results and analytics</p>
                <a href="/admin/results" class="btn btn-primary">View Results</a>
            </div>
            
            <div class="card" style="padding: 2rem;">
                <h3 style="margin-bottom: 1rem; color: #059669;">🗳️ Voting Interface</h3>
                <p style="color: #6b7280; margin-bottom: 1.5rem;">Access the voting system</p>
                <a href="/client" class="btn btn-success">Go to Voting</a>
            </div>
        </div>
    </div>
    """)

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('admin.login'))

@login_required
@admin_bp.route('/results')
def results():
    db: Session = SessionLocal()
    try:
        votes = db.query(Vote).all()
        counts = {}
        for vote in votes:
            candidate = vote.candidate
            counts[candidate] = counts.get(candidate, 0) + 1
    finally:
        db.close()

    candidates = list(counts.keys())
    vote_counts = list(counts.values())
    total_votes = sum(vote_counts)

    return render_template_string(base_template + """
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="color: #1f2937; margin-bottom: 0.5rem;">Election Results</h1>
        <p style="color: #6b7280;">Live voting data</p>
    </div>

    {% if counts %}
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem; margin-bottom: 2rem;">
            <div class="card" style="padding: 1.5rem; text-align: center;">
                <div style="font-size: 2rem; font-weight: bold; color: #2563eb;">{{ total_votes }}</div>
                <div style="color: #6b7280; font-size: 0.875rem;">Total Votes</div>
            </div>
            <div class="card" style="padding: 1.5rem; text-align: center;">
                <div style="font-size: 2rem; font-weight: bold; color: #059669;">{{ candidates|length }}</div>
                <div style="color: #6b7280; font-size: 0.875rem;">Candidates</div>
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 2rem; margin-bottom: 2rem;">
            <div class="card" style="padding: 1.5rem;">
                <h3 style="text-align: center; margin-bottom: 1rem;">Vote Count</h3>
                <canvas id="barChart" width="400" height="300"></canvas>
            </div>
            <div class="card" style="padding: 1.5rem;">
                <h3 style="text-align: center; margin-bottom: 1rem;">Distribution</h3>
                <canvas id="pieChart" width="400" height="300"></canvas>
            </div>
        </div>

        <div class="card" style="padding: 1.5rem;">
            <h3 style="margin-bottom: 1rem;">Detailed Results</h3>
            <table style="width: 100%; border-collapse: collapse;">
                <thead>
                    <tr style="border-bottom: 2px solid #e5e7eb;">
                        <th style="text-align: left; padding: 0.75rem;">Candidate</th>
                        <th style="text-align: center; padding: 0.75rem;">Votes</th>
                        <th style="text-align: center; padding: 0.75rem;">Percentage</th>
                    </tr>
                </thead>
                <tbody>
                    {% for name, count in counts.items() %}
                    <tr style="border-bottom: 1px solid #f3f4f6;">
                        <td style="padding: 0.75rem; font-weight: 500;">{{ name }}</td>
                        <td style="text-align: center; padding: 0.75rem;">{{ count }}</td>
                        <td style="text-align: center; padding: 0.75rem;">{{ "%.1f"|format((count/total_votes)*100) }}%</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    {% else %}
        <div class="card" style="padding: 3rem; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📊</div>
            <h3 style="margin-bottom: 0.5rem;">No Votes Yet</h3>
            <p style="color: #6b7280;">Waiting for votes to be cast...</p>
        </div>
    {% endif %}

    <div style="text-align: center; margin-top: 2rem;">
        <a href="/admin" class="btn btn-primary">← Back to Dashboard</a>
    </div>

    <script>
        const candidates = {{ candidates | tojson }};
        const voteCounts = {{ vote_counts | tojson }};
        
        const colors = ['#2563eb', '#059669', '#dc2626', '#f59e0b', '#7c3aed', '#db2777'];

        // Bar Chart
        const barCtx = document.getElementById('barChart').getContext('2d');
        new Chart(barCtx, {
            type: 'bar',
            data: {
                labels: candidates,
                datasets: [{
                    label: 'Votes',
                    data: voteCounts,
                    backgroundColor: colors.slice(0, candidates.length),
                    borderRadius: 4
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false } },
                scales: {
                    y: { beginAtZero: true, ticks: { stepSize: 1 } }
                }
            }
        });

        // Pie Chart
        const pieCtx = document.getElementById('pieChart').getContext('2d');
        new Chart(pieCtx, {
            type: 'doughnut',
            data: {
                labels: candidates,
                datasets: [{
                    data: voteCounts,
                    backgroundColor: colors.slice(0, candidates.length)
                }]
            },
            options: {
                responsive: true,
                cutout: '50%',
                plugins: {
                    legend: { position: 'bottom' }
                }
            }
        });
    </script>
    </div>
    """, counts=counts, candidates=candidates, vote_counts=vote_counts, total_votes=total_votes)