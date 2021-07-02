import os
from bs4 import BeautifulSoup
dir_name = 'V:/Final_Project/DBA'



def get_values(full_path):
    soup = BeautifulSoup(open(full_path), 'html.parser')
    name = soup.find(class_ = "pr5 f14").text
    about = soup.find(class_ = "f13 lh20 pt10 w500").text
    # ls = soup.find(class_ ="tup_lt w338").text
    i = 0
    dict_details = {}
    for tag in soup.find_all("li"):
        if(":" in tag.text):
                details = tag.text.split(":")
                dict_details[details[0].strip()] = details[1].strip()
        elif("as" in tag.text):
            arr = tag.text.split("*")
            company_name = arr[0].split(" as ")[0].strip()
            description_and_date = arr[0].split(" as ")[1]
            sp = description_and_date.split(" ")
            one_str = ''
            two_str = ''
            flag = 0
            for j in range(1,len(sp)):
                if(sp[j].isdigit() and flag == 0):
                    flag = 1
                    first = sp[j-1][:-3]
                    second = sp[j-1][len(sp[j-1])-3:]
                    one_str = one_str +' '+ first
                    two_str = two_str + ' ' + second
                elif(sp[j].isdigit() == False and flag == 0):
                    one_str = one_str + ' ' + sp[j-1]
                else:
                    two_str = two_str + ' ' + sp[j-1]
            two_str = two_str + ' ' + sp[len(sp)-1]
            one_str= one_str.strip()
            two_str= two_str.strip()
            print(company_name)
            print(one_str)
            print(two_str)

            
        i += 1
    # for ele in dict_details:
    #     print(ele,":",dict_details[ele])
    # print(len(dict_details))
    print("*****************************")
    print("*****************************")

"""
    Get list of all the html files present in the directory and pass it to the 
get_values function
"""
def get_list():
    list_of_html = os.listdir(dir_name)
    count = 0
    for html_page in list_of_html:
        full_path = os.path.join(dir_name,html_page)
        get_values(full_path)
        count += 1
        if(count == 5):
            break

get_list()
