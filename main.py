def main():
    print('Connecting to Database...')
    conn = mysql.connect(user=env.DB_USER,
                         password=DB_PASSWORD,
                         host=env.DB_HOST,
                         database=env.DB_DATABASE)
    conn.query('SELECT * FROM data LIMIT 5')
    conn.query("INSERT data VALUES ('name', ':value')", data={'value': 'Sean'})


if __name__ == '__main__':
    main()

