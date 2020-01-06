#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# TT Securities    
#
# Computer Science 111
#

import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

def avg_price(prices):
	"""takes a list of 1 or more prices and computes and returns the average price"""
	result = 0
	for x in prices:
		result = result + int(x)
	return result/len(prices)

def std_dev(prices):
	"""takes a list of 1 or more prices and computes and returns the standard deviation of the prices"""
	result = 0 
	for x in prices:
		y = (x - avg_price(prices)) ** 2
		result = result + y 
	z = result/len(prices)
	return math.sqrt(z)

def max_day(prices):
	"""takes a list of 1 or more prices and computes and returns the day (i.e., the index) of the maximum price"""
	m = prices[0]
	y = 0
	for x in range(len(prices)):
		if m < prices[x]: 
			m = prices[x]
			y = x
	return y 

def any_below(prices,threshold):
	"""takes a list of 1 or more prices and an integer threshold, and uses a loop to determine if there are any prices below that threshold"""
	for i in prices:
		if i < threshold:
			return True
	return False 


def find_plan(prices):
	"""takes a list of 2 or more prices, and that uses one or more loops to find the best days on which to buy and sell the stock whose prices are given in the list of prices"""
	max_revenue = 0
	pos1 = 0 
	pos2 = 0
	for i in range(len(prices)):
		for j in range(i,len(prices)):
			revenue = (prices[j] - prices[i])
			if revenue > max_revenue:
				max_revenue = revenue
				pos1 = i
				pos2 = j 
	return [pos1, pos2, max_revenue]
		
				     					    
def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()
        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break 
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        elif choice == 3:
            average = avg_price(prices)
            print('The average price is',average)
        elif choice == 4:
            standarddeviation = std_dev(prices)
            print('The standard deviation is',standarddeviation)
        elif choice == 5:
            max1 = max_day(prices)  
            z = prices[max1]
            print('The max price is',z,'on day',max1)
        elif choice == 6:
            x = int(input('Enter the Threshold number:'))
            z = any_below(prices,x)
            if z == True:
                print('There is at least one price below',x)
            else:
                print('There are no prices below',x)
        elif choice == 7:
            plan = find_plan(prices)
            x = plan[0]
            y = plan[1]
            print('Buy on day',x,'at price',prices[x])
            print('Sell on day',y,'at price',prices[y])
            print('Total profit:',plan[2])
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
    


