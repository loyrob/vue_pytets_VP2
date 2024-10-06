from conftest import *

def test_fill_and_read_input_box(browser, variables):
    iframe = open_bindings_and_wait_to_iframe(browser, variables)

    input_text1 = read_input_box(iframe, variables)
    input_label1 = read_input_label(iframe, variables)

    fill_input_box(iframe, variables, "Ulanbatar")
    input_text2 = read_input_box(iframe, variables)
    input_label2 = read_input_label(iframe, variables)

    assert input_text1  == "Edit me"
    assert input_label1 == "Edit me"
    assert input_text2  == "Ulanbatar"
    assert input_label2 == "Ulanbatar"

def test_check_and_uncheck_checkbox(browser, variables):
    iframe = open_bindings_and_wait_to_iframe(browser, variables)

    check_the_checkbox(iframe, variables)
    checked1 = is_checkbox_checked(iframe, variables)
    label1 = read_checkbox_label(iframe, variables)

    unckeck_the_checkbox(iframe, variables)
    checked2 = is_checkbox_checked(iframe, variables)
    label2 = read_checkbox_label(iframe, variables)

    assert checked1 == True
    assert label1 == 'Checked: true'
    assert checked2 == False
    assert label2 == 'Checked: false'

def test_multichecknox(browser, variables):
    iframe = open_bindings_and_wait_to_iframe(browser, variables)

    uncheck_multi_checkbox('Jack',iframe, variables)
    check_multi_checkbox('John Mike', iframe, variables)
    checked1 = is_checkbox_Jack_checked(iframe, variables)
    checked2 = is_checkbox_John_checked(iframe, variables)
    checked3 = is_checkbox_Mike_checked(iframe, variables)
    checked  = read_multi_checkbox_label(iframe, variables)
    checked = ' '.join(checked.split())

    assert checked == 'Checked names: [ "John", "Mike" ]'
    assert checked1 == False
    assert checked2 == True
    assert checked3 == True

def test_radio(browser, variables):
    iframe = open_bindings_and_wait_to_iframe(browser, variables)

    check_radio('One', iframe, variables)
    checked1 = read_radio_label(iframe, variables)

    check_radio('Two', iframe, variables)
    checked2 = read_radio_label(iframe, variables)

    assert checked1 == 'Picked: One'
    assert checked2 == 'Picked: Two'


def test_multiselect(browser, variables):
    iframe = open_bindings_and_wait_to_iframe(browser, variables)

    select_multiselect_ac(iframe, variables)
    selected = read_multi_select_label(iframe, variables)
    selected = ' '.join(selected.split())

    assert selected == 'Selected: [ "A", "C" ]'