from conftest import *

def test_open_modals(browser, variables):
    iframe = open_modals_and_wait_to_iframe(browser, variables)
    open_modal_window(iframe, variables)

    is_modal_header_visible(iframe, variables)
    is_modal_body_visible(iframe, variables)
    is_modal_footer_visible(iframe, variables)


