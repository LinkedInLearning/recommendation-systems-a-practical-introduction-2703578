from flask import Flask, request, jsonify
import psycopg2

# NOTE: MODIFY THE FILE secrets.template.py
from reco_secrets import DATABASE, USER, PASS


app = Flask(__name)


def get_recommendations(user_id):
    conn = psycopg2.connect(
        database=DATABASE,
        user=USER,
        password=PASS,
        host="localhost",
        port="5432",
    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM recommendations WHERE user_id = %s", (user_id,))
    row = cur.fetchone()
    
    cur.close()
    conn.close()
    
    if row is None:
        return None
    else:
        columns = [desc[0] for desc in cur.description]
        recommendation_data = dict(zip(columns, row))
        del recommendation_data['user_id']  # Remove the 'user_id' from the result
        return recommendation_data


@app.route('/recommendations', methods=['POST'])
def recommend_items():
    data = request.get_json()

    if data is None or 'user_id' not in data:
        return jsonify({'error': 'Invalid request data'}), 400

    user_id = data['user_id']
    recommendations = get_recommendations(user_id)
    
    if recommendations is None:
        return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify(recommendations)
    

if __name__ == '__main__':
    app.run(debug=True)