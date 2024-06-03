def number_of():
    letters_dict = {}

    with open("books/frankenstein.txt") as f:
        content = f.read()
        lowered_content = content.lower()
        word_list = content.split()
        word_count = len(word_list)
        
        #print(content)
        

        for chars in lowered_content:
            if chars.isalpha():
                if chars in letters_dict:
                    letters_dict[chars] += 1
                else:
                    letters_dict[chars] = 1

        sorted_characters = [{"char": k, "count": v} for k, v in letters_dict.items()]
        sorted_characters.sort(key=lambda x: x["count"], reverse=True)



        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found int he document")
        for item in sorted_characters:
            print(f"The '{item['char']}' character was found {item['count']} times.")
        print("--- End report ---")

if __name__ == "__main__":
    number_of()
