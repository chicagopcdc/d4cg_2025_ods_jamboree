import chromadb
import csv
import argparse


def get_until_alpha_loop(s):
    result = ""
    for char in s:
        if char.isalpha():
            break
        result += char
    return result

def chroma_lookup(infile, outfile, num_matches):
    # chroma_client = chromadb.PersistentClient("./chroma_db_c3dc_cde")
    # collection = chroma_client.get_collection(name="cadsr_c3dc_cde")

    chroma_client = chromadb.PersistentClient("./chroma_db_extended_cde")
    collection = chroma_client.get_collection(name="cadsr_extended_cde")

    with open(infile, "r") as source_dd:
        with open(outfile, "w") as out_dd:
            tsv_reader = csv.reader(source_dd, delimiter='\t')
            hdr = "src_cde_id\t"
            for i in range(num_matches):
                hdr += "match_cde_id_" + str(i+1) + "\t"
            for i in range(num_matches):
                hdr += "match_cde_concept_text_" + str(i+1) + "\t"
            for i in range(num_matches):
                hdr += "match_distance_" + str(i+1) + "\t"
            out_dd.write(hdr + "match_position\tis_match\n")
            for row in tsv_reader:
                print(str(row[0]) + ": " + str(row[1]))
                src_cde_id = get_until_alpha_loop(str(row[0]))
                matched_position = -1
                results = collection.query(
                    query_texts=[row[1]],
                    n_results=num_matches
                )
                out_dd.write(src_cde_id + "\t")
                for key, value in results.items():
                    if key == "ids":
                        for id in value[0]:
                            out_dd.write(str(id) + "\t")
                            if str(id) == src_cde_id:
                                matched_position = value[0].index(id)
                    if key == "documents":
                        for doc in value[0]:
                            out_dd.write(str(doc) + "\t")
                    if key == "distances":
                        for dist in value[0]:
                            out_dd.write(str(dist) + "\t")
                out_dd.write(str(matched_position+1)+"\t")
                if matched_position > -1:
                    out_dd.write("1")
                else:
                    out_dd.write("0")
                out_dd.write("\n")


def main():
    parser = argparse.ArgumentParser(description="A script to lookup matching CDEs from a ChromaDB instance.")
    parser.add_argument("-i", "--infile", type=str, default="", help="The input file to process.")
    parser.add_argument("-o", "--outfile", type=str, default="", help="The output file to write.")
    parser.add_argument("-n", "--num_matches", type=int, default=10, help="The number of CDEs to match.")
    
    args = parser.parse_args()
    chroma_lookup(args.infile, args.outfile, args.num_matches)

if __name__ == "__main__":
    main()