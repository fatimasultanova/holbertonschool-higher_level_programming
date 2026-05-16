#!/usr/bin/python3
"""
Sənədləşdirmə (Documentation): Bu modul hbtn_0e_0_usa verilənlər bazasından
bütün ştatları (states) ID ardıcıllığı ilə sıralayıb ekrana çıxarır.
"""
import sys
import MySQLdb


def list_all_states():
    """
    Funksiya Sənədləşdirməsi: Verilənlər bazasına qoşulur və sorğunu icra edir.
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_all_states()
