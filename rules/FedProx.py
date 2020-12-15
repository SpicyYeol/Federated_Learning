import numpy as np
from utils import *
def FedProx(server, client, data, round, selected_client):
    # data : percentage
    module_list = server.state_dict()

    list_net = list(map(lambda x: x.state_dict(),client))

    for param in zip(module_list):
        tmp = 0
        for weight,per in zip(list_net, data):
            tmp = tmp + weight[param[0]]*per
        module_list[param[0]] = tmp

    diff = 0
    # for param in zip(module_list):
    #     for weight in list_net:
    #         diff += np.sum(np.square(module_list[param[0]]-weight))
    # diff = diff/len(list_net)

    indics = flutils.random_client(round,selected_clients=selected_client,num_clients=len(client))
    print(indics)

    return module_list