import chromadb
import json
import argparse

def create_chroma_collection(persistent_dir, coll_name, infile):

    chroma_client = chromadb.PersistentClient(persistent_dir)

    collection = chroma_client.get_or_create_collection(
        name=coll_name,
        configuration={
            "hnsw": {
                "space": "cosine",
                "ef_construction": 200
            }
        }
    )

    with open(infile, "r") as json_file:
        data = json.load(json_file)
        i=1
        for key, value in data.items():
            print(i)
            i+=1
            collection.upsert(
                ids=[key],
                documents=[value]
            )

def main():
    parser = argparse.ArgumentParser(description="A script to create embeddings of CDEs and insert into a ChromaDB instance.")
    parser.add_argument("-d", "--persistent_dir", type=str, default="./chroma_db_cde", help="The directory where the persistent db should be stored.")
    parser.add_argument("-c", "--coll_name", type=str, default="cadsr_cde", help="The name of the chromadb collection to write.")
    parser.add_argument("-i", "--infile", type=str, default="cadsr_full_dec-concat.json", help="The input file to use for the embeddings.")
    
    args = parser.parse_args()
    create_chroma_collection(args.persistent_dir, args.coll_name, args.infile)

if __name__ == "__main__":
    main()