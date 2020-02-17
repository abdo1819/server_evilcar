import sqlalchemy
import cx_Oracle

host="localhost"
port=1521
sid='xe'
user='abdullah'
password='a'
sid = cx_Oracle.makedsn(host, port, sid=sid)

connection_string = sqlalchemy.engine.url.URL("oracle", user, password, sid)
engine =  sqlalchemy.create_engine(
            connection_string,
            convert_unicode=False,
            pool_recycle=10,
            pool_size=50,
            echo=True
        )

result = engine.execute('select * from TEST')

for row in result:
    print (str(row).split("'")[1])
