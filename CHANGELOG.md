# Changelog
## v0.0.12 - 17-10-2023
### Added
- get_representative_value_function_dict method
- get_hasse_diagram_dict now returns whole graph
  - example:
    {
    1: [3],
    2: [3],
    3: []
    }
  

### Fixed
- get_hasse_diagram_dict now returns Dict[str, List[str]]
example: {'A': {'F', 'K'}} changed to {'A': ['F', 'K']}

### Important Notes
- solver.get_ranking_dict seems not needed according to the latest information

- For now solver.get_hasse_diagram_dict will only work correctly for general function (all linear_segments set to 0)

## v0.0.11 - 11-10-2023
### Added

- New/Refined Parser methods:
    - get_performance_table_dict_csv
    - get_criterion_list_csv 


- Pydantic dataclasses (with data validation):
    - Preference
    - Indifference 
    - Criterion


- New solver method usage (using pydantic dataclasses):

### Removed
- Weights from problem calculation

### Important Notes
- solver.get_ranking_dict seems not needed according to the latest information

- For now solver.get_hasse_diagram_dict will only work correctly for general function (all linear_segments set to 0)

