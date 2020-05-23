# Connects to Postgres hosted on Heroku 
# Connection string - postgres://bknzuntqpziqfq:3bf1e3697ef741a173e13accc818b053c7810ac13c14e56ab50633a9a0411bd6@ec2-54-165-36-134.compute-1.amazonaws.com:5432/dds2f16l3ah56k

import pandas as pd
from sqlalchemy import create_engine,MetaData, Table, Column, Integer, String
import os

#sample data frame only for test
df = pd.DataFrame({"A": [1, None, 2]})
df.columns

#Old connection string does not work after the database maintenance
#conn_str='postgres://bknzuntqpziqfq:3bf1e3697ef741a173e13accc818b053c7810ac13c14e56ab50633a9a0411bd6@ec2-54-165-36-134.compute-1.amazonaws.com:5432/dds2f16l3ah56k'

#Had to generate a new one
conn_str='postgres://wogqdccobpqsto:762414ccac8b002d6289c26031901c9ab6234cd970ae7365e56a2c5d9c9024ec@ec2-34-232-147-86.compute-1.amazonaws.com:5432/db81ga2lvphmh1'

# # from sqlalchemy import create_engine
engine = create_engine(conn_str)

# #sample table only for test
# df.to_sql('users', if_exists='replace',con=engine)

# # Should retrieve the sample data from postgres hosted on Heroku
# print(engine.execute("SELECT * FROM users").fetchall())


meta = MetaData()
# create world_happiness table with two column in the postgres database on Heroku
# world_happiness = Table(
#    'world_happiness', meta, 
#     Column('country', String), 
#    Column('score', Integer),
# )
meta.drop_all(engine)
# meta.create_all(engine)



# # read the contents of the sql insert file and feed into execute
# fd = open('InsertData.sql', 'r')
# sqlFile = fd.read()
# fd.close()

# engine.execute("Delete from world_happiness")
# print(engine.execute(sqlFile))
# #print a list of countries with happiness score greater than 7
# print(engine.execute("SELECT * FROM world_happiness where score > 6").fetchall())


# Caribbean Data
# read the contents of the sql insert file and feed into execute
# fd = open('columnnames.sql', 'r')
# createtable_sql = fd.read()
# fd.close()
# sql_create_table_query = "create table Caribbean(" +createtable_sql
# print(sql_create_table_query)

# #insert data 
# fd = open('regiontables/Caribbean.sql', 'r')
# insertdata_Caribbean_sql = fd.read()
# fd.close()

# print(engine.execute(sql_create_table_query))
# print(engine.execute(insertdata_Caribbean_sql))


# print(engine.execute("SELECT COLUMN_NAME, DATA_TYPE FROM information_schema.COLUMNS WHERE TABLE_NAME = 'Caribbean';"))

# print(engine.execute("SELECT * FROM Caribbean").fetchall())


fd = open('columnnames.sql', 'r')
createtable_sql = fd.read()
fd.close()

for filename in os.listdir('regiontables'):
    if  filename.endswith(".sql"): 
        region_tablename =filename.split('.')[0]

        
        sql_create_table_query = "create table "+region_tablename+"(" +createtable_sql
        #print(sql_create_table_query)

        #insert table data
        f=open(os.path.join('regiontables',filename),'r')
        insertdata_sql = f.read()
        
        print(insertdata_sql)
        print('------------------------')

        print(engine.execute(sql_create_table_query))
        print(engine.execute(insertdata_sql))
      
        continue
    else:
        continue
        
