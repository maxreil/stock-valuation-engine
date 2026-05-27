def safe_get(series, key):
    try:
        return series.loc[key]
    except Exception:
        return None
