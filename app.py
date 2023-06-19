from ingestion_sql import GenerateData

if __name__ == '__main__':
    print('testing...')
    execute = GenerateData(25)
    execute.generate_data()
