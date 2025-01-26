from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Глобальные переменные для хранения данных
events = [
    "Футбольный матч - 10 ноября",
    "Беговой забег - 15 ноября",
    "Йога в парке - 20 ноября",
    "Велосипедный тур - 25 ноября",
    "Турнир по волейболу - 30 ноября",
    "Зимний забег - 5 декабря"
]

participant_events = []  # Мероприятия, на которые записался участник

@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/profile/participant', methods=['GET', 'POST'])
def participant_profile():
    if request.method == 'POST':
        event = request.form.get('event')
        if event and event not in participant_events:
            participant_events.append(event)
    return render_template('participant_profile.html', events=events, participant_events=participant_events)

@app.route('/profile/organizer', methods=['GET', 'POST'])
def organizer_profile():
    global events
    if request.method == 'POST':
        new_event = request.form.get('new_event')
        if new_event:
            events.append(new_event)
        delete_event = request.form.get('delete_event')
        if delete_event and delete_event in events:
            events.remove(delete_event)
    return render_template('organizer_profile.html', events=events)

if __name__ == '__main__':
    app.run(debug=True, port=5080)