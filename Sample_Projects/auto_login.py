from selenium import webdriver
from getpass import getpass

username = "dlqateams@gmail.com"
password = "M@nh@tt@n2021$!"

driver = webdriver.Chrome("/home/amit/Downloads/chromedriver")
driver.get("https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26state%3DhashArgsFromTB_us-west-2_d684a5cd78503d19&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge=d_UR8uhra4rLimX1nVchhzwdaqrWJO-QV1JHZDMeqRA&code_challenge_method=SHA-256")

username_entry = driver.find_element_by_id("resolving_input")
username_entry.send_keys(username)

next_button = driver.find_element_by_css_selector("#next_button")
next_button.click()

password_entry = driver.find_element_by_id("password")
password_entry.send_keys("password")

signin_button = driver.find_element_by_id("signin_button")
signin_button.submit()