import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
def test_02_actions():
    driver = webdriver.Chrome()
    driver.get('https://awesomeqa.com/selenium/mouse_interaction.html')
    #clickable = driver.find_element(By.ID,"clickable")
    #actions = ActionChains(driver)
    #actions.click_and_hold(clickable).key_down(Keys.SHIFT).send_keys("Shabu").key_up(Keys.SHIFT).perform()
    # Click - Normal and action will performed
    # click and hold - click and hold -> click but we will not release.

    # Drag and Drop

    draggable = driver.find_element(By.ID,"draggable")
    droppable = driver.find_element(By.ID,"droppable")
    ActionChains(driver).drag_and_drop(draggable,droppable).perform()

    #driver.find_element(By.ID, "click").click()

    # Action Builder -> Mouse - back
    #actions_builder = ActionBuilder(driver)
    #actions_builder.pointer_action.pointer_down(MouseButton.BACK)
    #actions_builder.pointer_action.pointer_down(MouseButton.BACK)
    #actions_builder.perform()




    time.sleep(100)
