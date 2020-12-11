def fedAvg(server, client):
    module_list = server.state_dict()

    list_net = list(map(lambda x: x.state_dict(),client))

    for param in zip(module_list):
        tmp = 0
        for weight in list_net:
            tmp = tmp + weight[param[0]]
        tmp = tmp / len(list_net)
        module_list[param[0]] = tmp

    return module_list
