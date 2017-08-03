import lottery_loader
import network2

def main():
  lottery_loader.load_data()
  training_data, test_data = lottery_loader.load_data()
  import pdb; pdb.set_trace()
  net = network2.Network([50, 300, 1])
  net.SGD(training_data, epochs=60, mini_batch_size=10, eta=100, evaluation_data=test_data)


if __name__ == "__main__":
  main()
