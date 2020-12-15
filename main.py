import argparse
import os
from train import train
from utils.argutils import print_args


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--rules", help="Name of the run algorithm",default="FedProx")
    parser.add_argument("--model", help="Name of the run model", default="CNN")
    parser.add_argument("--client", help="Number of the client", default=10)
    parser.add_argument("--round", help="Number of the train in the server", default=10)
    parser.add_argument("--epoch", help="Number of the train in the client", default=500)

    args = parser.parse_args()
    print_args(args,parser)

    train(args)


