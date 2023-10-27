import cherrypy
import psycopg2

# NOTE: MODIFY THE FILE secrets.template.py
from reco_secrets import DATABASE, USER, PASS


class UserItemsAPI:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_items(self, userID):
        conn = psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASS,
            host="localhost",
            port="5432",
        )
        cur = conn.cursor()

        select_query = "SELECT itemID FROM user_items WHERE userID = %s;"
        cur.execute(select_query, (userID,))
        result = cur.fetchall()

        conn.close()

        # Convert the result to a list of dictionaries
        item_ids = [row[0] for row in result]

        return {"itemIDs": item_ids}


if __name__ == "__main__":
    cherrypy.quickstart(UserItemsAPI())
