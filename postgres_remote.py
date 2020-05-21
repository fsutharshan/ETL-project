# Connects to Postgres hosted on Heroku 
# Connection string - postgres://bknzuntqpziqfq:3bf1e3697ef741a173e13accc818b053c7810ac13c14e56ab50633a9a0411bd6@ec2-54-165-36-134.compute-1.amazonaws.com:5432/dds2f16l3ah56k

import pandas as pd
from sqlalchemy import create_engine,MetaData, Table, Column, Integer, String

#sample data frame only for test
df = pd.DataFrame({"A": [1, None, 2]})
df.columns

conn_str='postgres://bknzuntqpziqfq:3bf1e3697ef741a173e13accc818b053c7810ac13c14e56ab50633a9a0411bd6@ec2-54-165-36-134.compute-1.amazonaws.com:5432/dds2f16l3ah56k'

# from sqlalchemy import create_engine
engine = create_engine(conn_str)

#sample table only for test
df.to_sql('users', if_exists='replace',con=engine)

# Should retrieve the sample data from postgres hosted on Heroku
print(engine.execute("SELECT * FROM users").fetchall())

# Drop world_happiness table if exists throwing errors
#print(engine.execute("DROP TABLE world_happiness IF EXISTS").fetchall())
#print(engine.execute("DROP TABLE world_happiness").fetchall())

meta = MetaData()
# create world_happiness table with two column in the postgres database on Heroku
world_happiness = Table(
   'world_happiness', meta, 
    Column('country', String), 
   Column('score', Integer),
)
meta.create_all(engine)

# read the contents of the sql insert file and feed into execute
fd = open('InsertData.sql', 'r')
sqlFile = fd.read()
fd.close()

print(engine.execute(sqlFile))
#print a list of countries with happiness score greater than 7
print(engine.execute("SELECT * FROM world_happiness where score > 6").fetchall())