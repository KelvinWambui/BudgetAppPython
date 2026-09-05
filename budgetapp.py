class Category:
    def __init__(self,name):
        self.ledger=[]
        self.name=name
    #deposit
    def deposit(self,amount,description=''):
        self.ledger.append({'amount':amount,'description':description})
        
    #Get Balance
    def get_balance(self):
        balance=0
        for trans in self.ledger:
            balance+=trans['amount']
        
        return balance

    #check funds
    def check_funds(self,amount):
        return amount <= self.get_balance()

    #withdraw funds
    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount':-amount,'description': description})
            return True
        else :
            return False
    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount,description=f'Transfer to {category.name}')
            category.deposit(amount,description=f'Transfer from {self.name}')
            return True
        else:
            return False

    def __str__(self):
        title = self.name.center(30, '*')

        for trans in self.ledger:
            description = trans['description'][:23]
            amount = trans['amount']

            title += f"\n{description:<23}{amount:>7.2f}"

        title += f"\nTotal: {self.get_balance()}"

        return title
       


        
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)


            


def create_spend_chart(categories):
    
    # Calculate spending for each category
    spent_amounts = []

    for category in categories:
        spent = 0

        for transaction in category.ledger:
            if transaction["amount"] < 0:
                spent += abs(transaction["amount"])

        spent_amounts.append(spent)

    # Calculate total spending
    total_spent = sum(spent_amounts)

    # Calculate percentage for each category
    percentages = []

    for spent in spent_amounts:
        percentage = int((spent / total_spent) * 100)
        percentage = (percentage // 10) * 10
        percentages.append(percentage)

    # Start building the chart
    chart = "Percentage spent by category\n"

    # Create percentage bars from 100 to 0
    for percentage in range(100, -1, -10):
        chart += f"{percentage:>3}| "

        for category_percentage in percentages:
            if category_percentage >= percentage:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Find the longest category name
    max_length = max(len(category.name) for category in categories)

    # Write category names vertically
    for i in range(max_length):
        chart += "     "

        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

        if i < max_length - 1:
            chart += "\n"

    return chart

