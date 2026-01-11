import json
import os
import psycopg2
from psycopg2.extras import RealDictCursor


def lambda_handler(event, context):
    conn = None
    sql = event["body"] 

    try:

        conn = psycopg2.connect(
            host=os.environ["PG_HOST"],
            port=int(os.environ.get("PG_PORT", 5432)),
            dbname=os.environ["PG_DBNAME"],
            user=os.environ["PG_USER"],
            password=os.environ["PG_PASSWORD"],
            connect_timeout=5,
        )
        results = []
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql)
            if cur.description:
                rows = cur.fetchall()
                results = rows

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "count": len(results),
                "tables": results
            })
        }

    except Exception as e:
        print("Error listing table:", e)
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": "Failed to list tables",
                "details": "error"
            })
        }

    finally:
        if conn:
            conn.close()
