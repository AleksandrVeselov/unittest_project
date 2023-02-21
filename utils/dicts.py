def get_val(collection, key, default='git'):
    if isinstance(collection, dict):
        return collection.get(key, default)

    else:
        return default
