def main():

    unique = [" ", " "]

    text = "Hello, World! "
    unique_text = ""
    word_number = 0

    for letter in text:

        if letter != " ":
            unique_text = unique_text + letter
        else:
            unique[word_number] = unique_text
            word_number = word_number + 1
            unique_text = ""

    print(unique)


main()
