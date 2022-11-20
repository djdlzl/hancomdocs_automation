import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import threading
import multiprocessing



# 시간에 맞게 변경
dir_date_time = '20221121_07'
dir_date = '20221121'


url = ['https://workdocs-collab-edit-iad.awsapps.com/workdocs/index.html#/mydocs', 
'https://workdocs-collab-edit-dub.awsapps.com/workdocs/index.html#/mydocs', 'https://workdocs-collab-edit-nrt.awsapps.com/workdocs/index.html#/mydocs', 
'https://workdocs-collab-edit-syd.awsapps.com/workdocs/index.html#/mydocs', 'https://workdocs-collab-edit-sin.awsapps.com/workdocs/index.html#/mydocs', 
'https://thinkfree.awsapps.com/workdocs/index.html#/mydocs'];
url_oregon = 'https://thinkfree.awsapps.com/workdocs/index.html#/mydocs';
url_virginia = 'https://workdocs-collab-edit-iad.awsapps.com/workdocs/index.html#/mydocs';
url_dublin = 'https://workdocs-collab-edit-dub.awsapps.com/workdocs/index.html#/mydocs';
url_tokyo = 'https://workdocs-collab-edit-nrt.awsapps.com/workdocs/index.html#/mydocs';
url_sidney = 'https://workdocs-collab-edit-syd.awsapps.com/workdocs/index.html#/mydocs';
url_singapore = 'https://workdocs-collab-edit-sin.awsapps.com/workdocs/index.html#/mydocs';
workdocs_id = 'noc@bespinglobal.com'
workdocs_passwd = 'sjaksahffk.123!@#'
test = 'test'


def init_driver():
    driver_options = webdriver.ChromeOptions();
    driver_options.add_experimental_option("detach", True);
    driver_options.add_experimental_option("excludeSwitches", ['enable-logging']);
    driver = webdriver.Chrome(options=driver_options);
    # driver_options = webdriver.EdgeOptions();
    # driver_options.add_experimental_option("detach", True);
    # driver_options.add_experimental_option("excludeSwitches", ['enable-logging']);
    # driver = webdriver.Edge(options=driver_options); 
    
      
    return driver;
    



def workdocs_login_email(driver):
    # driver.find_element(By.XPATH, '//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[2]/a').click();
    driver.find_element(By.XPATH, '//*[@id="emailId"]').click();
    driver.find_element(By.XPATH, '//*[@id="emailId"]').send_keys(workdocs_id)
    driver.find_element(By.XPATH, '//*[@id="login"]').click();
    time.sleep(5);
    # driver.implicitly_wait(5);
    pyautogui.press('esc');
    # driver.find_elemet().send_keys(Keys.ESCAPE);
    # driver.execute_script("document.addEventListener('escape',(event));");
    # driver.execute_script("window.close()");
    # webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform();
    # time.sleep(2);
    driver.implicitly_wait(10);
    driver.find_element(By.XPATH, '//*[@id="wdc_username"]').click();
    driver.find_element(By.XPATH, '//*[@id="wdc_username"]').send_keys(workdocs_id)
    driver.find_element(By.XPATH, '//*[@id="wdc_password"]').click();
    driver.find_element(By.XPATH, '//*[@id="wdc_password"]').send_keys(workdocs_passwd)
    driver.find_element(By.XPATH, '//*[@id="wdc_login_button"]').click();

def workdocs_enter_directory(driver):
    driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').click();
    driver.implicitly_wait(5);
    driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').click();
    driver.implicitly_wait(5);
    driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').click();
    driver.implicitly_wait(5);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); #생성
    driver.implicitly_wait(2);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[4]/a').click(); #폴더
    time.sleep(1.5);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').click();
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').send_keys(dir_date_time);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/a').click(); # 폴더 생성 완료
    time.sleep(2.5);
    driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[1]').click(); # 생성된 폴더 들어가기


def workdocs_enter_directory_date(driver):
    driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').click();
    driver.implicitly_wait(5);
    driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').click();
    driver.implicitly_wait(5);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); #생성
    driver.implicitly_wait(2);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[4]/a').click(); #폴더
    time.sleep(1.5);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').click();
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').send_keys(dir_date);
    time.sleep(1.5);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/a').click(); # 폴더 생성 완료
    time.sleep(2.5);
    driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[1]').click(); # 생성된 폴더 들어가기
    driver.implicitly_wait(5);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); #생성
    driver.implicitly_wait(2);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[4]/a').click(); #폴더
    time.sleep(1.5);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').click();
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').send_keys(dir_date_time);
    time.sleep(1.5);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/a').click(); # 폴더 생성 완료
    time.sleep(2.5);
    driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').click();

def workdocs_create_docs(driver):
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); #생성 버튼
    driver.implicitly_wait(2);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[1]/a').click();
    time.sleep(30); #docs가 자바스크립트라 implicitly로 하면 안됨.
    # driver.implicitly_wait(30);
    # Docs = driver.find_elements(By.XPATH, '//*[@id="page_52524923"]/div[2]/div'); #문서 클릭
    # driver.execute_script('arguments[0].click();', Docs)
    # ActionChains.send_keys("test").perform();
    # driver.find_element(By.XPATH, '//*[@id="page_38743858"]/div[2]/div').send_keys(test); #
    # time.sleep(5);
    driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[2]/div[1]/button').click(); #나가기 버튼
    time.sleep(1.5);
    driver.find_element(By.XPATH, '//*[@id="mainTitleBar"]/div/span/span[2]/secondary-nav/div/ul/li[1]/a').click(); #< 버튼
    time.sleep(0.5);
    driver.find_element(By.XPATH, '//*[@id="mainTitleBar"]/div/span/span[2]/secondary-nav/div/ul/li[1]/ul/li[4]/a').click(); #폴더로 나가기
    time.sleep(1.5);
    driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').click();
    time.sleep(1.5);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); #생성 버튼
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[2]/a').click(); #시트 생성
    time.sleep(30);
    driver.implicitly_wait(10);
    driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[2]/div[1]/button').click(); #나가기 버튼
    time.sleep(2.5);
    driver.find_element(By.XPATH, '//*[@id="mainTitleBar"]/div/span/span[2]/secondary-nav/div/ul/li[1]/a').click(); #< 버튼
    time.sleep(1.5);
    driver.find_element(By.XPATH, '//*[@id="mainTitleBar"]/div/span/span[2]/secondary-nav/div/ul/li[1]/ul/li[5]/a').click(); #폴더로 나가기
    time.sleep(0.5);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); # 생성 버튼
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[3]/a').click(); #프레젠테이션 생성
    time.sleep(30);
    driver.implicitly_wait(10);
    driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[2]/div[1]/button').click(); #나가기 버튼
    time.sleep(1);
    driver.find_element(By.XPATH, '//*[@id="mainTitleBar"]/div/span/span[2]/secondary-nav/div/ul/li[1]/a').click(); #< 버튼
    driver.find_element(By.XPATH, '//*[@id="mainTitleBar"]/div/span/span[2]/secondary-nav/div/ul/li[1]/ul/li[5]/a').click(); #폴더로 나가기

def execute_method(url, i):
    if url[i] == url[5]:
        time.sleep(1);
        driver = init_driver();
        # handle = driver.window_handles
        # driver.execute_script('window.open("about:blank", "_blank");')
        # driver.switch_to.window(handle[i])
        driver.get(url[i]);
        driver.implicitly_wait(10);
        workdocs_login_email(driver);
        driver.implicitly_wait(10);
        workdocs_enter_directory(driver);
        # workdocs_enter_directory_date(driver);
        time.sleep(2.5);
        workdocs_create_docs(driver);
    else:
        driver = init_driver();
        # handle = driver.window_handles
        # driver.execute_script('window.open("about:blank", "_blank");')
        # driver.switch_to.window(handle[i])
        driver.get(url[i]);
        driver.implicitly_wait(10);
        workdocs_login_email(driver);
        driver.implicitly_wait(10);
        workdocs_enter_directory(driver);
        # workdocs_enter_directory_date(driver);
        time.sleep(2.5);
        workdocs_create_docs(driver);

    print(url[i], "complete");
    

if  __name__  ==  "__main__" :
    
    start = time.localtime();
    print((start[3]));
    for i in range(len(url)):
        t = threading.Thread(target=execute_method, args=[url, i]);
        t.start();

    # driver = init_driver();
    # # handle = driver.window_handles
    # # driver.execute_script('window.open("about:blank", "_blank");')
    # # driver.switch_to.window(handle[i])
    # driver.get(url[0]);
    # driver.implicitly_wait(10);
    # workdocs_login_email(driver);
    # driver.implicitly_wait(10);
    # # workdocs_enter_directory(driver);
    # workdocs_enter_directory_date(driver);
    # time.sleep(2.5);
    # workdocs_create_docs(driver);

        

    end = time.time();

    print("수행시간: %f초" % (end - start));
    

    
    # driver.get(url_dublin);    
    # driver.implicitly_wait(7);
    # workdocs_login_email(driver);
    # driver.implicitly_wait(10);
    # workdocs_enter_directory(driver);
    # time.sleep(2.5);
    # workdocs_create_docs(driver);



    

# driver = uc.Chrome(use_subprocess=True)
# url = 'https://www.hancomdocs.com/'
# driver.get(url)

# driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/header/div/div/div/div[2]/button[1]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/main/article/div[1]/button[1]').click()
# driver.find_element(By.XPATH, '//*[@id="identifierId"]').click()
# driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('trackingitest')
# driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()