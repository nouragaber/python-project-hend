import requests
import bs4

job_titles = []
company_names =[]
company_locationes =[]
information =[]
posted =[]
page_num=0
while True:
    # try:
               #requests to fetch the url
           res= requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=web%20developers&start={page_num}")
           #page content
           con=res.content
           #print(con)
           #create soup object to parse content
           soup=  bs4.BeautifulSoup(con, "lxml")


           page_limit = int(soup.find("strong").text)
           if(page_num>page_limit//15):
               print("pages ended")
               break
           #find elements
           job_title = soup.find_all("h2",{"class":"css-m604qf"})
           company_name= soup.find_all("a",{"class":"css-17s97q8"})
           company_location= soup.find_all("span",{"class":"css-5wys0k"})
           job_information = soup.find_all("div", {"class":"css-y4udm8"})
           posted_new= soup.find_all("div",{"class":"css-4c4ojb"})
           posted_old= soup.find_all("div",{"class":"css-do6t5g"})
           posteed =[*posted_new , *posted_old]
               #step loop over returned lists
           for i in range(len(job_title)):
               job_titles.append(job_title[i].text)
               company_names.append(company_name[i].text)
               company_locationes.append(company_location[i].text)
               information.append(job_information[i].text)
               posted.append(posteed[i].text)

           page_num +=1
"""" print("page switched")
except:
           print("error")
           break
"""
print (job_titles)


print (company_names)


print(company_locationes)


print(information)


print(posted)