def find_pro_categorization(strings, keyword):
    categorized_strings = []
    uncategorized_strings = []

    for string in strings:
        if keyword in string:
            categorized_strings.append(string)
        else:
            uncategorized_strings.append(string)

    return categorized_strings, uncategorized_strings


if __name__ == "__main__":
    strings = ["bannana", "apple", "bluyeberry", "strawberry"]
    keyword = "berry"
    categorized_strings, uncategorized_strings = find_pro_categorization(strings, keyword)
    print(categorized_strings, uncategorized_strings)