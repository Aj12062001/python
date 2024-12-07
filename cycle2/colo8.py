colors = input("Enter colors seperated by a comma: ")
colors = [color.strip() for color in colors.split(",")]
print("First color = {}, last color = {}".format(colors[0], colors[-1]))
