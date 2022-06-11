from math import sqrt
from prettytable import PrettyTable

example_string = input("Please input data divided by space: ")
example_array = example_string.split(" ")
example_array = [int(x) for x in example_array]


sorted_array = sorted(set(example_array))


seen = []
items_sum = 0
xifi_sum = 0
xixifi_sum = 0

# Checking frequency
for item in sorted_array:

    current_item_count = 0
    # Iterate over original string
    for original_item in example_array:

        if item == original_item:
            current_item_count += 1

    if not current_item_count == 0:
        new_item = {"xi": item, "fi": current_item_count}
        seen.append(new_item)


table = PrettyTable(["Xi", "Fi", "XiFi", "Xi^2 * Fi"])

for item in seen:

    # Calculate cols
    xi_row = item['xi']
    fi_row = item['fi']
    xifi_row = item["xi"] * item['fi']
    xixifi_row = item["xi"] * item['xi'] * item['fi']

    # calculate sums
    items_sum += fi_row
    xifi_sum += xifi_row
    xixifi_sum += xixifi_row

    # Add to table
    table.add_row([xi_row, fi_row, xifi_row, xixifi_row])

table.add_row(["SUM", items_sum, xifi_sum, xixifi_sum])


def caclulate_xn(xifi, n):
    return round(xifi / n, 2)


def calculate_sn(xixifi, Xn, n):
    snsqr = round((xixifi / n) - (Xn * Xn), 2)
    sn = sqrt(snsqr)

    return round(sn, 2)


def calculate_probability(Xn, Sn, n, Z):

    lower_border = (Xn - (Z * (Sn / sqrt((n - 1)))))
    upper_border = Xn + (Z * (Sn / sqrt((n - 1))))

    return [round(lower_border, 2), round(upper_border, 2)]


print(table)

xn = caclulate_xn(xifi_sum, items_sum)
sn = calculate_sn(xixifi_sum, xn, items_sum)

print(xn)
print(sn)

prob = calculate_probability(xn, sn, items_sum, 2.575)


print(f"Probability is [{prob[0]};{prob[1]}] with 99% chance")
