from behave import When, Then
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


RECURRING_CHECKS = (By.CSS_SELECTOR, 'body > div.page__navigation > div > div > div:nth-child(1) > ul > li:nth-child(2) > a')

@When('Open posthire from top navbar2')
def hover_over_and_select(context):
    element_to_hover_over = context.driver.find_element_by_css_selector('body > div.page__navigation > div > div > div:nth-child(2) > ul > li:nth-child(3) > div > button')
    hover = ActionChains(context.driver).move_to_element(element_to_hover_over)
    hover.perform()
    sleep(2)
    context.driver.find_element_by_xpath('/html/body/ul[2]/li[2]/a').click()
    sleep(3)
    context.driver.maximize_window()
@When('click recurring checks2')
def click_recurring_checks(context):
    context.driver.find_element(*RECURRING_CHECKS).click()
    sleep(2)

@When('Click rule to edit')
def click_rule_to_delete(context):
    context.driver.find_element_by_css_selector('td.obiq-table__cell.rules-table__clickable').click()
    sleep(3)

@Then('edit {reminder}')
def edit_reminder(context, reminder):
    reminder = context.driver.find_element_by_css_selector('input.obiq-input.message-template-row__reminder-item.message-template-row__days-input')
    reminder.clear()
    reminder.send_keys('11')
    context.driver.find_element_by_css_selector('button.rule__button.obiq-button.obiq-button_primary').click()
    sleep(4)

