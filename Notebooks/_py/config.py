import os
from sqlalchemy import create_engine

class config:
    user = 'postgres'
    password = '1111'
    host = '127.0.0.1'
    port = 5432
    db = 'diabetes'
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}')

    # paths
    path = os.getcwd().replace('\\', '/')
    path = '/'.join(path.split('/')[:-1])
    
    path_data = path+'/data'
    path_submissions = path_data+'/submissions'
    path_data_csv = path_data+'/data_csv'

    target_name = 'diagnosed_diabetes'


    
    