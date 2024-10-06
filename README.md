# vue_pytest_VP2
Pytest & Playwright tests for VUEJS.ORG examples website.
=========================================================

This repository contains a simple example Pytest and Playwright tests of the VUEJS.ORG examples website.

## Requirements
- python 3.7 or higher
- pip
- pytest
- playwright

## Getting started
1. Clone the repository
```bash
git clone https://github.com/loyrob/vue_pytets_VP2.git
```
2. Install dependencies (if you don't have them already)
```bash
pip install pytest playwright
```

## How to run

2. Run tests
from the root of the project run:
```bash
pytest
```

## Test results
After running the tests, you will see the test results in the terminal.

## Test cases
- [conftest.py](tests/conftest.py) - contains fixtures, variables and functions for the tests.
- [test_vue_crud.py](tests/test_vue_crud.py) - contains test cases for [#crud](https://vuejs.org/examples/#crud).
  - test_create_user - test to create user.
  - test_update_user - test to update user.
  - test_delete_user - test to delete user.
  - test_filter_users - test to filter of users.
- [test_vue_form_bindings.py](tests/test_vue_form_bindings.py) - contains test cases for [#form-bindings](https://vuejs.org/examples/#form-bindings).
  - test_fill_and_read_input_box - test to fill and read input box.
  - test_check_and_uncheck_checkbox - test to check and uncheck checkbox.
  - test_multichecknox - test to check and uncheck multiple checkboxes.
  - test_radio - test to select radio button.
  - test_multiselect - test to select multiple options from a select box.
- [test_vue_modal.py](tests/test_vue_modal.py) - contains test case for [#modal](https://vuejs.org/examples/#modal).
  - test_open_modal - test to open the modal window.

 


