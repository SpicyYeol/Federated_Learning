import argparse
import os
from utils.argutils import print_args
from models import *
from rules import *
import torch

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="Name of the run algorithm",default="FedAvg")
    parser.add_argument("--model", help="Name of the run model", default="CNN")
    parser.add_argument("--client", help="Number of the client", default=3)
    parser.add_argument("--round", help="Number of the train in the server", default=10)
    parser.add_argument("--epoch", help="Number of the train in the client", default=500)

    args = parser.parse_args()
    print_args(args,parser)

    client = []
    server = None

    if args.model is "CNN":
        [client.append(CNN.CNN()) for i in range(args.client)]
        server = CNN.CNN()

    module_list = server.state_dict()

    list_net = list(map(lambda x: x.state_dict(),client))


    server.load_state_dict(FedAvg(server,client))


