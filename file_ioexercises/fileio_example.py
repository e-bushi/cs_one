def count_total_money():
    with open("sales_data.txt") as f:
        sales_data = list(f.readlines())
    total = 0.0
    for item in sales_data:
        spliced = item.split("\t")

        for value in spliced:
            if "." in value:

                if "\n" in value:
                    string_num = ""
                    for v in value:
                        if v != "\n" and v != "$":
                            string_num += v

                    total += float(string_num)

    print(total)

def clean_data():
    with open("sales_data.txt") as f:
        sales_data = list(f.readlines())
    total = 0.0
    for item in sales_data:
        spliced = item.split("\n")

    for item in spliced:
        spliced.remove("")

    print(spliced)


clean_data()
# def more_pythonic_total():
#     with open("sales_data.txt") as f:
#         sales_data = list(f.readlines())
#     total = sum([i[3] for i in sales_data])


# count_total_money()
# more_pythonic_total()
