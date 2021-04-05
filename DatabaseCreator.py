import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost/mydb')

df = pd.read_csv('movies.csv', sep=',').replace(to_replace='null', value=np.NaN)
df.to_sql('Movies', engine)#, schema='schema', if_exists='replace')