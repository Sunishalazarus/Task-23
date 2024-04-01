from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver import ActionChains

class DragAndDrop:

    def __init__(self, url="https://jqueryui.com/droppable/"):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    def boot(self):
        """
        This method is to open up the chrome browser with the URL and makes the browser to go fullscreen.
        """
        self.driver.get(self.url)
        sleep(3)
        self.driver.maximize_window()

    def quit(self):
        """
        This method is used to close the webbrowser
        """
        self.driver.quit()

    def findElementByID(self, id):
        return self.driver.find_element(by=By.ID, value=id)

    def dragAndDrop(self):
        """
        To do a drag and drop operation.
        :return:
        """
        try:
            self.boot()
            sleep(5)
            self.driver.switch_to.frame(self.driver.find_element(by=By.TAG_NAME, value="iframe"))
            start = self.findElementByID("draggable")
            destination = self.findElementByID("droppable")
            action_chains = ActionChains(self.driver)
            action_chains.drag_and_drop(start, destination).perform()
            sleep(3)


        except NoSuchElementException as e:
            print(e)

        finally:
            self.driver.quit()

obj= DragAndDrop()
obj.dragAndDrop()