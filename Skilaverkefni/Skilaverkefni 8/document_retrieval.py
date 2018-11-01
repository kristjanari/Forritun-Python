import string

def get_filename():
    return input("Document collection: ")

def print_options():
    return ("""
What would you like to do?
1. Search Documents
2. Print Document
3. Quit Program
> """)

def get_text_from_file(filename):
    try:
        with open(filename) as file:
            text_string = file.read()
        return text_string
    except FileNotFoundError:
        print("Documents not found.")

def clean_text(text_string):
    text_string = text_string.replace("\n"," ")
    for punctuation in string.punctuation:
        text_string = text_string.replace(punctuation,"")
    return text_string

def get_documents_list(text_string):
    documents_list = text_string.split("NEW DOCUMENT")
    documents_list.pop(0)
    return documents_list

def create_word_dict(documents_list):
    word_dict = {}
    word_list = []
    for index,value in enumerate(documents_list):
        value = value.lower()
        word_list  = value.split()
        for word in word_list:
            if word in word_dict:
                #index er númer "documents"
                word_dict[word].add(index)
            else:
                word_dict[word] = {index}
    return word_dict

def print_document(documents_list):
    document = int(input("Enter document number: "))
    print("Document #{}".format(document), end = "")
    print(documents_list[document].strip(">").strip("<"), end="")

def search_document(word_dict):
    documents_set = set()
    doc_string = ""
    search_words = input("Enter search words: ").lower()
    search_words = search_words.split()
    for word in search_words:
        if word in word_dict:
            if documents_set == set():
                documents_set= word_dict[word]
            else: 
                documents_set = documents_set.intersection(word_dict[word])
        else:
            return None
    for element in documents_set:
        doc_string = doc_string + str(element) + " "
    return doc_string

def the_loop(documents_list, word_dict):
    choice = "1"
    while choice in {"1","2"}:
        choice = input(print_options())
        if choice == "1":
            searched_documents = search_document(word_dict)
            if searched_documents:
                print("Documents that fit search:", searched_documents)
            else:
                print("No match.")
        elif choice == "2":
            print_document(documents_list)
        else:
            print("Exiting program.")
                    
def main():
    filename  = get_filename()
    text_string = get_text_from_file(filename)
    documents_list = get_documents_list(text_string)
    clean_textstring = clean_text(text_string)
    clean_documents_list = get_documents_list(clean_textstring)
    word_dict = create_word_dict(clean_documents_list)
    the_loop(documents_list,word_dict)

main()