# Connects to Postgres hosted on Heroku 
# Connection string - postgres://bknzuntqpziqfq:3bf1e3697ef741a173e13accc818b053c7810ac13c14e56ab50633a9a0411bd6@ec2-54-165-36-134.compute-1.amazonaws.com:5432/dds2f16l3ah56k

import pandas as pd
from sqlalchemy import create_engine

df = pd.DataFrame({"A": [1, None, 2]})
df.columns

conn_str='postgres://bknzuntqpziqfq:3bf1e3697ef741a173e13accc818b053c7810ac13c14e56ab50633a9a0411bd6@ec2-54-165-36-134.compute-1.amazonaws.com:5432/dds2f16l3ah56k'

# from sqlalchemy import create_engine
engine = create_engine(conn_str)

df.to_sql('users', if_exists='replace',con=engine)

# Should retrieve the data from postgres hosted on Heroku
print(engine.execute("SELECT * FROM users").fetchall())

