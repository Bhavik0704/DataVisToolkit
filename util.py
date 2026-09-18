def validate_columns(df, columns):
    for col in columns:
        if col not in df.columns:
            raise ValueError("Column '" + col + "' not found in CSV.")
