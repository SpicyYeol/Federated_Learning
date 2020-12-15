import numpy as np

def random_client(round,selected_clients,num_clients):
    # round            : training round
    # selected_clients : user parameter
    # num_clients      : total generated clients
    num_clients = min(selected_clients,num_clients)
    np.random.seed(round)
    indices = np.random.choice(range(num_clients),num_clients,replace=False)
    return indices
