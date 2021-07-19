from selenium import webdriver
# import org.openqa.selenium.interactions.Actions
from selenium.webdriver.common.keys import Keys
import time

class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/')
        time.sleep(4)

        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

        time.sleep(10)
        bot.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        try:
            time.sleep(5)
            bot.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        except:
            print("Button not found")
        # self.logout()

    def logout(self):
        bot = self.bot
        time.sleep(2)
        bot.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span').click()
        time.sleep(10)
        bot.find_element_by_xpath("//div[contains(text(), 'Log Out')]").click()

    def changepassword(self,pwd):
        bot = self.bot
        time.sleep(2)
        bot.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span').click()

        time.sleep(2)
        bot.find_element_by_xpath("//div[contains(text(), 'Settings')]").click()

        time.sleep(5)
        bot.find_element_by_xpath("//a[contains(text(), 'Change Password')]").click()

        time.sleep(2)
        oldpassword = bot.find_element_by_name('cppOldPassword')
        newpassword = bot.find_element_by_name('cppNewPassword')
        confirmpassword = bot.find_element_by_name('cppConfirmPassword')
        oldpassword.clear()
        newpassword.clear()
        confirmpassword.clear()
        oldpassword.send_keys(self.password)
        newpassword.send_keys(pwd)
        confirmpassword.send_keys(pwd)

        self.password = pwd
        time.sleep(2)
        bot.find_element_by_xpath("//button[contains(text(), 'Change Password')]").click()

    def likeposts(self):
        scrolltimes = 4
        while scrolltimes > 0:
            bot = self.bot
            time.sleep(2)
            # getting all the posts currently displayed on the page
            posts = bot.find_elements_by_xpath("//article[@role='presentation']")

            # first getting the number of posts on a page
            numberofposts = 0
            for post in posts:
                numberofposts += 1
            # using the number of posts to run a loop that'll like all using XPATH
            count = 1
            while numberofposts > 0:
                postpath = f"/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[{count}]/div[3]/section[1]/span[1]/button"
                bot.find_element_by_xpath(postpath).click()
                time.sleep(2)
                count += 1
                numberofposts -= 1
            # SCROLLING to the bottom to load more posts
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            # DECREASING THE SCROLLTIME variable BY 1
            scrolltimes -= 1
            # TIME to wait in-between SCROLLS
            time.sleep(8)

    def likepostsUsingDoubleClick(self):
        scrolltimes = 4
        while scrolltimes > 0:
            bot = self.bot
            time.sleep(2)
            # getting all the posts currently displayed on the page
            posts = bot.find_elements_by_xpath("//article[@role='presentation']")

            # first getting the number of posts on a page
            numberofposts = 0
            for post in posts:
                numberofposts += 1
            # using the number of posts to run a loop that'll like all using XPATH
            count = 1
            while numberofposts > 0:
                postpath = f"/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[{count}]/div[2]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div"
                bot.find_element_by_xpath(postpath).click()
                # Actions action = new Actions(driver);
                # WebElement
                # link = driver.findElement(By.xpath("//button[text()='Double-Click Me To See Alert']"));
                # action.doubleClick(link).perform();
                time.sleep(2)
                count += 1
                numberofposts -= 1
            # SCROLLING to the bottom to load more posts
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            # DECREASING THE SCROLLTIME variable BY 1
            scrolltimes -= 1
            # TIME to wait in-between SCROLLS
            time.sleep(8)

uname = input("Enter username: ")
pwd = input("Enter password: ")

IB = InstaBot(uname,pwd)

IB.login()
IB.changepassword(pwd)
# IB.likeposts()
