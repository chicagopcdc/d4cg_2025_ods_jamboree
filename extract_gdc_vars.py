import yaml

with open("./source_files/gdc_terms.yaml", "r") as source_gdc:
    gdc = yaml.safe_load(source_gdc)

print("1. All top-level keys:")
for key, value in gdc.items():
    if key != 'id':
        if value['common']['termDef']['source'] == 'caDSR':
            print(f"{key}")
            print(value['common']['description'])
            print(value['common']['termDef']['term'])
            print(value['common']['termDef']['cde_id'])
            print()
