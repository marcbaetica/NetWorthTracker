import json


def parse_portofolio_from_file(file):
    with open(file, 'r') as f:
        portofolio = json.loads(f.read())
    print(f'Extracting protofolio information dating [{portofolio["date"]}].\n')
    return portofolio["assets"], portofolio["liabilities"], portofolio["date"]
