import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="aditi0306",  # Replace with your MySQL password
    database="PROJECT"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Function to create the alarms table
def create_alarms_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS alarms
                     (id INT AUTO_INCREMENT PRIMARY KEY,
                     alarm_time TIME,
                     recurring BOOLEAN,
                     sunday BOOLEAN,
                     monday BOOLEAN,
                     tuesday BOOLEAN,
                     wednesday BOOLEAN,
                     thursday BOOLEAN,
                     friday BOOLEAN,
                     saturday BOOLEAN)''')
    db.commit()

# Function to save alarm data to MySQL database
def save_alarm_to_db(alarm_time, recurring_days):
    query = "INSERT INTO alarms (alarm_time, recurring, sunday, monday, tuesday, wednesday, thursday, friday, saturday) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (alarm_time, True if recurring_days else False, 'Sunday' in recurring_days, 'Monday' in recurring_days, 'Tuesday' in recurring_days, 'Wednesday' in recurring_days, 'Thursday' in recurring_days, 'Friday' in recurring_days, 'Saturday' in recurring_days))
    db.commit()

# Function to retrieve alarm data from MySQL database
def get_alarms_from_db():
    cursor.execute("SELECT * FROM alarms")
    alarms = cursor.fetchall()
    formatted_alarms = []
    for alarm in alarms:
        formatted_alarm = list(alarm)
        formatted_alarm[1] = str(formatted_alarm[1])  # Convert timedelta to string
        formatted_alarms.append(formatted_alarm)
    return formatted_alarms

# Close cursor and database connection
def close_connection():
    cursor.close()
    db.close()

if __name__ == "__main__":
    # This part will execute if the script is run directly
    create_alarms_table()