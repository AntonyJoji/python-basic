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

    address_keywords=['ACT Chamber','MKK','Rd','palarivattom','Ernakulam','Kerala','P.O','PO','Floor']
    address =[]
    for ln in lines:
        if any(kw.lower() in ln.lower() for kw in address_keywords):
            address.append(ln)
        print("Found addresses:", address)
    

    # if not address:
    #     for i ,ln in enumerate(lines):
    #         if 'contact us' in ln.lower() or 'address' in ln.lower():
    #             snippet = "\n".join(lines[i:i+5])
    #             address.append(snippet)
                
    hours =[ln for ln in lines if re.search(r'\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b',ln,re.IGNORECASE) ]  
    print("Found hours:", hours)

    response_time =[ln for ln in lines if 'response' in ln.lower()or 'reply' in ln.lower()]
    print("Found response time info:", response_time)  
    

    return {
        "emails":emails,
        "phones":phones,
        "address":address,
        "hours":hours,
        "response_time":response_time
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
        
        f.write("\n----------------------------\n")
        f.write("\nAddresses:\n")
        for a in data["address"]:
           f.write(f"--{a}\n")

        f.write("\n----------------------------\n")
        f.write("\nHours:\n")
        for h in data["hours"]:
           f.write(f"--{h}\n")

        f.write("\n----------------------------\n")
        f.write("\nResponse Time Info:\n")  
        for r in data["response_time"]:
           f.write(f"--{r}\n")
   


if __name__ == "__main__":
    html = fetch_page(URL)
    soup = BeautifulSoup(html, 'html.parser')
    page_text = soup.get_text("\n",strip=True)
    data =extract_structured(page_text)
    write_output(data)
