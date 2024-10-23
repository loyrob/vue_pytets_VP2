from conftest import *

def test_create_user(browser, variables):
    iframe = open_crud_and_wait_to_iframe(browser, variables)

    fill_name(iframe, variables, "Adam")
    fill_surname(iframe, variables, "Madam")
    click_create_button(iframe, variables)

    verify_that_name_in_name_selector(iframe, variables, "Adam")
    verify_that_name_in_name_selector(iframe, variables, "Madam")
    verify_that_name_in_name_selector(iframe, variables, "Madam, Adam")

def test_modify_user(browser, variables):
    iframe = open_crud_and_wait_to_iframe(browser, variables)
    create_user(iframe, variables, "Eva", "Madar")
    rename_user(iframe, variables, "Eva", "Madar", "Eve", "Smith")

    verify_that_name_in_name_selector(iframe, variables, "Smith, Eve")

def test_delete_user(browser, variables):
    iframe = open_crud_and_wait_to_iframe(browser, variables)
    create_user(iframe, variables, "Eva", "Madac")
    click_delete_button(iframe, variables)
    verify_that_name_is_not_in_name_selector(iframe, variables, "Madac, Eva")

def test_filter_users(browser, variables):
    iframe = open_crud_and_wait_to_iframe(browser, variables)
    count1 = count_names_in_name_selector(iframe, variables)
    create_user(iframe, variables, "Eva", "Muster")
    count2 = count_names_in_name_selector(iframe, variables)
    fill_filter(iframe, variables, "Muster")
    count3 = count_names_in_name_selector(iframe, variables)

    # assert count1 == 3
    # assert count2 == 4
    # assert count3 == 2
    assert count2 == count1 + 1
    assert count3 == 2


