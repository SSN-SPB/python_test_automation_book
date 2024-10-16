import re

# Define if the string contains at least one Upper case letter
# followed by Lower case letters. E.g. '75serS3' - False; '75WseTrS3' - True;

regex_one = "[A-Z][a-z]"
string_one = "7865serS3"
string_two = "7865sers3"
string_three = "78S65UserU3"


def is_capital_and_not_capital_in_string(regex_string, test_string):
    pattern = re.compile(regex_string)
    result = re.findall(pattern, test_string)
    return len(result)


def main():
    print(is_capital_and_not_capital_in_string(regex_one, string_one))
    print(is_capital_and_not_capital_in_string(regex_one, string_two))
    print(is_capital_and_not_capital_in_string(regex_one, string_three))
    assert is_capital_and_not_capital_in_string(regex_one, string_one) == 0
    assert is_capital_and_not_capital_in_string(regex_one, string_two) == 0
    assert is_capital_and_not_capital_in_string(regex_one, string_three) == 1


if __name__ == "__main__":
    main()
