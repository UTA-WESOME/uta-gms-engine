# This file contains simple example of how to use uta-gms-engine package to make a ranking of variants
from typing import List
from src.utagmsengine.solver import Solver
from src.utagmsengine.dataclasses import Preference, Indifference, Criterion


performance_table_list_dummy = {
        'A': {'g1': 26.0, 'g2': 40.0, 'g3': 44.0},
        'B': {'g1': 2.0, 'g2': 2.0, 'g3': 68.0},
        'C': {'g1': 18.0, 'g2': 17.0, 'g3': 14.0},
        'D': {'g1': 35.0, 'g2': 62.0, 'g3': 25.0},
        'E': {'g1': 7.0, 'g2': 55.0, 'g3': 12.0},
        'F': {'g1': 25.0, 'g2': 30.0, 'g3': 12.0},
        'G': {'g1': 9.0, 'g2': 62.0, 'g3': 88.0},
        'H': {'g1': 0.0, 'g2': 24.0, 'g3': 73.0},
        'I': {'g1': 6.0, 'g2': 15.0, 'g3': 100.0},
        'J': {'g1': 16.0, 'g2': 9.0, 'g3': 0.0},
        'K': {'g1': 26.0, 'g2': 17.0, 'g3': 17.0},
        'L': {'g1': 62.0, 'g2': 43.0, 'g3': 0.0}
}
preferences_dummy: List[Preference] = [Preference(superior='G', inferior='F'), Preference(superior='F', inferior='E')]

indifferences_dummy: List[Indifference] = [Indifference(equal1='D', equal2='G')]

criteria_dummy: List[Criterion] = [
    Criterion(criterion_id='g1', gain=True),
    Criterion(criterion_id='g2', gain=True),
    Criterion(criterion_id='g3', gain=True)
]

solver = Solver(show_logs=False)

ranking = solver.get_ranking_dict(
    performance_table_list_dummy,
    preferences_dummy,
    indifferences_dummy,
    criteria_dummy
)

print(ranking)
