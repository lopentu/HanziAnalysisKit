import yaml

def meta2yaml(filename: str, metadata: dict, is_time_meta: bool = False):
    payload = {}
    if is_time_meta:
        payload['default_flow_style'] = None
    else:
        payload['Dumper'] = yaml.CDumper

    try:
        with open(filename, "w") as f:
            yaml.dump(metadata, f, allow_unicode=True, **payload)
    except Exception as error:
        raise Exception(f"File creation error: {error}")
