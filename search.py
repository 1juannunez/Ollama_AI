import os 
import glob

def  get_documentation():
    doc_path = "/resources/docs"

    #Find all .txt files in the directory
    files = glob.glob(os.path.join(doc_path, "*.txt"))

    #Display the found documents
    if files:
        print("Found documents:")
        for file in files:
            print(file)
        else:
            print("No documents found.")
def generate_outcome_answer2(answer):
    """
        Documentation Search
    """
    while True:
        print("\nWelcome to your Search AI Assitance!")
        print("")