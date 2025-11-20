import random
import string
from flask import Flask, request, render_template

# Create Flask app
app = Flask(__name__)

# Define route for home page
@app.route('/', methods=['GET', 'POST'])
def home():
    password = None

# Handle form submission
    if request.method == 'POST':
        num_letters = int(request.form.get('letters'))
        num_symbols = int(request.form.get('symbols'))
        num_numbers = int(request.form.get('numbers'))

# Generate password
        letters = string.ascii_letters
        numbers = string.digits
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Create password list
        password_list = []

        for _ in range(num_letters):
            password_list.append(random.choice(letters))
        for _ in range(num_symbols):
            password_list.append(random.choice(symbols))
        for _ in range(num_numbers):
            password_list.append(random.choice(numbers))

# Shuffle and join to form the final password
        random.shuffle(password_list)
        password = ''.join(password_list)

# Render template with password
    return render_template('indix.html', password=password)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
