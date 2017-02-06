"""
The script parses a page of reviews from Amazon.com and stores the review 
Information in a text file.
"""

from bs4 import BeautifulSoup

fconn=open('reviews.html')
html=fconn.read()#read the entire html into this variable
fconn.close()

tree=BeautifulSoup(html)#prepare the tree

reviewChunks = tree.findAll('div', {'class':'a-section review'}) # find all review Chunks
for RC in reviewChunks:
    starChunk=RC.find('i',{'class':'a-icon-star'})#<i class="a-icon a-icon-star a-star-4 review-rating"><span class="a-icon-alt">4.0 out of 5 stars</span></i>
    stars=starChunk.text

    titleChunk=RC.find('a', {'class':'review-title'})#<a class="a-size-base a-link-normal review-title a-color-base a-text-bold" href="/gp/customer-reviews/RTCU9IHUSOC3K/ref=cm_cr_pr_rvw_ttl?ie=UTF8&amp;ASIN=B00XKRWTUE">Very Good</a>
    title=titleChunk.text

    userChunk=RC.find('a',{'class':'author'})#<a class="a-size-base a-link-normal author" href="/gp/pdp/profile/AZ0OW7VY5G26T/ref=cm_cr_pr_pdp?ie=UTF8">John McCarthy</a>
    user=userChunk.text

    dateChunk=RC.find('span',{'class':'review-date'})#<span class="a-size-base a-color-secondary review-date">on February 2, 2016</span>
    date=dateChunk.text

    textChunk=RC.find('span',{'class':'review-text'})#<span class="a-size-base review-text">Works great.  Quick to connect to GPS. ... </span>
    text=textChunk.text
    text=text.encode('ascii','ignore')# remove non-utf 8 characters
     
    print stars,'\n',title,'\n',user,'\n',date,'\n',text
    print
    
