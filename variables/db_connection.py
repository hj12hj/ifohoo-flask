from config import dbInfo
from db import CommonDbPool
from registry import config

if   config is  None:

    db_type = dbInfo.get("dbType")

    print("db_type is " + db_type)

    db_config = dbInfo.get(db_type)
else:
    dbType = config.get("dbInfo").get("dbType")
    db_config = config.get("dbInfo").get(dbType)

print("db_config_is ---->>>>  " + str(db_config))

db = CommonDbPool(db_type=db_type, db_config=db_config)

if db.is_connection() == False:
    raise Exception(db_type + "  can't  connected")
