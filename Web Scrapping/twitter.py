# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:28:11 2017
Updated on Sun Mar 19 08:52:55 2017
@author: Mohammed Yusuf Khan
"""

from selenium import webdriver
import time
#import codecs


url='https://twitter.com/WalkingDead_AMC'

#open the browser and visit the url
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)


#scroll down twice to load more tweets
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)


#find all elements with a class that ends in 'tweet-text'
tweets=driver.find_elements_by_css_selector("[data-item-type=tweet]")

"""
for tweet in tweets:
    print (tweet.find_element_by_css_selector("[class$=tweet-text"))
"""

#write the tweets to a file
fw=open('tweets.txt','w',encoding='utf-8')
for tweet in tweets:
    txt,retweets,fav,replies, date='NA','NA', 'NA', 'NA', 'NA'

    try: txt=tweet.find_element_by_css_selector("[class$=tweet-text]").text
    except: print ('no text')

    try:
        retweetElement=tweet.find_element_by_css_selector("[class$=js-actionRetweet]")
        retweets=retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text
    except:
        print ('no retweets')

#fav
    try:
        favElement = tweet.find_element_by_css_selector("[class$=js-actionFavorite]")
        fav = favElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text
    except:
        print("no favourites")

#replies
    try:
        replyElement = tweet.find_element_by_css_selector("[class$=js-actionReply]")
        replies = replyElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text
    except:
        print("no replies")
#date
    try:
        dateElement = tweet.find_element_by_css_selector("[class=time]")
        date = dateElement.find_element_by_css_selector('[data-long-form=true]').text
    except:
        print('no dates')


    fw.write(txt.replace('\n',' ')+'\t'+str(retweets)+ '\t' +str(fav)+ '\t'+ str(replies) + '\t' + str(date) +'\n')


fw.close()


driver.quit()#close the browser
