from datetime import datetime, timedelta
import random
import socket
import time
import os

if __name__ == "__main__":
    started_at = datetime.utcnow()
    postgres_host = os.environ.get("POSTGRES_HOST", "postgres")
    postgres_port = os.environ.get("POSTGRES_PORT", 5432)
    while datetime.utcnow() < started_at + timedelta(minutes=5):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((postgres_host, postgres_port))
                print("Postgres had started")
                break
        except socket.error:
            print("Waiting for postgres")
            time.sleep(0.5 + (random.randint(0, 100) / 1000))
