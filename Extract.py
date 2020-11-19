
from urllib.request import  urlopen as uReq

from bs4 import BeautifulSoup as soup


myurl="https://www.ncbi.nlm.nih.gov/gene/"



id="2000" 

#add id to the url
#myurl="https://www.ncbi.nlm.nih.gov/gene/" + "2000"
#finally it will become myurl= "https://www.ncbi.nlm.nih.gov/gene/2000"

myurl=myurl+id


print(id)

uClient=uReq(myurl)

page_html=uClient.read()


uClient.close()


page_soup=soup(page_html,"html.parser")

summary_soup=page_soup.find("div",attrs={"id":"summaryDiv"})

l=summary_soup.find_all("dt")

sym=""
name=""
gene=""
org=""


for i in l:

  tex=i.next_element.next_element.next_element
  if(tex.next_element!="\n"):
    val=tex.next_element
  else:
    val = tex.a.text
  #check if required data is present in the row
  if("Symbol" in i.text):
    sym=val
  elif("Full Name" in i.text):
    name=val
  elif("Gene" in i.text):
    gene=val
  elif("Organism" in i.text):
    org=val
print(sym)
print(name)
print(gene)
print(org)
print("****")
