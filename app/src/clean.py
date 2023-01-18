import pandas as pd
import numpy as np
from pathlib import Path

amazon = pd.read_csv('app/Datasets/amazon_prime_titles-score.csv')
disney = pd.read_csv('app/Datasets/disney_plus_titles-score.csv')
hulu = pd.read_csv('app/Datasets/hulu_titles-score (2).csv')
netflix = pd.read_csv('app/Datasets/netflix_titles-score.csv')

data_dictionary = {
    'amazon': amazon,
    'disney': disney,
    'hulu': hulu,
    'netflix': netflix
}

#------------#
# Consigna 1:
#------------#
def generate_id_show(dict_data):
    for df_name , df in zip(dict_data.keys(), dict_data.values()):
        df['show_id'] = df_name[0] + df['show_id']
        dict_data[df_name] = df    
    return dict_data
# print(data_dictionary['amazon'])

#------------#
# Consigna 2:
#------------#
def fillna_initial_df_name(dict_data):
    for df_name,df in  zip(dict_data.keys(),dict_data.values()):
        df['rating'] = df['rating'].fillna('g')
        dict_data[df_name] = df
    return dict_data
# print(data_dictionary['amazon']['rating'].unique())

#------------#
# Consigna 3:
#------------#
def change_date_added_datetime(dict_data):
    for df_name, df in zip(dict_data.keys(), dict_data.values()):
        df['date_added'] = pd.to_datetime(df['date_added'].str.strip(),  format='%B %d, %Y').dt.strftime('%Y-%m-%d')
        dict_data[df_name] = df
    return dict_data
# print(data_dictionary['amazon']['date_added'].unique())

#------------#
# Consigna 4:
#------------#
def convert_to_lower(dict_data):
    for df_name, df in zip(dict_data.keys(), dict_data.values()):
        object_columns_list= df.dtypes[df.dtypes == 'object'].index.to_list()
        for col in object_columns_list:
            df[col] = df[col].str.lower()
        dict_data[df_name] = df
    return dict_data
# print(data_dictionary['amazon'].iloc[1:2])

#------------#
# Consigna 5:
#------------#
def normalize_duration(dict_data):
    for df_name, df in zip(dict_data.keys(), dict_data.values()):    
        df[['duration_int', 'duration_type']] = df['duration'].str.split(' ', expand=True)
        df['duration_type'] = df['duration_type'].str.replace('seasons', 'season')
        df['duration_int'] = pd.to_numeric(df['duration_int'], downcast='integer', errors='coerce')
        # df['duration_int'] = df['duration_int'].astype(int)
        dict_data[df_name] = df
    return dict_data
# print(data_dictionary['amazon'].iloc[:2])

#-----------------------------#
# Concatenación de DataFrames
#-----------------------------#
def concat_dataframes(dict_data):
    movies = pd.concat([dict_data['amazon'], dict_data['disney'], dict_data['hulu'], dict_data['netflix']],axis=0)
    return movies
# print(movies_scores_df['show_id'].str[0].unique())

#--------------------------------------#
# Reordenar las columnas del dataframe
#--------------------------------------#
def reorder_cols(df):
    reordered_cols = ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added','release_year', 'rating', 'duration', 'duration_int', 'duration_type', 'listed_in', 'description','score']
    df = df[reordered_cols]
    return df
# print(movies_scores_df.iloc[3:1].columns)

#-----------------------#
# Exportaciónde la data
#-----------------------#
def save_as_json(df):
    # path_file = Path('app/src/db/movies_scores.json')
    # df_json = df.to_json(orient='records')
    # Exportar a JSON: convierte el DataFrame a JSON con orientación 'records' (lista de diccionarios)
    df_json = df.to_json(orient='records')
    # Guarda el JSON en un archivo .json
    with open('app/src/db/movies_scores.json','w') as file:
        file.write(df_json)

if __name__ == '__main__':
    # Consigna 1:
    data_dictionary = generate_id_show(data_dictionary)
    # Consigna 2:
    data_dictionary = fillna_initial_df_name(data_dictionary)
    # Consigna 3:
    data_dictionary = change_date_added_datetime(data_dictionary)
    # Consigna 4:
    data_dictionary = convert_to_lower(data_dictionary)
    # Consigna 5:
    data_dictionary = normalize_duration(data_dictionary)
    # Concatenación de dataframes
    movies_scores_df = concat_dataframes(data_dictionary)
    # Reordenar columnas
    movies_scores_df = reorder_cols(movies_scores_df)
    # Guardar la data json en un archivo
    save_as_json(movies_scores_df)
    print('Se ha limpiado correctamente los datasets.')