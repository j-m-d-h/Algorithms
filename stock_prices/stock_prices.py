#!/usr/bin/python

import argparse

def find_max_profit(prices):
    max = -100000
    for m in range(len(prices)-1):
        for s in range(m+1, len(prices)):
            if prices[s] - prices[m] > max:
                max = prices[s] - prices[m]
                print(prices[s], '-', prices[m], '= ', max)
            else:
                pass
    return max
if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
