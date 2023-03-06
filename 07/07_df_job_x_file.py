def delete_duplicates():
    for var in globals():
        if isinstance(globals()[var], pd.DataFrame):
            print(f'Przetwarzanie ramki {var}...')
            df = globals()[var]
            df = df.drop_duplicates()
            new_file = f"new_{var}.csv"
            df.to_csv(new_file, index=False)
            print(f'Zapisano ramkę bez duplikatów do pliku: {new_file}.\n')
