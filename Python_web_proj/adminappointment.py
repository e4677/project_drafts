from flask import request, render_template, redirect, url_for, session
from database_connector import DatabaseConnector

def get_data_from_db():
    if 'adminid' not in session:
        return redirect(url_for('admin_route'))

    db_connector = DatabaseConnector()

    try:
        connection = db_connector.get_connection()
        cursor = connection.cursor(dictionary=True)

        # Fetch data from appointment and residentinfo tables
        query = """
        SELECT a.barangayid, r.firstname, r.middlename, r.lastname, a.purpose, a.date, a.status
        FROM appointment a
        JOIN residentinfo r ON a.barangayid = r.barangayid
        """
        cursor.execute(query)
        data = cursor.fetchall()

        return data

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()

def update_appointment_status(barangayid, new_status):
    db_connector = DatabaseConnector()

    try:
        connection = db_connector.get_connection()
        cursor = connection.cursor()

        update_query = "UPDATE appointment SET status = %s WHERE barangayid = %s"
        cursor.execute(update_query, (new_status, barangayid))

        connection.commit()

    except Exception as e:
        print(f"Error: {str(e)}")
        connection.rollback()

    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()

def admin_appointment():
    db_connector = DatabaseConnector()

    if request.method == 'POST':
        barangayid = request.form['barangayid']
        
        if 'approve' in request.form:
            update_appointment_status(barangayid, 'Approved')
        elif 'decline' in request.form:
            update_appointment_status(barangayid, 'Declined')

        return redirect(url_for('adminappointment_route'))

    data = get_data_from_db()
    return render_template("adminappointment.html", data=data)

