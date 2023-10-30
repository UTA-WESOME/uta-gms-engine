# Changelog
## v0.0.15 - 30-10-2023
### Added
- criterion_functions to get_representative_value_function_dict

### Changed
- get_representative_value_function_dict now returns a Tuple

### Important Notes
- If there is given preference regarding worst/best position, 
the formula from the master's thesis is such that it makes it impossible for the given attribute to be equal to someone else,

## v0.0.14 - 29-10-2023
### Changed
- min/max positions renamed to best/worst

### Fixed
- Fixed issue with best/worst positions, now should work properly

### Important Notes
- If there is given preference regarding worst/best position, 
the formula from the master's thesis is such that it makes it impossible for the given attribute to be equal to someone else,

## v0.0.13 - 24-10-2023
### Added
- Position object
    - min and max positions can't be negative
- get_hasse_diagram_dict and get_representative_value_function_dict now can take additional parameter 'positions',
which is a list of Position objects

### Changed
- parser.get_criterion_list_csv now returns list of Criterion objects with number_of_linear_segments = 0

### Fixed
- get_hasse_diagram_dict and get_representative_value_function_dict now works
for general functions and with predefined number of linear segments

### Deleted
- solver.get_ranking_dict method

### Important Notes
- positions in get_hasse_diagram_dict and get_representative_value_function_dict might not work properly

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

