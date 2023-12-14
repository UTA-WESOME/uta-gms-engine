# Changelog
## v0.0.25 - 14-12-2023
### Added
- new sampler metric - pairwise_percentage
- new Tuple inside extreme_ranking, first one is pessimistic and the second one is optimistic approach
- new argument returned by get_representative_value_function_dict - number_of_rejected

### Changed
- Sampler now does not take into account indifference
- Adding pairwise_percentage and number_of_rejected, means that representative_value_function_dict now returns 8 arguments.

## v0.0.24 - 01-12-2023
### Added
- extreme ranking
- necessary and possible relations dicts

### Changed
- get_representative_value_function_dict now returns: alternatives_and_utilities_dict, criterion_functions, sampler_metrics, refined_extreme_ranking, necessary, possible

### Fixed
- criterion_functions from get_representative_value_function_dict now correctly returns negative values

## v0.0.23 - 28-11-2023
### Added
- Now '>=' comparison is possible
- Comparison dataclass: <br>
    alternative_1: str <br>
    alternative_2: str <br>
    criteria: List[str] = [] <br>
    sign: str = '>' <br>
### Deleted
- Preference dataclass, Indifference dataclass

### Fixed
- number of linear segmets is now number of linear segments and not number of characteristic points

## v0.0.22 - 27-11-2023
### Fixed
- deleted prints

## v0.0.21 - 26-11-2023
### Fixed
- refine_resolved_inconsistencies method

## v0.0.20 - 25-11-2023
### Added
- 'Intensity' dataclass with this schema: <br>
    alternative_id_1: str <br>
    alternative_id_2: str <br>
    alternative_id_3: str <br>
    alternative_id_4: str <br>
    criteria: List[str] = [] <br>
    sign: str = '>=' <br>

- get_representative_value_function_dict now raises Inconsistency exception 
when inconsistencies are found.

- Inconsistency exception carries data with constraints to be removed.
### Fixed
- Issue that threw error when no preferences were given

## v0.0.19 - 18-11-2023
### Added
- New default parameter 'criteria' for Position, Preference and Indifference
- All methods now take into account "partial criteria"
### Fixed
- alternative set in worst/best position can now be indifferent to other alternatives

## v0.0.18 - 10-11-2023
### Changed
- xmcda parser functions do not receive a path now. They receive XMCDA file and return a dictionary. 
  - get_performance_table_dict_xmcda has a new name. 
  - get_alternative_dict_xmcda has a new name and now. 
  - get_criterion_dict_xmcda has a new name and now.
- load_xmcda function doesn't receive a path. It receives XMCDA file and returns loaded file.

## v0.0.17 - 06-11-2023
### Fixed
- sampler_metrics now correctly takes into account interpolation when using predefined number of linear segments
- sampler_metrics now calculates much faster for predefined number of linear segments
- all methods now can take negative values
- github actions now correctly runs all the unit tests, when making push to remote repo

### Important Notes
- Current sampler_metrics takes does not take into account worst/best positions

- If there is given preference regarding worst/best position, 
the formula from the master's thesis is such that it makes it impossible for the given attribute to be equal to someone else,

## v0.0.16 - 31-10-2023
### Added
- sampler_metrics

### Changed
- get_representative_value_function_dict now returns sampler_metrics too.
    - representative_value_function_dict
    - criterion_functions
    - sampler_metrics

### Important Notes
- Current sampler_metrics takes into account only preference and indifference

- If there is given preference regarding worst/best position, 
the formula from the master's thesis is such that it makes it impossible for the given attribute to be equal to someone else,

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

