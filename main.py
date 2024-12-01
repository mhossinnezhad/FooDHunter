from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import TimeoutException, WebDriverException
import getpass
import csv
import sys
import time
import os
import colorama
import codecs
from colorama import Back, Fore, Style
from bidi.algorithm import get_display
from selenium.webdriver.common.by import By

colorama.init(autoreset=True)
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


def driver_load():
    print(Fore.MAGENTA + pFix("درحال بارگذاری درایور..."))
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("-private")  # Firefox's incognito mode
    driver = webdriver.Firefox(service=Service(
        GeckoDriverManager().install()), options=options)

    driver.set_window_size(800, 1000)
    options.set_preference("layout.css.devPixelsPerPx", "0.5")
    return driver


def print_loading_dots():
    sys.stdout.write(Fore.LIGHTGREEN_EX + pFix('درحال رزرو'))
    for i in range(4):
        sys.stdout.write(pFix('.'))
        sys.stdout.flush()
        time.sleep(0.005)
    sys.stdout.write('\r   \r')  # Clear the dots
    sys.stdout.flush()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.readlines()


def login():
    while True:
        print(Fore.LIGHTBLUE_EX + pFix('1:کاربر جدید'))
        print(Fore.LIGHTYELLOW_EX + pFix('2:حساب دارم'))
        print()
        option = input(Fore.LIGHTBLUE_EX + pFix(":گزینه ی خود را انتخاب کنید"))
        print("""++++++++++++++++++++++++++++""")
        if option == '1':
            name = input(Fore.LIGHTBLUE_EX + pFix(":نام خود را وارد کنید"))
            while True:
                username = input(
                    Fore.LIGHTBLUE_EX + pFix(":نام کاربری سامانه سماد خود را وارد کنید"))
                if len(username) == 13 or len(username) == 12 and username.isdigit():
                    break
                else:
                    print(Fore.RED + pFix("نام کاربری شما باید شامل 13 عدد باشد!"))
            password = getpass.getpass(pFix(": رمز عبور خود را وارد کنید"))
            print()
            print(Fore.MAGENTA + f" {pFix("خوش آمدید")}   {name}!")
            print()
            with open('usersnew.txt', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, username, password])
            return username, password
        elif option == '2':
            filename = 'usersnew.txt'
            with open(filename, 'r+') as file:
                reader = csv.reader(file)
                users = list(reader)
                for i, user in enumerate(users, start=1):
                    if i % 2 == 0:
                        print(Fore.LIGHTYELLOW_EX + f"{i}. {user[0]}")
                    else:
                        print(f"{i}. {user[0]}")
                user_index = int(
                    input(Fore.LIGHTBLUE_EX + pFix(":حساب خود را انتخاب کنید"))) - 1
                name, username, password = users[user_index]
                print(Fore.CYAN + f"{pFix("خوش آمدید")}  {name}!")

                return username, password
        else:
            print(Fore.RED + pFix("انتخاب اشتباه،لطفا دوباره تلاش کنید!"))


def show_options():
    options = ['2:markazi', '3:  tarbiat badani ', '4: Oulom paye',
               '5: somesara', '6: self service shargh', '7: keshavarzi']
    allowed_options = [2, 3, 4, 5, 6, 7]
    for i, option in enumerate(options, 1):
        print(f"{pFix(option)}")
    while True:
        print()
        selected_option = int(
            input(Fore.LIGHTBLUE_EX + pFix(":سلف مورد نظر را انتخاب کنید")))
        print()
        if selected_option in allowed_options:
            print()
            print(Fore.MAGENTA + f" {selected_option} {pFix(": انتخاب شما")}")
            print()
            return selected_option


def show_list_from_file(file_name):
    while True:

        print(Fore.LIGHTBLACK_EX + " back = Restart")

        user_input = input(Fore.LIGHTBLUE_EX +
                           pFix("غذای خود را انتخاب کنید:"))
        if user_input == 'back':
            main()
            continue
        else:
            try:
                selected_item = int(user_input)
                print(Fore.MAGENTA + f"You selected: {selected_item}")
                return selected_item
            except ValueError:
                print("Invalid input. Please enter a number or 'back'.")


def pFix(input_string):
    return get_display(input_string)


#      def replace_persian_with_english(input_string):
#          persian_to_english = {
#              'آ': 'a', 'ا': 'a', 'ب': 'b', 'پ': 'p', 'ت': 't', 'ث': 's', 'ج': 'j',
#              'چ': 'ch', 'ح': 'h', 'خ': 'kh', 'د': 'd', 'ذ': 'z', 'ر': 'r',
#              'ز': 'z', 'ژ': 'zh', 'س': 's', 'ش': 'sh', 'ص': 's', 'ض': 'z',
#              'ط': 't', 'ظ': 'z', 'ع': 'a', 'غ': 'gh', 'ف': 'f', 'ق': 'q',
#              'ک': 'k', 'گ': 'g', 'ل': 'l', 'م': 'm', 'ن': 'n', 'و': 'v',
#              'ه': 'h', 'ی': 'y'
#          }
#          output_string = ''.join([persian_to_english.get(char, char)
#                                  for char in input_string])
#          return output_string


# =========================================================

# =========================================================


def main():

    driver = driver_load()

    os.chdir('F:\\cmd foodhunter')
    print()
    print(Fore.GREEN + """
                                        ░░░░░░░░░░░░░░░▓▓█▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                        ░░░░░░░░░░░░░░░░░▓█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                        ░░░░░░░░░░░░░░░░░░███████████████████▒░░░░░░░░░░░░
                                        ░░░░░░░░░░░░░░░░░░▒█████████████████▓░░░░░░░░░░░░░
                                        ░░░░░░░░░░░░░░░░░░░█████████████████░░░░░░░░░░░░░░
                                        ░░░░░░░░░░░░░░░░░░░▒███████████████░░░░░░░░░░░░░░░
                                        ░░░░░░░░░░░░░░░░░░░░██████████████▒░░░░░░░░░░░░░░░
                                        ░░░░░░░░░░░░░░░░░░░░▒█▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░
                                        ░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░
                                        ░░░░░░░░░░░░░░░░░░░░░░▓██▓░░░░▓██▓░░░░░░░░░░░░░░░░
                                        ░░░░░░░░░░░░░░░░░░░░░░████░░░░███▓░░░░░░░░░░░░░░░░
""")
    print()
    print(Fore.GREEN + """
                                    █▀▀ █▀█ █▀█ █▀▄   █░█ █░█ █▄░█ ▀█▀ █▀▀ █▀█   █░█ ▄█ ░ █▀█
                                    █▀░ █▄█ █▄█ █▄▀   █▀█ █▄█ █░▀█ ░█░ ██▄ █▀▄   ▀▄▀ ░█ ▄ █▄█
""")
    print()
    print(Fore.LIGHTMAGENTA_EX + "Driver Ready!")
    print()
    print()

    # Use the copyfile function from the shutil module

    username, password = login()
    selected_option = show_options()
    counterForLoop = 0

    selfId = f'/html/body/div[6]/div[2]/div/table/tbody/tr[2]/td/div/select/option[{
        selected_option}]'

    driver.get("https://food.guilan.ac.ir/index.rose")
    driver.execute_script("document.body.style.zoom='40%'")

    driver.get("https://food.guilan.ac.ir/index.rose")
    # Adjust the timeout as needed (e.g., 10 seconds)
    wait = WebDriverWait(driver, 10)

    # Step 1: Wait for the checkbox to be visible and clickable, then click it
    checkbox = wait.until(EC.element_to_be_clickable(
        (By.ID, 'redirect-remember')))
    checkbox.click()

    # Step 2: Wait for the button to be visible and clickable, then click it
    button = wait.until(EC.element_to_be_clickable(
        (By.ID, 'btn-redirect-cancel')))
    button.click()
    # Enter username
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.ID, 'username'))).send_keys(username)

    # Enter password
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.ID, 'password'))).send_keys(password)

    # Click to login
    # Wait for the blocking element to disappear
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element((By.ID, "modal-redirect-confirm"))
    )

    # Now click the button after the modal disappears
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login_btn_submit"))
    )
    login_button.click()
    # Click the button once it is clickable

    driver.get("https://food.guilan.ac.ir/index/index.rose")

    # Wait for the span element to be clickable and click it
    span_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@onclick=\"openGeneralAjaxDialog('/nurture/user/multi/reserve/selectSelf.rose','رزرو غذا')\"]"))
    )
    span_element.click()

    # Wait for the generalAjaxDialogBodyDiv to be loaded
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "generalAjaxDialogBodyDiv")))

    # Click on the select element and choose the option with value "4"
    # =========================================================
    # Find the select element using its full XPath and wait until it's clickable
    select_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[6]/div[2]/div/table/tbody/tr[2]/td/div/select'))
    )

    # Click the select element to open the dropdown menu
    select_element.click()

    # Find the option element using its full XPath and wait until it's clickable
    option_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, selfId))
    )

    # Click the option element
    option_element.click()
    # =========================================================
    # Wait for the OK button to be clickable and click it
    ok_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@value='تایید و ادامه' and @onclick='checkSelectedSelfAndContinue()']"))
    )
    ok_button.click()
    driver.set_window_size(400, 600)

    # --------------------------------------------------------------------
    test = driver.find_elements(By.XPATH, '//*[contains(@id, "foodNameSpan")]')
    counterForLoop = 0
    for element in test:
        persian_text = element.text
        result = f"{pFix(persian_text)}"
        start = '|'
        end = '|'
        resultNew = [(result.split(start))[1].split(end)[0]]

        if counterForLoop % 2 == 0:
            print(f"{Fore.GREEN}{counterForLoop}: {resultNew}")
        else:
            print(f"{Fore.LIGHTGREEN_EX}{counterForLoop}: {resultNew}")

        counterForLoop += 1

    # =========================================================

    credit = driver.find_elements(By.XPATH, '//*[contains(@id, "creditId")]')
    for i in credit:
        creditCheck = []
        creditCheck.append(i.text)

    creditCheckBalance = int(creditCheck[0])
    print()
    print(Fore.RED + f"Etebar Hessab Shoma =  {creditCheckBalance} ")
    print()
    if creditCheckBalance <= -540000:

        print()
        print(Fore.LIGHTRED_EX + "ETEBAR KAFI NIST!!!!!!!")
        print(Fore.LIGHTRED_EX + "LOTFAN HESAB KHOD RA CHARGE KONID!")
        print()
        print()

    elif creditCheckBalance < -540000:
        print(Fore.LIGHTRED_EX + "Etebar shoma momken ast kafi nabashad!")

    # =========================================================

    selected_item = show_list_from_file('foodList.txt')
    foodId = f"//*[@id='buyFreeFoodIconSpanuserWeekReserves.selected{
        selected_item}']/img"
    # --------------------------------------------------------------------

    def check_and_click():
        # Wait for the image to appear

        # Check if the specific ID is present
        if driver.find_elements(By.XPATH, foodId):
            # Click the dynamic ID element
            driver.find_element(
                By.XPATH, foodId).click()
            WebDriverWait(driver, 20).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
            driver.find_element(By.ID, 'doReservBtn').click()
            return True

        return False
    # Main loop to refresh the page and check for the image
    reservation_made = False
    while not reservation_made:
        driver.refresh()  # Refresh the webpage
        print_loading_dots()  # Wait for 0.1 seconds
        # Check for the image and click if it's there
        reservation_made = check_and_click()

        # Close the log file

    print(Fore.LIGHTGREEN_EX + """

                                    ████████████████████████████████████████████████████████████████

     """)
    print(Fore.GREEN + """
                                    ███╗░░██╗░█████╗░░██████╗██╗░░██╗  ░░░░░██╗░█████╗░███╗░░██╗██╗
                                    ████╗░██║██╔══██╗██╔════╝██║░░██║  ░░░░░██║██╔══██╗████╗░██║██║
                                    ██╔██╗██║██║░░██║╚█████╗░███████║  ░░░░░██║███████║██╔██╗██║██║
                                    ██║╚████║██║░░██║░╚═══██╗██╔══██║  ██╗░░██║██╔══██║██║╚████║╚═╝
                                    ██║░╚███║╚█████╔╝██████╔╝██║░░██║  ╚█████╔╝██║░░██║██║░╚███║██╗
                                    ╚═╝░░╚══╝░╚════╝░╚═════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝
""")
    print(Fore.LIGHTGREEN_EX + """

                                    ████████████████████████████████████████████████████████████████

     """)

    def restart_program():

        print("1. Restart program")
        print("2. Do you need Qrcode?")
        print("3. Exit program")

        user_input = input(
            "Do you want to restart the program? (1 for yes/2 for no): ")
        if user_input == "1":
            driver.quit()
            main()  # Ensure `main` function is defined elsewhere

        if user_input == "2":
            driver.get("https://samad.app/login")

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(By.XPATH(
                "/html/body/div[1]/div/div/div[2]/div[1]/div/div[3]/div[1]/div/span/svg"))).click()

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/input'))).send_keys("دانشگاه گیلان")

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, '//li[contains(text(), "دانشگاه گیلان")]'))).click()

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/button/span/svg')).click()

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div[3]/div[2]/input'))).send_keys(username)

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div[3]/div[3]/span/input'))).send_keys(password)

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div[3]/button'))).click()

        elif user_input == "3":
            print("Exiting the program.")
            driver.quit()
        else:
            print("Invalid input. Please enter '1' for yes or '2' for no.")
            restart_program()

    restart_program()


if __name__ == "__main__":
    main()
    input("press enter to exit.")
