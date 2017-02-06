"""
This script download the pages of reviews of a given amazon product.
Each page is stored in a separate html file.
"""

#import the two libraries we will be using in this script
import urllib2,os,sys,time

#make a new browser, this will download pages from the web for us. This is done by calling the 
#build_opener() method from the urllib2 library
browser=urllib2.build_opener()

#desguise the browser, so that websites think it is an actual browser running on a computer
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

#number of pages you want to retrieve
pagesToGet=2

#make a new folder to store the pages, but only if it doesn't already exist
if not os.path.exists('reviewPages'):os.mkdir('reviewPages')


"""
Note: The range() function
    the range(a,b) function returns the list of numbers from a all the way to (but excluding) b. 
    For example, range (1,4) will return  [1, 2, 3]
"""

#for every number in the range from 1 to pageNum+1  
for page in range(1,pagesToGet+1):
    
    print 'processing page :', page

    #prepare the link to the next page    
    url='http://www.amazon.com/Garmin-010-01472-10-Forerunner-225/product-reviews/B00XKRWTUE/ref=cm_cr_pr_btm_link_'+str(page)+'?ie=UTF8&showViewpoints=1&sortBy=recent&pageNumber='+str(page)

    #an exception might be thrown, so the code should be in a try-except block
    try:
        #use the browser to get the url.
        response=browser.open(url)# this might throw an exception if something goes wrong.
    
    except Exception as e: # this describes what to do if an exception is thrown
        error_type, error_obj, error_info = sys.exc_info()# get the exception infomration
        print 'ERROR FOR LINK:',url #print the link that cause the problem
        print error_type, 'Line:', error_info.tb_lineno #print error info and line that threw the exception
        continue#ignore this page.
    
    #read the response in html format. This is essentially a long piece of text
    myHTML=response.read()

    #write the page to a new html file
    fwriter=open('reviewPages/'+str(page)+'.html','w')
    fwriter.write(myHTML)
    fwriter.close()
    
    #wait for 2 seconds
    time.sleep(2)
