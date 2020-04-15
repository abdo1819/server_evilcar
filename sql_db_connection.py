import sqlalchemy
import cx_Oracle

def create_engine(database_type,host,port,sid,user,password):

    sid = cx_Oracle.makedsn(host, port, sid=sid)

    connection_string = sqlalchemy.engine.url.URL(database_type, user, password, sid)
    engine =  sqlalchemy.create_engine(
                connection_string,
                convert_unicode=False,
                pool_recycle=10,
                pool_size=50,
                echo=True
            )
    return engine
