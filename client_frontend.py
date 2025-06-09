from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from db import SessionLocal, Vote  # assuming Vote is your model

client_bp = Blueprint('client', __name__, template_folder='templates')


# Route to render voting form
@login_required
@client_bp.route('/')
def vote_form():
    return render_template('vote_form.html')  # make sure this file exists


# Route to handle vote submission and save to database
@login_required
@client_bp.route('/submit_vote', methods=['POST'])
def submit_vote():
    voter_id = request.form.get('voter_id')
    candidate = request.form.get('candidate')

    # Ensure form values are provided
    if not voter_id or not candidate:
        return "<h3>❌ Missing Voter ID or Candidate</h3><a href='/client'>Try Again</a>"

    db = SessionLocal()
    try:
        # Check if voter already voted
        existing_vote = db.query(Vote).filter_by(voter_id=voter_id).first()
        if existing_vote:
            return "<h3>❌ You have already voted!</h3><a href='/client'>Back</a>"

        vote = Vote(voter_id=voter_id, candidate=candidate)
        db.add(vote)
        db.commit()
        return f"<h3>✅ Vote submitted successfully and saved to database!</h3><a href='/client'>Vote Again</a>"
    except Exception as e:
        db.rollback()
        return f"<h3>❌ Error saving vote: {e}</h3><a href='/client'>Try Again</a>"
    finally:
        db.close()
