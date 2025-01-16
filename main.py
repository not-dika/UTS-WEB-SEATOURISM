from flask import Flask, redirect, render_template, request, jsonify, url_for
from mysqli import MySQLInterface

app = Flask(__name__)
db = MySQLInterface("localhost", "root", "", "seatourism")

@app.route("/")
def root():
    query = "SELECT * FROM destination_highlights"
    destinations = db.fetch_all(query)
    return render_template('index.html', destinations=destinations)

@app.route('/bookings', methods=['POST'])
def handle_booking():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    destination = data.get('destination')
    additional = data.get('additional')
    query = """
    INSERT INTO bookings (full_name, email, destination, additional_requirement)
    VALUES (%s, %s, %s, %s)
    """
    db.execute_query(query, (name, email, destination, additional))
    return jsonify({'message': 'Booking received!'}), 200

@app.route('/admin')
def index():
    query = "SELECT * FROM destination_highlights"
    highlights = db.fetch_all(query)
    return render_template('admin.html', highlights=highlights)

@app.route('/admin/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        destination = request.form['destination']
        best_time_to_visit = request.form['best_time_to_visit']
        avg_temperature = request.form['avg_temperature']
        must_visit_attractions = request.form['must_visit_attractions']
        avg_daily_budget = request.form['avg_daily_budget']

        query = """
            INSERT INTO destination_highlights (destination, best_time_to_visit, avg_temperature, must_visit_attractions, avg_daily_budget)
            VALUES (%s, %s, %s, %s, %s)
        """
        db.execute_query(query, (destination, best_time_to_visit, avg_temperature, must_visit_attractions, avg_daily_budget))
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/admin/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        destination = request.form['destination']
        best_time_to_visit = request.form['best_time_to_visit']
        avg_temperature = request.form['avg_temperature']
        must_visit_attractions = request.form['must_visit_attractions']
        avg_daily_budget = request.form['avg_daily_budget']
        query = """
            UPDATE destination_highlights
            SET destination = %s, best_time_to_visit = %s, avg_temperature = %s, must_visit_attractions = %s, avg_daily_budget = %s
            WHERE id = %s
        """
        db.execute_query(query, (destination, best_time_to_visit, avg_temperature, must_visit_attractions, avg_daily_budget, id))
        return redirect(url_for('index'))
    
    query = "SELECT * FROM destination_highlights WHERE id = %s"
    highlight = db.fetch_one(query, (id,))
    return render_template('edit.html', highlight=highlight)

@app.route('/admin/delete/<int:id>', methods=['GET'])
def delete(id):
    query = "DELETE FROM destination_highlights WHERE id = %s"
    db.execute_query(query, (id,))
    return redirect(url_for('index'))

@app.route('/admin/bookings')
def bookings():
    query = "SELECT * FROM bookings"
    bookings_data = db.fetch_all(query)
    return render_template('bookings.html', bookings=bookings_data)

@app.route('/admin/bookings/delete/<int:id>', methods=['GET'])
def delete_booking(id):
    query = "DELETE FROM bookings WHERE id = %s"
    db.execute_query(query, (id,))
    return redirect(url_for('bookings'))

if __name__ == "__main__":
    app.run()