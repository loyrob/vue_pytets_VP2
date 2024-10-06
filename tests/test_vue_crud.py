from conftest import *

def test_create_user(browser, variables):
    iframe = open_crud_and_wait_to_iframe(browser, variables)

    fill_name(iframe, variables, "Adam")
    fill_surname(iframe, variables, "Madam")
    click_create_button(iframe, variables)

    check_name_in_name_selector(iframe, variables, "Adam")
    check_name_in_name_selector(iframe, variables, "Madam")
    check_name_in_name_selector(iframe, variables, "Madam, Adam")

def test_modify_user(browser, variables):
    iframe = open_crud_and_wait_to_iframe(browser, variables)
    create_user(iframe, variables, "Eva", "Madar")
    rename_user(iframe, variables, "Eva", "Madar", "Eve", "Smith")

def test_delete_user(browser, variables):
    iframe = open_crud_and_wait_to_iframe(browser, variables)
    create_user(iframe, variables, "Eva", "Madac")
    click_delete_button(iframe, variables)
    check_name_not_in_name_selector(iframe, variables, "Madac, Eva")


def test_filter_users(browser, variables):
    iframe = open_crud_and_wait_to_iframe(browser, variables)
    count_names_in_name_selector(iframe, variables)
    create_user(iframe, variables, "Eva", "Muster")
    count_names_in_name_selector(iframe, variables)
    fill_filter(iframe, variables, "Muster")
    count_names_in_name_selector(iframe, variables)


