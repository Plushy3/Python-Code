import csv
import turtle


def read_data():
    data = []
    with open(r'''C:\Users\susan\PycharmProjects\pythonProject1\cfg-python\data\sales.csv''', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data


data = read_data()
sales = []
expenditure = []
month = []

lowest_sales = highest_sales = 0
low_sales_month = " "
high_sales_month = " "

lowest_expenditure = highest_expenditure = 0
low_exp_month = " "
high_exp_month = " "


def graph_print_one_bar(divide):
    # Fill Colour Inside the Graph Bar
    turtle.begin_fill()
    # Turn Turtle to Left to Go Up the Height of the Bar
    turtle.left(90)
    # Move Turtle Forward to Draw Height of Bar
    turtle.forward(divide)
    # Turn Right at the Top of the Bar
    turtle.right(90)
    # Draw Across the Bar 11 Pixels
    turtle.forward(11)
    # Turn to Face Down the Bar
    turtle.right(90)
    # Draw Down the Bar
    turtle.forward(divide)
    # Turn Back Across the Base of The Bar
    turtle.right(90)
    # Move Forward 11 Pixels to Complete the Graph Bar
    turtle.forward(11)
    # Lift the Pen off of the Page
    turtle.penup()
    # Turn to 180 Degrees to Face the Original Direction
    turtle.right(180)
    # Leave a Gap Between Each Bar ie. Jump over Base of Bar (11 Pixels + Leave 11 Pixel Blank Gap)
    turtle.forward(11)
    # Next Line : Describe the End of the Block Filling of the Graph Bar
    turtle.end_fill()
    # Pen Down Ready to Draw Next Bar
    turtle.pendown()
    return


# Draw 1 Bar on Graph
def graph(sale, exp):
    # GRAPH BAR PRINT OF ONE MONTHS SALES DATA

    # Set Colour of Sales Graph Bar
    turtle.color('black')
    # Next Line : Make the Graph Bar Smaller by Dividing the Excel Sales Data by 50
    divide = sale // 40

    graph_print_one_bar(divide)

    # GRAPH BAR PRINT OF ONE MONTHS EXPENDITURE DATA

    # Set Colour of Expenses Graph Bar
    turtle.color('red')
    # Next Line : Make the Graph Bar Smaller by Dividing the Excel Expenses Data by 50
    divide = exp // 40

    graph_print_one_bar(divide)

    # Leave a blank gap after each months graph bars
    turtle.penup()
    turtle.forward(11)
    return


for row in data:
    sale = int(row['sales'])
    exp = int(row['expenditure'])
    # We have 1 months sales + expenditure data: So Graph this Data
    graph(sale, exp)
    # Find the Lowest and Highest Sales For the Year : Start by Defaulting The Lowest with the first months data
    # otherwise the initial zero value will always be the lowest amount
    my_month = str(row['month'])

    if lowest_sales == 0:
        low_sales_month = my_month.capitalize()
        lowest_sales = sale
    elif lowest_sales > sale:
        low_sales_month = my_month.capitalize()
        lowest_sales = sale
    elif highest_sales < sale:
        high_sales_month = my_month.capitalize()
        highest_sales = sale
    sales.append(sale)

    if lowest_expenditure == 0:
        low_exp_month = my_month.capitalize()
        lowest_expenditure = exp
    elif lowest_expenditure > exp:
        low_exp_month = my_month.capitalize()
        lowest_expenditure = exp
    elif highest_expenditure < exp:
        high_exp_month = my_month.capitalize()
        highest_expenditure = exp

    expenditure.append(exp)
    print('low_exp_month', low_exp_month)
    print('lowest_expenditure', lowest_expenditure)
    print('high_exp_month', high_exp_month)
    print('highest_expenditure', highest_expenditure)
    print('expenditure', expenditure)


def graph_headings():
    # Final Graph Heading and any calculated values ie. anything that goes on the graph that isn't the graph bars
    turtle.color('black')
    turtle.penup()
    turtle.goto(100, 240)
    turtle.write("Monthly Sales Figures - 2018")
    turtle.goto(90, 230)
    turtle.write("Sales (Black) / Expenditure (Red)")
    turtle.goto(6, -20)
    turtle.write("  J         F         M        A         M         J         J         A        "
                 "S        O         N         D")
    turtle.goto(0, -80)
    turtle.write(low_sales_mth)
    turtle.goto(0, -100)
    turtle.write(high_sales_mth)
    turtle.goto(0, -140)
    turtle.write(low_exp_mth)
    turtle.goto(0, -160)
    turtle.write(high_exp_mth)

    turtle.goto(0, -200)
    turtle.write(avg_sales)
    turtle.goto(0, -220)
    turtle.write(avg_expenditure)

    turtle.goto(0, -260)
    turtle.write(total_sales)
    turtle.goto(0, -280)
    turtle.write(total_expenditure)

    turtle.goto(0, -320)
    turtle.write(yearly_profit)

    # Hide the Arrow Head when the Graph is Completed
    turtle.hideturtle()
    turtle.done()
    return


# Calculated Values used on the Graph within function graph_headings
total_sales = sum(sales)
total_expenditure = sum(expenditure)
print('total_expenditure', total_expenditure)
print('low_exp_mth', low_exp_month)
yearly_profit = total_sales - total_expenditure

average_sales = total_sales // 12
average_expenditure = total_expenditure // 12

low_sales_mth = f"The lowest  sales value was in {low_sales_month} this amount was £{lowest_sales:,d}"
high_sales_mth = f"The highest sales value was in {high_sales_month} this amount was £{highest_sales:,d}"

low_exp_mth = f"The lowest  expenditure value was in {low_exp_month} this amount was £{lowest_expenditure:,d}"
high_exp_mth = f"The highest expenditure value was in {high_exp_month} this amount was £{highest_expenditure:,d}"

avg_sales = f"Average sales per month: £{average_sales:,d}"
avg_expenditure = f"Average expenditure per month: £{average_expenditure:,d}"

total_sales = f"Total sales: £{total_sales:,d}"
total_expenditure = f"Total expenditure: £{total_expenditure:,d}"

yearly_profit = f"2018 Profit: £{yearly_profit:,d}"

graph_headings()
