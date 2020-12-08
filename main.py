import argparse
import os
from utils.argutils import print_args
from models import *
import torch

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="Name of the run algorithm",default="FedAvg")
    parser.add_argument("--model", help="Name of the run model", default="CNN")
    parser.add_argument("--round", help="Number of the train in the server ", default=10)
    parser.add_argument("--epoch", help="Number of the train in the client ", default=500)

    args = parser.parse_args()
    print_args(args,parser)


    if args.model is "CNN":
        net = CNN.CNN()

    a = net.modules()


    # name, param = net.named_parameters()


    with torch.no_grad():
        print("A")

    print(net)


