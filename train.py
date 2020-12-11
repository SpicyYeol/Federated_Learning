from models import *
from rules import *
import torch

def train(args):
    client = []
    server = None

    if args.model is "CNN":
        [client.append(CNN.CNN()) for i in range(args.client)]
        server = CNN.CNN() # CNN()

    module_list = server.state_dict()

    list_net = list(map(lambda x: x.state_dict(),client))

    if args.rules is "FedAvg":
        server.load_state_dict(FedAvg.fedAvg(server,client))


