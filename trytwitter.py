from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import os
import csv

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def enter_text(field,text):
    for x in text:
        field.send_keys(x)
        time.sleep(random.uniform(1, 5))

def csv_poprow(path):
    try:
        if os.path.exists(path):
            with open(path,'r',newline='',encoding='utf-8') as f:
                rows = list(csv.reader(f))

        if rows:
            row = rows[0]
            print(f'processing row: {row}')
            rows.pop(0)

            with open(path,'w',newline='',encoding='utf-8') as f2:
                writer = csv.writer(f2)
                writer.writerows(rows)
            
            print("processed row is deleted")
            return row
        else:
            print("No rows to process")
            return None
    except Exception as e:
        print("Cannot open the file coz of " + str(e))
        return None
    return None
def get_Quote(driver):
    try:
        driver.get("https://chat.openai.com")
        print("Loading Chatgpt..")
    except Exception as e:
        print("Couldnt Enter ChatGPT coz of " + str(e))
        return False
    try:
        WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//button[@data-testid='login-button']"))
        )
        login_button = driver.find_element(By.XPATH,"//button[@data-testid='login-button']")
        login_button.click()
        try:
            WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//input[@type='checkbox']"))
            )
        except:
            print("No checkbox found")
        finally:
            checkbox_field = driver.find_element(By.XPATH,"//input[@type='checkbox']")
            checkbox_field.click()
        
        WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//input[@name='email']"))
        )
        email_field = driver.find_element(By.XPATH,"//input[@name='email']")
        email_field.send_keys("sliitbook@gmail.com")
        email_field.send_keys(Keys.RETURN)
        WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//input[@name='password']"))
        )
        password_field = driver.find_element(By.XPATH,"//input[@name='password']")
        password_field.send_keys("apiapiapiapi")
        password_field.send_keys(Keys.RETURN)
    except Exception as e:
        print("Couldnt able to login coz of " + str(e))

    try:
        WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//div[@id='prompt-textarea']"))
        )
        input_field = driver.find_element(By.XPATH,"//div[@id='prompt-textarea']")
        input_field = input_field.find_element(By.XPATH,"//p")
        enter_text(input_field,"Quote of the hour")
        time.sleep(2)
        input_field.send_keys(Keys.RETURN)
        # # WebDriverWait(driver,10).until(
        #     EC.presence_of_element_located((By.XPATH,"//button[@aria-label='Send prompt']"))
        # )
        time.sleep(30)
    except Exception as e:
        print("Couldn't Enter prompt coz of " + str(e))
        return False
    try:
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label='Send prompt']")))
        # button = driver.find_element(By.XPATH,"//button[@aria-label='Send prompt']")
        # button.click()
        WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//div[@data-message-author-role='assistant']"))
        )
        quote = driver.find_element(By.XPATH,"//div[@data-message-author-role='assistant']").text
        return quote
    except Exception as e:
        print("Couldnt get Response coz of " + str(e))
        return False
class Twitter:
    def __init__(self,username,password,email,driver):
        self.username = username
        self.password = password
        self.email = email
        self.driver = driver
    
    def login(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(3)
        print("Navigating to Login Page")    
        #username
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//input[@name='text']"))
            )
        except Exception as e:
            print("Unable to locate Username Field coz of " + str(e))
            return False
        finally:
            username_field = self.driver.find_element(By.XPATH, "//input[@name='text']")
            username_field.send_keys(self.username)
            username_field.send_keys(Keys.RETURN)
            print("Entered Username")

        #email 
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//span[contains(text(), 'email')]"))
            )
            email_field = self.driver.find_element(By.XPATH, "//input[@name='text']")
            email_field.send_keys(self.email)
            email_field.send_keys(Keys.RETURN)
            print("Email Entered")
        except:
            print("Dosen't Require Email")

        #password
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//input[@name='password']"))
            )
        except Exception as e:
            print("Unable to locate Password Field coz of " + str(e))
            return False
        finally:
            password_field = self.driver.find_element(By.XPATH, "//input[@name='password']")
            password_field.send_keys(self.password)
            password_field.send_keys(Keys.RETURN)
            print("Entered Password")
           #email 
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//span[contains(text(), 'email')]"))
            )
            email_field = self.driver.find_element(By.XPATH, "//input[@name='text']")
            email_field.send_keys(self.email)
            email_field.send_keys(Keys.RETURN)
            print("Email Entered")
        except:
            print("Dosen't Require Email")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Timeline: Trending now']"))
            )
        except Exception as e:
            print("Unable to Login in coz of " + str(e))
            return False
        finally:
            print("Logged in Successfully")

        return True

    def trending_topics(self):
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//div[contains(@aria-label, 'Timeline: Trending now')]"))
            )
            trending_section = self.driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Timeline: Trending now')]")
            trending_topics = trending_section.find_elements(By.XPATH, ".//div[@dir='ltr']")

            top_trends = [topic.text for topic in trending_topics[:5]]

            print("Top 5 Trending Topics:")
            for idx, trend in enumerate(top_trends, start=1):
                print(f"{idx}. {trend}")

        except Exception as e:
            print("Trending section not found")

    def post_text(self,content):
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//a[@href='/compose/post']"))
            )
        except Exception as e:
            print("Couldnt able find post link because of " + str(e))
            return False
        try:
            link = self.driver.find_element(By.XPATH,"//a[@href='/compose/post']")
            link.click()
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//button[@data-testid='tweetButton']"))
            )
            content_field = self.driver.find_element(By.XPATH,"//div[@aria-label='Post text']")
            content_field.click()
            content_field.send_keys(content)
            post_button = self.driver.find_element(By.XPATH,"//button[@data-testid='tweetButton']")
            post_button.click()
        except Exception as e:
            print("Couldnt able to post because of " + str(e))
            return False
        time.sleep(5)
        print("Posted Successfully")
        return True
    
    def search(self,topic):
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//a[@href='/explore']"))
            )
        except Exception as e:
            print("Couldnt able find search link because of " + str(e))
            return False
        try:
            link = self.driver.find_element(By.XPATH,"//a[@href='/explore']")
            link.click()
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Search']"))
            )
            search_field = self.driver.find_element(By.XPATH,"//input[@placeholder='Search']")
            search_field.click()
            search_field.send_keys(topic)
            search_field.send_keys(Keys.RETURN)
        except Exception as e:
            print("Couldnt able to search because of " + str(e))
            return False

        print("Searched Successfully")
        
        
        res = []
        cnt = 10
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//article"))
        )
        article = self.driver.find_element(By.XPATH,"//article")    
        while cnt > 0:
            cnt = cnt - 1
            self.driver.execute_script("arguments[0].scrollIntoView(true);", article)
            article_height = self.driver.execute_script("return arguments[0].offsetHeight;", article)
            username = article.find_element(By.XPATH,".//span[@class='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3']").text
            t = article.find_element(By.XPATH,".//time[@datetime]").text            
            content_tags = article.find_element(By.XPATH,".//div[@data-testid='tweetText']")  
            content_tags = content_tags.find_elements(By.XPATH,".//span")
            content = " ".join(content_tag.text for content_tag in content_tags)
            res.append( 
                {
                    "username":username,
                    "t":t,
                    "content":content
                }
            )
            self.driver.execute_script(f"window.scrollBy(0, {article_height + 2});")
            try:
                WebDriverWait(self.driver,10).until(
                    EC.presence_of_element_located((By.XPATH,"//article"))
                )
                article = self.driver.find_element(By.XPATH,"//article")    
            except:
                print("No more articles")
                break
        return res
    

    

chrome_options = Options()
chrome_options.add_argument("--headless")
# chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--incognito")

CHROMEDRIVER_PATH = "./chromedriver.exe"
#brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
#chrome_options.binary_location = brave_path
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
quote_row = csv_poprow("./new_quotes.csv")

if quote_row != None:
    quote = '"' + quote_row[0] + '"' + ' - ' + color.BOLD + quote_row[1] + color.END
    print(quote)
    bot = Twitter("QuoteofdeDay","Quoteoftheyear","sliitbook@gmail.com",driver)
    bot.login()
    bot.post_text(quote)
#bot.trending_topics()
#v = bot.search("Donald Trump")
#for tweet in v:
    #print(f'username is {tweet["username"]}')
    #print(f'time is {tweet["t"]}')
    #print(f'content is {tweet["content"]}')
    #print("")

