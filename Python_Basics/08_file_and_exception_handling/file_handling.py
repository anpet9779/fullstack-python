# file = open("order.txt", "w")
# try:
#     file.write("Order for 4 cups of masala chai")
# except Exception as e:
#     print(e)
# finally:
#     file.close()


# --------------------------------------

#'with' is the new and modern way of file handling

with open("order.txt", "w") as file:
    file.write("Order for 4 cups of masala chai")