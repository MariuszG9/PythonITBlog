def delete_duplicates_and_nulls():
    for var in globals():
        if isinstance(globals()[var], pd.DataFrame):
            df = globals()[var].drop_duplicates()
            df = df.dropna()
            new_df_name = 'new_' + var
            globals()[new_df_name] = df
            print(f"Utworzono ramkę danych {new_df_name}:\n{df}\n")
