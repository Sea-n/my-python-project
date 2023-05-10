def main():
    print('Connecting to Database...')
    mysql.connect(user=env.DB_USER,
                  password=DB_PASSWORD,
                  host=env.DB_HOST,
                  database=env.DB_DATABASE)


if __name__ == '__main__':
    main()

