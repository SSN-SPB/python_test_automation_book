# Read the file and remove equal lines (if any).


def remove_all_similar_lines_from_file(source_file, target_file):
    file_name = open(source_file, "r")
    file_name_modified = open(target_file, "w+")
    # data = file_name.read()
    test_list = []
    # print(data)
    for line in file_name:
        print(line)
        if line not in test_list:
            test_list.append(line)
            file_name_modified.write(line)
    file_name.close()
    file_name_modified.close()


def main():
    remove_all_similar_lines_from_file("init_file_3_1.txt", "out_file_3_1.txt")


if __name__ == "__main__":
    main()
