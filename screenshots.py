#! python3

## Take a list of hostnames or IPs and screenshot websites

from selenium import webdriver
import os,sys

if len(sys.argv) !=3:
    print('Usage: screenshots.py <path to save in> <IP/hostname file>')
    sys.exit(1)

## Pass directory where to save screenshots and the host list to takeScreenshot function
def takeScreenshot(saveDir, ipList):
    chromeDriver = 'chromedriver'
    driver = webdriver.Chrome(chromeDriver)

    ## change to directory you want files saved in
    os.chdir(saveDir)

    ## Open URL and save screenshot
    driver.set_window_size(1920,1080)
    driver.get('https://' + ipList)
    savefile = ipList + '.png'
    driver.get_screenshot_as_file(savefile)
    driver.quit()   

screenshotDir = sys.argv[1]
listFile = sys.argv[2]

infile = open(listFile).read().splitlines()
for host in infile:
    takeScreenshot(screenshotDir, host)





