from sqlalchemy import create_engine, text
from collections import OrderedDict
db_connection = "mysql+pymysql://6soqlhydxpnoaugs0ldc:pscale_pw_fnkwaPKPqxtKeu1puM61zYD0L1QQG7KA7P3RKFC5VTB@aws.connect.psdb.cloud/techtalkposts?charset=utf8mb4"


engine = create_engine(
    db_connection,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
    )

with engine.connect() as conn:
    result = conn.execute(text("select * from posts"))
    print(type(result))
    result_all = result.all()
    print(OrderedDict(result_all))
    print(type(result_all))
    first_result = result_all[0]
    print(type(first_result))
    print(first_result)
