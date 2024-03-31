from flask import Flask, render_template, request, jsonify
from threading import Thread
import datetime as dt
import time
from database import save_alarm_to_db, get_alarms_from_db

app = Flask(__name__)

# Function to handle the alarm
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = dt.datetime.now()
        current_time = actual_time.strftime("%H:%M:%S")
        print("Current Time:", current_time)
        if current_time == set_alarm_timer:
            print("Alarm!")
            break

# Route to handle setting alarms
@app.route('/set-alarm', methods=['POST'])
def set_alarm():
    try:
        alarm_time = request.form['alarm_time']
        recurring_days = request.form.getlist('recurring_days[]')
        save_alarm_to_db(alarm_time, recurring_days)
        # Return a JSON response indicating success
        return jsonify({'message': 'Alarm saved successfully'}), 200
    except Exception as e:
        # Log the exception for debugging purposes
        print("An error occurred while saving the alarm:", str(e))
        # Return a JSON response with the error message
        return jsonify({'error': 'Error occurred while saving the alarm. Please try again later.'}), 500

# Route to render the HTML interface with alarm data
@app.route('/')
def index():
    alarms = get_alarms_from_db()
    return render_template('alarm.html', alarms=alarms)

if __name__ == '__main__':
    # Create alarms table if not exists
    from database import create_alarms_table
    create_alarms_table()
    app.run(debug=False)
