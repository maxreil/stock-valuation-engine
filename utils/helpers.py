def safe_get(dataframe, key):
    """
    Safely retrieve a row from a pandas DataFrame.

    Returns None if the key does not exist.
    """
    try:
        return dataframe.loc[key]
    except Exception:
        return None
