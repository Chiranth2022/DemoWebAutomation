from selenium.webdriver import Chrome
driver=Chrome()
class Registrationpage:
    def click_on_register_link():
        driver.find_element('id',"register").click()

ob1= Registrationpage()  
print(ob1.__dict__)
print("helo chiranth")