def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- BEGIN REPORT OF BOOKS/FRANKENSTEIN.TXT ---\n");
    print(f"The word count of the selected book is : {wordCount(text)}\n")
    print(f"{printReport(characterSorter(characterOccurence(text)))}")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def wordCount(book_text: str):
    return len(book_text.split())

def characterOccurence(book_text: str):
    my_dict = {}
    for character in book_text.lower():
        if character not in my_dict:
            my_dict[character] = 1
        else:
            my_dict[character] += 1
    return my_dict

def sort_on(dict):
    return dict["num"]

def dict_to_list(dict : dict):
    return dict.sort()

def characterSorter(dict: dict):
    list_of_dict = []
    for char, count in dict.items():
        if char.isalpha():
            new_dict = {"char" : char, "num": count}
            list_of_dict.append(new_dict)
    list_of_dict.sort(reverse=True,key= sort_on)
    return list_of_dict

def printReport(sorted_list: list):
    for item in sorted_list:
        char = item["char"]
        count = item["num"]
        print(f"The '{char}' character was found {count} times" )

main()