from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Secret key for flashing messages
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure key

# Flask-Mail Configuration (For Gmail, use an App Password)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your_app_password'  # Use an App Password, NOT your regular password
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'  # Must match MAIL_USERNAME

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        flash("All fields are required!", "danger")
        return redirect(url_for('home'))

    try:
        msg = Message(
            subject=f"New Contact from {name}",
            sender=email,  
            recipients=['your_email@gmail.com'],  # Change this to your recipient email
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )

        mail.send(msg)
        flash("Message sent successfully!", "success")
    except Exception as e:
        flash(f"Error sending message: {str(e)}", "danger")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
