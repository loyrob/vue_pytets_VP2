# vue_pytest_VP2
Pytest & Playwright tests for VUEJS.ORG examples website.
=========================================================

This repository contains a simple Pytest and Playwright tests of the VUEJS.ORG examples website.

## Table of Contents
- [Requirements](#requirements)
- [Getting started](#getting-started)
- [How to run](#how-to-run)
- [Test results](#test-results)
- [Test cases](#test-cases)
  - [conftest.py](#conftestpy)
  - [test_vue_crud.py](#test_vue_crudpy)
  - [test_vue_form_bindings.py](#test_vue_form_bindingspy)
  - [test_vue_modal.py](#test_vue_modalpy)

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

- [test_vue_crud.py](./tests/test_vue_crud.py) - contains test cases for [#crud](https://vuejs.org/examples/#crud).
  - <u>test_create_user</u> - test to create user.
    - create new user.
    - check if the user is created.
  - <u>test_update_user</u> - test to update user.
    - update user.
    - check if the user is updated.
  - <u>test_delete_user</u> - test to delete user.
    - delete user.
    - check if the user is deleted.
  - <u>test_filter_users</u> - test to filter of users.
    - read the count of users without filtering.
    - cerate new user.
    - read the count of users after creating a new user.
    - filter users.
    - check if the user is filtered.
    
- [test_vue_form_bindings.py](tests/test_vue_form_bindings.py) - contains test cases for [#form-bindings](https://vuejs.org/examples/#form-bindings).
  - <u>test_fill_and_read_input_box</u> - test to fill and read input box.
    - compare the value of the input box with the input box label.
    - fill the input box.
    - compare the value of the input box with the input box label after change.
  - <u>test_check_and_uncheck_checkbox</u> - test to check and uncheck checkbox.
    - check the checkbox, save the state and save the checkbox label. 
    - uncheck the checkbox, save the state and save the checkbox label.
    - verify the correct state of the correct checkbox state and label in both states.
  - <u>test_multichecknox</u> - test to check and uncheck multiple checkboxes.
    - uncheck default checkbox.
    - check two other checkboxes.
    - verify the correct state of the checkboxes.
    - verify the correct value of the checkbox label.
  - <u>test_radio</u> - test to select radio button.
    - save the default radio button label.
    - check the radio button.
    - verify the correct state of the radio button in both cases.
  - <u>test_select</u> - test to select option from a select box.
    - selects options 'B', 'C', and 'A' sequentially from the select box.
    - verify the correct value of label.  
  - <u>test_multiselect</u> - test to select multiple options from a select box.
    - select two options from the select box.
    - verify the correct value of label.
  
- [test_vue_modal.py](tests/test_vue_modal.py) - contains test case for [#modal](https://vuejs.org/examples/#modal).
  - <u>test_open_modal</u> - test to open the modal window.
    - click the 'Show Modal' button. 
    - check if the modal window is opened and header, body and footer are visible.

 


