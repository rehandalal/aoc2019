def get_input_data(fn):
    with open(f'input/{fn}') as f:
        raw = f.read()
    return [v for v in raw.split('\n') if v != '']


def get_input_data_comma_separated(fn):
    with open(f'input/{fn}') as f:
        raw = f.read()
    return raw.strip('\n').split(',')
