from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class orangehrm:
    def setup(self):
        self.driver = webdriver.Chrome("C:\\Users\\Rakesh Varma\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
#----------------- TC_PIM_01--------------------
    def forgetlink(self):
        self.driver.find_element(By.XPATH,'//div[@class="orangehrm-login-forgot"]/p').click()
        self.driver.find_element(By.XPATH,'//input[@class="oxd-input oxd-input--active"]').send_keys("Sirisha")
        self.driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        time.sleep(5)
        get_text = self.driver.find_element(By.XPATH,'//div[@class="orangehrm-card-container"]/h6').text
        expected_result = "Reset Password link sent successfully"
        print("TEST CASE ID: TC_PIM_01")
        if get_text == expected_result:
            print("TEST CASE RESULT: PASSED")
        else:
            print("TEST CASE RESULT: FAILED")
#----------------- TC_PIM_02--------------------
    def admin_headers(self):
        self.driver.back()
        self.driver.back()
        self.driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("admin123")
        self.driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,'(//li[@class="oxd-main-menu-item-wrapper"])[1]').click()
        time.sleep(5)
        title = self.driver.title
        print("TEST CASE ID: TC_PIM_02")
        is_test_case_passed = True
        if title != "OrangeHRM":
            is_test_case_passed = False
        gettext = self.driver.find_elements(By.XPATH,'//nav[@class="oxd-topbar-body-nav"]')
        actual_page_headers = []
        expected_page_header = ["User Management","Job","Organization","Qualifications","Nationalities","Corporate Branding","Configuration"]
        for i in gettext:
            actual_page_headers = str(i.text).split("\n")
        for i in expected_page_header:
            if i not in actual_page_headers:
                is_test_case_passed = False
        if is_test_case_passed:
            print("TEST CASE RESULT: PASSED")
        else:
            print("TEST CASE RESULT: FAILED")
#----------------- TC_PIM_03------------------------------------
    def adminpage(self):
        gettext_1 = self.driver.find_elements(By.XPATH,'//ul[@class="oxd-main-menu"]')
        print("TEST CASE ID: TC_PIM_03")
        actual_admin_page_headers = []
        expected_admin_page_headers = ["Admin","PIM","Leave","Time","Recruitment","My Info","Performance","Dashboard","Directory","Maintenance","Buzz"]
        is_test_case_passed= True
        for i in gettext_1:
            actual_admin_page_headers = str(i.text).split("\n")
        for i in expected_admin_page_headers:
            if i not in actual_admin_page_headers:
                is_test_case_passed = False
        if is_test_case_passed:
            print("TEST CASE RESULT: PASSED")
        else:
            print("TEST CASE RESULT: FAILED")
orangehrm_1 = orangehrm()
orangehrm_1.setup()
orangehrm_1.forgetlink()
orangehrm_1.admin_headers()
orangehrm_1.adminpage()