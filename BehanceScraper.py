#! python3
# behance.py - asks user how many likes and views post must be on post
# to scrape it and how many posts file should contains, opens "https://www.behance.net/" and saves posts into Excel.
# Will be taken title, number of likes, number of views and post link.
# File will be saved with unique date time.
# It is needed to download Chrome driver before for your Chrome version and put it to working directory, link = http://chromedriver.chromium.org/downloads


import datetime, time, bs4, openpyxl, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Ask user for post likes, views and file posts
while True:
    likes_number = input('Enter how many likes post must have:',)
    if likes_number.isdecimal():
        likes_number = int(likes_number)
        print('\n')
        break
    else:
        print('Please specify the value by typing digits!')
        continue
while True:
    views_number = input('Enter how many views post must have:',)
    if views_number.isdecimal():
        views_number = int(views_number)
        print('\n')
        break
    else:
        print('Please specify the value by typing digits!')
        continue
while True:
    print('---------NOTE---------\nPROGRAM WILL EXIT IF ENTERED AMOUNT OF POSTS EXCEEDS EXISTING AMOUNT WITH SPECIFIED VALUES\n---------NOTE---------')
    general_number = input('Enter how many posts file should have:',)
    if general_number.isdecimal():
        general_number = int(general_number)
        print('\n')
        break
    else:
        print('Please specify the value by typing digits!')
        continue

# open Excel and fill the headers out
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Posts'
sheet['A1'] = 'Title'
sheet['B1'] = 'Likes'
sheet['C1'] = 'Views'
sheet['D1'] = 'Post Link'

# Open website
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.behance.net/')

# Find posts
current_searched_posts_amount   = 0     # start variable for searched posts amount
current_general_number_amount   = 0     # start variable for written posts down
while True:
    time.sleep(7)
    htmlElem = browser.find_element_by_tag_name('html')
    posts = browser.find_elements_by_class_name('ContentGrid-grid-1EY')
    posts_bs4 = bs4.BeautifulSoup(posts[0].get_attribute('innerHTML'), features="lxml")
    posts_bs4 = posts_bs4.select('li')
    if len(posts_bs4) == current_searched_posts_amount:
        wb.save('Behance_Posts__' + str(current_time.year) + str(r'-') + str(current_time.month) + str(r'-') + str(current_time.day) + str(r'__') + \
            str(current_time.hour) + str(r'-') + str(current_time.minute) + str(r'-') + str(current_time.second) + '.xlsx')
        print('Program is being closed due to exceeded amount of entered posts comparing to existing posts amount on website.\nCurrent work progress is saved.')
        sys.exit()
    while True:
        # Write posts data to Excel
        for post in range(current_searched_posts_amount, len(posts_bs4)):
            current_likes_number = posts_bs4[post].select('.Stats-stats-1iI')[0].text.split('\n')[0].strip()
            current_views_number = posts_bs4[post].select('.Stats-stats-1iI')[0].text.split('\n')[1].strip()
            if int(current_likes_number) >= likes_number and int(current_views_number) >= views_number:
                if current_general_number_amount != 0:
                    # Printing the progress
                    print('Already saved ' + str(current_general_number_amount) + ' of ' + str(general_number) + ' posts.')
                current_general_number_amount = current_general_number_amount + 1
                if current_general_number_amount > general_number:
                    current_time = datetime.datetime.now()
                    wb.save('Behance_Posts__' + str(current_time.year) + str(r'-') + str(current_time.month) + str(r'-') + str(current_time.day) + str(r'__') + \
                        str(current_time.hour) + str(r'-') + str(current_time.minute) + str(r'-') + str(current_time.second) + '.xlsx')
                    print('------------------------------------------\nDone.')
                    sys.exit()
                else:
                    sheet['A' + str(current_general_number_amount + 1)] = posts_bs4[post].select('div[data-slug]')[0].get('data-slug')
                    sheet['B' + str(current_general_number_amount + 1)] = current_likes_number
                    sheet['C' + str(current_general_number_amount + 1)] = current_views_number
                    sheet['D' + str(current_general_number_amount + 1)] = posts_bs4[post].select('a')[0].get('href')
                    continue
        # Continue the loop
        current_searched_posts_amount = len(posts_bs4)
        htmlElem.send_keys(Keys.END)
        break

