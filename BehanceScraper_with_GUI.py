#! python3
# BehanceScraper_with_GUI.py - asks user how many likes and views post must be on post
# to scrape it and how many posts file should contains, opens "https://www.behance.net/" and saves posts into Excel.
# Will be taken title, number of likes, number of views and post link.
# File will be saved with unique date time.
# It is needed to download Chrome driver before for your Chrome version and put it to working directory, link = http://chromedriver.chromium.org/downloads

import tkinter as tk
import tkinter.ttk, datetime, time, bs4, openpyxl, sys, pymsgbox, threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

root = tk.Tk()
root.title('Behance Scraper')

main_canvas = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
main_canvas.pack()

main_label = tk.Label(root, text='Please specify the following variables')
main_label.config(font=('helvetica', 14))
main_canvas.create_window(200, 30, window=main_label)

# Likes input form
likes_label = tk.Label(root, text='Enter how many likes post must have:')
likes_label.config(font=('helvetica', 10))
main_canvas.create_window(112, 100, window=likes_label)

likes_input = tk.Entry(root)
main_canvas.create_window(290, 100, window=likes_input)

# Views input form
views_label = tk.Label(root, text='Enter how many views post must have:')
views_label.config(font=('helvetica', 10))
main_canvas.create_window(114, 125, window=views_label)

views_input = tk.Entry(root)
main_canvas.create_window(290, 125, window=views_input)

# File posts form
posts_label = tk.Label(root, text='Enter how many posts file should have:')
posts_label.config(font=('helvetica', 10))
main_canvas.create_window(115, 150, window=posts_label)

posts_input = tk.Entry(root)
main_canvas.create_window(290, 150, window=posts_input)

# Entered variables checking function
error_label_bool = False # starting error label condition
def variables_checking():
    global error_label_bool
    global error_label
    global likes_number
    global views_number
    global general_number

    # Get result from input forms
    likes_number = likes_input.get()
    views_number = views_input.get()
    general_number = posts_input.get()

    # Delete already existing error label
    if error_label_bool != False:
        error_label.destroy()

    # Print the error label
    if (
        not likes_number.isdecimal() or \
        not views_number.isdecimal() or \
        not general_number.isdecimal()
        ):
        error_label = tk.Label(root, text='Error: Input variables are not valid!')
        error_label.config(bg='red', fg='white', font=('helvetica', 12, 'bold'))
        main_canvas.create_window(200, 250, window=error_label)
        error_label_bool = True
        return None

    # Ask to confirm the entered values and start the scraping
    if (
        likes_number.isdecimal() and \
        views_number.isdecimal() and \
        general_number.isdecimal()
        ):
        error_label_bool = False
        answer = pymsgbox.confirm(text='Are you sure to continue with entered values?')
        if answer == pymsgbox.CANCEL_TEXT:
            return None
        else:
            scrape_with_progress_bar()

# Scrape function
def scrape_with_progress_bar():
    # Scrape function itself
    def scrape():
        global current_likes_number
        global current_views_number
        global current_general_number_amount
        global general_number
        likes_input.delete(0, 'end')
        views_input.delete(0, 'end')
        posts_input.delete(0, 'end')
        
        # open Excel and fill the headers out
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = 'Posts'
        sheet['A1'] = 'Title'
        sheet['B1'] = 'Likes'
        sheet['C1'] = 'Views'
        sheet['D1'] = 'Post Link'

        # Progress bar
        progress = tkinter.ttk.Progressbar(root, orient=tk.HORIZONTAL, length=100, mode='determinate')
        progress.pack()
        
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
                root.update_idletasks()
                pymsgbox.alert(title='Behance Scraper', text='Program is being closed due to exceeded amount of entered posts comparing' + \
                               ' to existing posts amount on website.\nCurrent work progress is saved.', icon=pymsgbox.WARNING)
                progress.forget()
                scrape_button.configure(state='normal')
                sys.exit()
            while True:
                # Write posts data to Excel
                for post in range(current_searched_posts_amount, len(posts_bs4)):
                    current_likes_number = ''.join(posts_bs4[post].select('.Stats-stats-1iI')[0].text.split('\n')[1].strip().split(','))
                    current_views_number = ''.join(posts_bs4[post].select('.Stats-stats-1iI')[0].text.split('\n')[3].strip().split(','))
                    if int(current_likes_number) >= int(likes_number) and int(current_views_number) >= int(views_number):
                        if current_general_number_amount != 0:
                            # Update the progress bar
                            progress['value'] = int(current_general_number_amount * 100 / int(general_number))
                            root.update_idletasks()
                        current_general_number_amount = current_general_number_amount + 1
                        
                        if current_general_number_amount > int(general_number):
                            current_time = datetime.datetime.now()
                            wb.save('Behance_Posts__' + str(current_time.year) + str(r'-') + str(current_time.month) + str(r'-') + str(current_time.day) + str(r'__') + \
                                str(current_time.hour) + str(r'-') + str(current_time.minute) + str(r'-') + str(current_time.second) + '.xlsx')
                            progress['value'] = int(current_general_number_amount * 100 / int(general_number))
                            root.update_idletasks()
                            pymsgbox.alert(title='Behance Scraper', text='Scraping finished successfully')
                            progress.forget()
                            scrape_button.configure(state='normal')
                            sys.exit()
                        else:
                            sheet['A' + str(current_general_number_amount + 1)] = posts_bs4[post].select('div[data-slug]')[0].get('data-slug')
                            sheet['B' + str(current_general_number_amount + 1)] = current_likes_number
                            sheet['C' + str(current_general_number_amount + 1)] = current_views_number
                            sheet['D' + str(current_general_number_amount + 1)] = posts_bs4[post].select('a')[2].get('href')
                            continue
                # Continue the loop
                current_searched_posts_amount = len(posts_bs4)
                htmlElem.send_keys(Keys.END)
                break
        
    scrape_button.configure(state='disabled')
    threading.Thread(target=scrape).start()

# Scrape button
scrape_button = tk.Button(text='Scrape the Behance', command=variables_checking, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
main_canvas.create_window(200, 200, window=scrape_button)

root.mainloop()
