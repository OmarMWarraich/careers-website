from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'description': 'We are looking for a software engineer to join our team.',
        'location': 'San Francisco, CA',
        'salary': '$100,000 - $150,000',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'description': 'We are looking for a data scientist to join our team.',
        'location': 'New York, NY',
        'salary': '$80,000 - $120,000',
    },
    {
        'id': 3,
        'title': 'Blockchain Developer',
        'description': 'We are looking for a product manager to join our team.',
        'location': 'San Francisco, CA',
        'salary': '$120,000 - $180,000',
    },
    {
        'id': 4,
        'title': 'Artificial Intelligence Engineer',
        'description': 'We are looking for an artificial intelligence engineer to join our team.',
        'location': 'San Francisco, CA',
        'salary': '$120,000 - $180,000',
    },
]

@app.route('/')

def hello_world():
    return render_template('home.html'
                           , jobs=JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
