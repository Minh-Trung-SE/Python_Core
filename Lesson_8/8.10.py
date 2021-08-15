domain_list = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]

for i in domain_list:
    print(f"Suffixes this domain: {i} is {i.split('.')[-1]}")
