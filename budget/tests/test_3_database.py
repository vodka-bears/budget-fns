#!/usr/bin/env python3

from scan import scan_code, parse_code
from receipt_orm import Entry, Receipt
from settings import get_config_file
import peewee
import default
import receipt_orm
    
db = peewee.SqliteDatabase(
    get_config_file()["Basic"]["Database"]
)
receipt_orm.proxy.initialize(db)
db.connect()
peewee.create_model_tables([Receipt, Entry])
for i in range(2):
    q = parse_code(scan_code("/dev/video0", (640,480)))
    if q.verify():
        print("OK")
    r = q.get(default.login, default.password)
    print(r._meta.database.database)
    r.save()
print(db.get_tables())

for i in range(2):
    print()