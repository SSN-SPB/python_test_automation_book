# Print out all words with length of n-characters


def print_words_with_length_n_from_file(source_file, required_length):
    file_name = open(source_file, "r")
    for line in file_name:
        for word in line.strip().split(" "):
            if len(word) == required_length:
                print(word)
    file_name.close()


def main():
    print_words_with_length_n_from_file("init_file_3_1.txt", 2)


if __name__ == "__main__":
    main()
