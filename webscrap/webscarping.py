import requests
from bs4 import BeautifulSoup
import re


URL="https://expertzlab.com/contact"


def fetch_page(url):
    r=requests.get(url,timeout=15)
    r.raise_for_status()
    return r.text

def extract_structured(text):
    lines =[ln.strip() for ln in text.splitlines() if ln.strip()]
    # print(lines)
    joined ="\n".join(lines)
    # print(joined)

    emails=sorted(set(re.findall(r'[\w\.-]+@[\w\.-]+\.\w+',joined)))
    print("Found emails:", emails)
    phones=sorted(set(re.findall(r'(?:\+?\d{1,3}[\s\-]?)?\(?\d+\)?[\d\s\-]{10,}',joined)))
    for i in range(len(phones)):
        phones[i]=re.sub(r'[\s\-]+','',phones[i])   
    print("Found phones:", phones)

    return {
        "emails":emails,
        "phones":phones
    }


def write_output(data,filename="data.txt"):
    with open(filename,'w',encoding='utf-8') as f:
        f.write("-------Extracted Data-------\n\n")
        f.write("Emails:\n")
        for e in data["emails"]:
           f.write(f"--{e}\n")


        f.write("\n----------------------------\n")
        f.write("\nPhones:\n")
        for p in data["phones"]:
           f.write(f"--{p}\n")  

   


if __name__ == "__main__":
    html = fetch_page(URL)
    soup = BeautifulSoup(html, 'html.parser')
    page_text = soup.get_text("\n",strip=True)
    data =extract_structured(page_text)
    write_output(data)
