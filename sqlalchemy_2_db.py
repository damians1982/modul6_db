from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')

print(engine.driver)

print(engine.table_names())

print(engine.execute("SELECT * FROM projects"))

results = engine.execute("SELECT * FROM projects")

for r in results:
   print(r)