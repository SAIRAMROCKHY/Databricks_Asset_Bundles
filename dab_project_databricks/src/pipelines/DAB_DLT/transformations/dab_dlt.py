import dlt

@dlt.table(
    name = 'dab_source'
)

def dab_source():
    df = spark.range(10)
    return df