### About Me ########################################
#   Coded By : Muneeb Ahmad                         #
#   Github Link: https://github.com/Muneeb-Ahmad-Ch #
#####################################################

import os
from time import sleep
from datetime import datetime
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

#############
# Constants #
#############
# Update Your URL below :
BASE_URL = 'https://ethereumprice.org/live/'
# below is the pause interval after which next screenshot will be taken (in sec)
TIMER_PAUSE = 5  # 30 sec
# default output folder name is 'output', if you want to replace it you can replace below
PARENT_FOLDER = os.getcwd() + '\\output\\'
# total number of screenshots required
TOTAL_REQUIRED_SCREENSHOTS = 5


#############
# Functions #
#############
def get_current_datetime():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("[%H_%M_%S %d_%m_%Y]")
    return dt_string
#############


class BOT ():
    def __init__(self, headless=False) -> None:
        self.Start(headless)
        pass

    def Start(self, headless=False):
        print('Starting Bot .', end='')
        options = uc.ChromeOptions()
        print('.', end='')
        if headless:
            options.headless = True
            options.add_argument('--headless')
        print('.', end='')
        self.driver = uc.Chrome(options=options, use_subprocess=True)
        print('.', end='')
        # you can also update window size of browser
        self.driver.set_window_size(1300, 700)
        print('.', end='')
        self.wait = WebDriverWait(self.driver, 10)
        print(' [Done]')

    def goto(self, url=BASE_URL):
        self.driver.get(url)
        print('Going to:', url)

        self.sleep(2)

    # wait for methods
    def wait_xpath(self, code):
        self.wait.until(
            ExpectedConditions.presence_of_element_located((By.XPATH, code)))

    def click_by_xpath(self, xp):
        self.wait_xpath(xp)
        self.driver.find_element(
            By.XPATH, xp).click()

    def get_text_by_xpath(self, xp):
        self.wait_xpath(xp)
        return self.driver.find_element(
            By.XPATH, xp).text

    def sleep(self, n):
        print(f"On Sleep for {n} sec.")
        sleep(n)

    def quit(self):
        self.driver.quit()
        print("Bot Browser Quitted.")

    def take_screenshot(self,  parent_folder, output_filename_prefix):
        try:
            # create output folder if not there
            if not os.path.exists(parent_folder):
                os.makedirs(parent_folder)
                print("File Created!")
            else:
                # print("Folder Already Found!")
                pass
            print("Taking Screen Shot ...")

            dt = get_current_datetime()
            # output file name will have the output_filename along with the date and time
            fname = parent_folder + f"{output_filename_prefix} {dt}.png"
            self.driver.save_screenshot(fname)
            print(f"Screenshot Saved: {fname} ")
        except:
            print("Error in Taking Screen Shot")


if __name__ == '__main__':

    print("File location:", os.getcwd())
    print("Loading ...")
    # in case you want to see the live action of the backend browser, set headless to False
    bot = BOT(headless=True)
    bot.goto(BASE_URL)  # go to base url by default
    for i in range(TOTAL_REQUIRED_SCREENSHOTS):
        bot.take_screenshot(parent_folder=PARENT_FOLDER,
                            output_filename_prefix=i)
        bot.sleep(TIMER_PAUSE)

    print("End of the program.")
