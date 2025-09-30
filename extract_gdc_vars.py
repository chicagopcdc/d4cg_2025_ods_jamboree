import yaml

with open("./source_files/gdc_terms.yaml", "r") as source_gdc:
    gdc = yaml.safe_load(source_gdc)
    with open("./source_files/gdc_terms_out.txt", "w") as out_file:
        for key, value in gdc.items():
            if key != 'id':
                if value['common']['termDef']['source'] == 'caDSR':
                    out_line = (str(value['common']['termDef']['cde_id']) + 
                        "\tLONGNAME:" + str(value['common']['termDef']['term']) + 
                        "|PREFERREDDEFINITION:" + str(value['common']['description']) + 
                        "|DEC_CONCEPTS:"  + str(value['common']['termDef']['term']))
                    print(out_line)
                    out_file.write(out_line + "\n")

            
