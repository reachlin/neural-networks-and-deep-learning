import cPickle

# Third-party libraries
import numpy as np

red = 33
blue = 16

def load_data():
  train_input = np.genfromtxt('../data/lottery_old.csv', delimiter=',', dtype=int, usecols=(0,1,2,3,4,5,6,7))
  train_data = [vectorized_input(x) for x in train_input]
  train_result = [np.ones((1, 1))]*len(train_data)
  train = zip(train_data, train_result)

  test_input = np.genfromtxt('../data/lottery.csv', delimiter=',', dtype=int, usecols=(0,1,2,3,4,5,6,7))
  test_data = [vectorized_input(x) for x in test_input]
  test_result = [np.ones((1, 1))]*len(test_data)
  test = zip(test_data, test_result)
  return (train, test)

def vectorized_input(row):
  # total 33+16+1 slots
  # slot 0 for lottery date
  # slot 1-33 for red balls
  # slot 34-49 for blue balls
  rtn = np.zeros((red+blue+1, 1), dtype=int)
  for index, item in enumerate(row):
    if index == 0:
      rtn[index, 0] = item
    elif index == len(row)-1:
      rtn[item+red, 0] = 1
    else:
      rtn[item, 0] = 1
  return rtn
