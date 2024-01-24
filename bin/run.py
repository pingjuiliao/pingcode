#!/usr/bin/env python3

import argparse

algorithm_list = {
    'mis': 'pingcode.dynamic_programming.max_independent_set.MaxIndependentSet',
    'dijkstra': 'pingcode.graph.shortest_path.ShortestPath',
    'kbest_pair': 'pingcode.kbest.kbest_pair.KBestPairFromTwoList',
    'dream_team': 'pingcode.kbest.dream_team.DreamTeam',
    'mergesort': 'pingcode.sorting.mergesort.MergeSort',
    'quicksort': 'pingcode.sorting.quicksort.QuickSort',
}


def algorithm_class_import(name):
    module_name, alg_class_name = name.rsplit('.', 1)
    module = __import__(module_name, fromlist=[alg_class_name])
    alg_class = getattr(module, alg_class_name)
    return alg_class


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('-a', '--alg', dest='algorithm', required=True)
    args = p.parse_args()

    if args.algorithm not in algorithm_list:
        print(f'[Error] {args.algorithm} not found.')
        return

    module_name = algorithm_list[args.algorithm]

    # (Dynamically) Get the class
    AlgorithmProblem = algorithm_class_import(module_name)

    # Problem & Solve
    problem = AlgorithmProblem()
    problem.evaluate()


if __name__ == '__main__':
    parse_args()
