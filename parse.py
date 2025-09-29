import os,sys
import xmltodict, json


def parseDetails(raw):
    concat = ""
    if "ConceptDetails" in raw:
        for item in raw["ConceptDetails"]:
            if isinstance(raw["ConceptDetails"][item], list):
                for sub_item in raw["ConceptDetails"][item]:
                    concat += sub_item["LONG_NAME"].strip() + " "
            else:
                concat += raw["ConceptDetails"][item]["LONG_NAME"].strip() + " "
    return concat.strip()


if __name__ == "__main__":
    folder_path = 'cde_xmls/'
    results = {}

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.xml'):
            print("Parsing: " + filename)
            with open(folder_path + filename, "r", encoding="utf-8") as xml_file:
                xml = xml_file.read()
                data = xmltodict.parse(xml)
                for element in data["DataElementsList"]["DataElement"]:
                    dec = element["DATAELEMENTCONCEPT"]
                    results[dec["PublicId"]] = parseDetails(dec["ObjectClass"]) + " " + parseDetails(dec["Property"])
                                          
    with open("cde_concat.json", "w") as file_out:
        file_out.write(json.dumps(results, indent=4))
