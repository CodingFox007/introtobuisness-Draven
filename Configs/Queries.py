from Configs.DbConnections import *

def retrieve_names():
    names = []
    try:
        with engine.connect() as conn:
            result = conn.execute(text('select * from places'))
            for i in result:
                names.append(i[1])
    except Exception as e:
        print(f"There was an issue with executing the following command: {e}")

    return names