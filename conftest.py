# conftest.py
from xml.etree.ElementPath import xpath_tokenizer

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def variables():
    return {
        "IFRAME":               'xpath=//div[@class="iframe-container"]/iframe',

        "URL1":                 'https://vuejs.org/examples/#form-bindings',

        "INPUT_INPUT":          'xpath=//*[@id="app"]/input[1]',
        "INPUT_TEXT":           'xpath=//*[@id="app"]/p[1]',

        "CHECKBOX":             'xpath=//*[@id="checkbox"]',
        "CHECKBOX_LABEL":       'xpath=//*[@id="app"]/label[1]',

        "MULTI_SELECT":         'xpath=//select[@multiple]',
        "MULTI_SELECT_LABEL":   'xpath=//*[@id="app"]/p[5]',
        "MULTI_CHECKBOX_JACK":  'xpath=//*[@id="jack"]',
        "MULTI_CHECKBOX_JOHN":  'xpath=//*[@id="john"]',
        "MULTI_CHECKBOX_MIKE":  'xpath=//*[@id="mike"]',
        "MULTI_CHECKBOX_LABEL": 'xpath=//*[@id="app"]/p[2]',

        "RADIO_ONE":            'xpath=//*[@id="one"]',
        "RADIO_TWO":            'xpath=//*[@id="two"]',
        "RADIO_LABEL":          'xpath=//*[@id="app"]/p[3]',

        "SELECT":               'xpath=//*[@id="app"]/select[1]',
        "SELECT_A":             'xpath=//*[@id="app"]/select[1]/option[2]/text()',
        "SELECT_B":             'xpath=//*[@id="app"]/select[1]/option[3]/text()',
        "SELECT_C":             'xpath=//*[@id="app"]/select[1]/option[4]/text()',
        "SELECT_LABEL":         'xpath=//*[@id="app"]/p[4]',

        "URL2":                 'https://vuejs.org/examples/#modal',
        "MODAL_BUTTON":         'xpath=//button[@id="show-modal"]',
        "MODAL_HEADER":         'xpath=//div[@class="modal-header"]',
        "MODAL_BODY":           'xpath=//div[@class="modal-body"]',
        "MODAL_FOOTER":         'xpath=//div[@class="modal-footer"]',

        "URL3":                 'https://vuejs.org/examples/#crud',

        "FILTER_PREFIX_INPUT":  'xpath=//input[@placeholder="Filter prefix"]',
        "NAME_SELECTOR":        'xpath=//*[@id="app"]/select',
        "NAME_INPUT":           'xpath=//*[@id="app"]/label[1]/input',
        "SURNAME_INPUT":        'xpath=//*[@id="app"]/label[2]/input',
        "CREATE_BUTTON":        'xpath=//*[@id="app"]/div[2]/button[1]',
        "UPDATE_BUTTON":        'xpath=//*[@id="app"]/div[2]/button[2]',
        "DELETE_BUTTON":        'xpath=//*[@id="app"]/div[2]/button[3]'

    }

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

def open_bindings_and_wait_to_iframe(page, variables):
    page.goto(variables["URL1"])
    # page.wait_for_selector(variables["IFRAME"])
    iframe = page.frame_locator(variables["IFRAME"])
    return iframe

def fill_input_box(iframe, variables, text):
    iframe.locator(variables["INPUT_INPUT"]).fill(text)

def read_input_box(iframe, variables):
    return iframe.locator(variables["INPUT_INPUT"]).input_value()

def read_input_label(iframe, variables):
    text = iframe.locator(variables["INPUT_TEXT"]).text_content()
    print(f"input label: {text}")
    return text

def check_the_checkbox(iframe, variables):
    checkbox = iframe.locator(variables["CHECKBOX"])
    checkbox.check()

def unckeck_the_checkbox(iframe, variables):
    checkbox = iframe.locator(variables["CHECKBOX"])
    checkbox.uncheck()

def is_checkbox_checked(iframe, variables):
    checkbox = iframe.locator(variables["CHECKBOX"])
    checked = checkbox.is_checked()
    return checked

def check_multi_checkbox(names, iframe, variables):
    if 'Jack' in names:
        checkbox = iframe.locator(variables["MULTI_CHECKBOX_JACK"])
        checkbox.check()
    if 'John' in names:
        checkbox = iframe.locator(variables["MULTI_CHECKBOX_JOHN"])
        checkbox.check()
    if 'Mike' in names:
        checkbox = iframe.locator(variables["MULTI_CHECKBOX_MIKE"])
        checkbox.check()

def uncheck_multi_checkbox(names, iframe, variables):
    if 'Jack' in names:
        checkbox = iframe.locator(variables["MULTI_CHECKBOX_JACK"])
        checkbox.uncheck()
    if 'John' in names:
        checkbox = iframe.locator(variables["MULTI_CHECKBOX_JOHN"])
        checkbox.uncheck()
    if 'Mike' in names:
        checkbox = iframe.locator(variables["MULTI_CHECKBOX_MIKE"])
        checkbox.uncheck()

def is_checkbox_Jack_checked(iframe, variables):
    checkbox = iframe.locator(variables["MULTI_CHECKBOX_JACK"])
    checked = checkbox.is_checked()
    return checked

def is_checkbox_John_checked(iframe, variables):
    checkbox = iframe.locator(variables["MULTI_CHECKBOX_JOHN"])
    checked = checkbox.is_checked()
    return checked

def is_checkbox_Mike_checked(iframe, variables):
    checkbox = iframe.locator(variables["MULTI_CHECKBOX_MIKE"])
    checked = checkbox.is_checked()
    return checked

def read_multi_checkbox_label(iframe, variables):
    text = iframe.locator(variables["MULTI_CHECKBOX_LABEL"]).text_content()
    print(f"multi checkbox label: {text}")
    return text

def read_checkbox_label(iframe, variables):
    text = iframe.locator(variables["CHECKBOX_LABEL"]).text_content()
    print(f"--- checkbox label: {text}")
    return text

def select_multiselect_ac(iframe, variables):
    # Select options by index 0 and 2 in the multi-select element
    iframe.locator(variables["MULTI_SELECT"]).select_option(index=[0, 2])

def read_multi_select_label(iframe, variables):
    text = iframe.locator(variables["MULTI_SELECT_LABEL"]).text_content()
    print(f"multi select label: {text}")
    return text

def check_radio(radio, iframe, variables):
    if radio == 'One':
        radio = iframe.locator(variables["RADIO_ONE"])
        radio.check()
    if radio == 'Two':
        radio = iframe.locator(variables["RADIO_TWO"])
        radio.check()

def read_radio_label(iframe, variables):
    text = iframe.locator(variables["RADIO_LABEL"]).text_content()
    return text

def open_modals_and_wait_to_iframe(page, variables):
    page.goto(variables["URL2"])
    iframe = page.frame_locator(variables["IFRAME"])
    return iframe

def open_modal_window(page, variables):
    page.locator(variables["MODAL_BUTTON"]).click()

def is_modal_header_visible(iframe, variables):
    header = iframe.locator(variables["MODAL_HEADER"])
    visible = header.is_visible()
    assert visible

def is_modal_body_visible(iframe, variables):
    body = iframe.locator(variables["MODAL_BODY"])
    visible = body.is_visible()
    assert visible

def is_modal_footer_visible(iframe, variables):
    footer = iframe.locator(variables["MODAL_FOOTER"])
    visible = footer.is_visible()
    assert visible

def open_crud_and_wait_to_iframe(page, variables):
    page.goto(variables["URL3"])
    iframe = page.frame_locator(variables["IFRAME"])
    return iframe

def filter_prefix_input(iframe, variables, text):
    iframe.locator(variables["FILTER_PREFIX_INPUT"]).fill(text)

def read_name(iframe, variables):
    name = iframe.locator(variables["NAME_INPUT"]).input_value()
    return name

def read_surname(iframe, variables):
    surname = iframe.locator(variables["SURNAME_INPUT"]).input_value()
    return surname

def select_name(iframe, variables, name):
    iframe.locator(variables["NAME_SELECTOR"]).click()
    iframe.locator(variables["NAME_SELECTOR"]).fill(name)

def fill_name(iframe, variables, name):
    iframe.locator(variables["NAME_INPUT"]).fill(name)

def fill_surname(iframe, variables, surname):
    iframe.locator(variables["SURNAME_INPUT"]).fill(surname)

def click_create_button(iframe, variables):
    iframe.locator(variables["CREATE_BUTTON"]).click()

def click_update_button(iframe, variables):
    iframe.locator(variables["UPDATE_BUTTON"]).click()

def click_delete_button(iframe, variables):
    iframe.locator(variables["DELETE_BUTTON"]).click()

def read_name_selector(iframe, variables):
    name = iframe.locator(variables["NAME_SELECTOR"]).text_content()
    return name

def check_name_in_name_selector(iframe, variables, name):
    names = read_name_selector(iframe, variables)
    assert name in names
    print(f"Name: {name} is in the name selector")

def check_name_not_in_name_selector(iframe, variables, name):
    names = read_name_selector(iframe, variables)
    assert name in names
    print(f"Name: {name} is in the name selector")

def create_user(iframe, variables, name, surname):
    fill_name(iframe, variables, name)
    fill_surname(iframe, variables, surname)
    click_create_button(iframe, variables)
    check_name_in_name_selector(iframe, variables, surname + ", " + name)

def select_name_from_names(iframe, variables, name1):
    xpath = f"//option[contains(text(),'{name1}')]"
    iframe.locator(xpath).click()

def rename_user(iframe, variables, name1, surname1, name2, surname2):
    select_name_from_names(iframe, variables, surname1)
    surname = read_surname(iframe, variables)
    assert surname == surname1

    fill_name(iframe, variables, name2)
    fill_surname(iframe, variables, surname2)
    click_update_button(iframe, variables)

    surname = read_surname(iframe, variables)
    assert surname == surname2

    check_name_in_name_selector(iframe, variables, surname2 + ", " + name2)

def delete_user(iframe, variables, name, surname):
    select_name_from_names(iframe, variables, surname)
    click_delete_button(iframe, variables)
    check_name_not_in_name_selector(iframe, variables, surname + ", " + name)
    print(f"Name: {name} is not already in the name selector")

def count_names_in_name_selector(iframe, variables):
    iframe.locator(variables["NAME_SELECTOR"]).click()
    xpath = f"{variables['NAME_SELECTOR']}/option"
    print(f"\n ----xpath: " + xpath)
    options_locator = iframe.locator(xpath)
    count = options_locator.count()

    # options_locator = iframe.locator(f"{variables['NAME_SELECTOR']}/option")
    # print(f"\n ----options selector: " + options_locator)
    # count = options_locator.count()
    print(f"\n ----Number of options in the selector: {count}")
    return count

def fill_filter(iframe, variables, param):
    iframe.locator(variables["FILTER_PREFIX_INPUT"]).fill(param)