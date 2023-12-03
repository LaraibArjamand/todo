import yaml

def yaml_coerce(value):
    # Convert value to proper python
    if isinstance(value, str):
        # converts string dict to actual python dicts
        return yaml.load(f"dummy: {value}", Loader=yaml.SafeLoader)["dummy"]
    return value