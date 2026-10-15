"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

conn_params = {
    "host": "localhost",
    "database": "north",
    "user": "postgres",
    "password": "kotakbas228",  #или KOTAKBAS228    
    "port": "5432"
}


def fill_customers(cursor):
    with open('north_data/customers_data.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cursor.execute(
                "INSERT INTO customers VALUES (%s, %s, %s)",
                row
            )


def fill_employees(cursor):
    with open('north_data/employees_data.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cursor.execute(
                "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                row
            )


def fill_orders(cursor):
    with open('north_data/orders_data.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cursor.execute(
                "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                row
            )


def main():
    try:
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cur:
                fill_customers(cur)
                fill_employees(cur)
                fill_orders(cur)
                conn.commit()
                print("Data loaded successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == '__main__':
    main()