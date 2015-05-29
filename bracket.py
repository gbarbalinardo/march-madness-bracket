import numpy as np
import cProfile as profile
import numbapro as nbp
import json

from math import sqrt, log, cos, pi

# import data

file_directory = "input_json.json"
json_data = open(file_directory).read()
data = json.loads(json_data)
scale_factor = 10


def repeat_tournament(path, iterations):

    # run iterations of the tournament and return the winner of each

    n_teams = path[0][0].size
    path = path.astype(np.int32, copy=False)
    teams_id = np.zeros((iterations, n_teams))
    teams_id = teams_id.astype(np.int32, copy=False)
    result = run_tournament(path, teams_id)
    return result


@nbp.guvectorize(['void(int32[:,:], int32[:], int32[:])'], '(n, n),(n)->()', target='gpu')
def run_tournament(path_t, teams_id, result):

    # given the list of scores in a matrix, find the winner of the tournament

    n_teams = path_t[0].size
    for i in range(n_teams):
        teams_id[i] = i
    bin_size = 2
    while bin_size <= n_teams:
        for i in range(0, n_teams, bin_size):
            if path_t[teams_id[i], teams_id[i + bin_size/2]] >= path_t[teams_id[i + bin_size/2], teams_id[i]]:
                teams_id[i] = teams_id[i]
            else:
                teams_id[i] = teams_id[i+bin_size/2]
        bin_size *= 2
    result[0] = teams_id[0]



@nbp.vectorize(['int16(float32, float32, float32)'], target='gpu')
def distribution(mu, u, v):

    # box muller transform: generate a normal distribution from a uniform one

    sigma = 10
    z2 = sqrt(-2 * log(u)) * cos(2 * pi * v)
    x2 = mu + z2 * sigma
    return x2


def run_simulation():

    k1_matrix = np.zeros(len(data))
    k0_matrix = np.zeros(len(data))

    for i in range(0, len(data)):
        team = data[i]
        k0_matrix[i] = team['offensive']
        k1_matrix[i] = team['defensive']

    iterations = 1000
    n_team = len(k0_matrix)
    k0_matrix[:] = 1.0/k0_matrix[:]

    k0_matrix *= 8
    k1_matrix *= 8

    # l_t correspond to a single istance of the tournament
    l_t_matrix = np.outer(k1_matrix, k0_matrix)

    # l contains all the instances of the tournament
    l_matrix = np.zeros(shape=(iterations, n_team, n_team))

    for t in range(iterations):
        l_matrix[t, :, :] = l_t_matrix

    # define type of the variables
    rand1 = np.random.uniform(size=(iterations, n_team, n_team))
    rand2 = np.random.uniform(size=(iterations, n_team, n_team))
    rand1 = rand1.astype(np.float32, copy=False)
    rand2 = rand2.astype(np.float32, copy=False)
    l_matrix = l_matrix.astype(np.float32, copy=False)

    # generate normal distributions
    path = distribution(l_matrix, rand1, rand2)

    # Print the list of winners
    results = repeat_tournament(path, iterations)
    for winner in results:
        print data[winner]["team"]


if __name__ == '__main__':
    profile.run("run_simulation()", sort="time")