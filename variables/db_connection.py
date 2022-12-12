from config import dbInfo
from db import CommonDbPool

db_type = dbInfo.get("dbType")
db_config = dbInfo.get(db_type)
db = CommonDbPool(db_type=db_type, db_config=db_config)

if db.is_connection() == False:
    raise Exception(db_type + "  can't  connected")
