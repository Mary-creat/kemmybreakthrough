from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint for personal assistant interaction
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = process_user_input(user_input)
    return jsonify({'response': response})

def process_user_input(user_input):
    if 'weather' in user_input:
        # You can use an external weather API here to fetch weather information.
        weather_data = requests.get('https://api.example.com/weather').json()
        return f"The weather today is {weather_data['description']}."

    if 'news' in user_input:
        # You can use an external news API to fetch the latest news.
        news_data = requests.get('https://api.example.com/news').json()
        return f"Here are the latest headlines: {', '.join(news_data['headlines'])}."

    if 'calculate' in user_input:
        try:
            expression = user_input.split('calculate')[1].strip()
            result = eval(expression)
            return f"The result is {result}."
        except Exception as e:
            return "Sorry, I couldn't perform the calculation."

    return "I'm not sure how to assist with that."

if __name__ == '__main__':
    app.run(debug=True)
