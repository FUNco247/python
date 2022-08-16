import requests

print("welcome to is it down? py program! (Hi nico fam ^_^)")
run = True
while run:
  urlInput = input("please write url or urls you want to check !  seperated by comma : ")
  urlsArr = urlInput.replace(" ","").lower().split(",")
  for url in urlsArr:
    try:
      if not url.startswith("http://"):
        url = "http://" + url
      status = requests.get(url).status_code
      if status == 200:
        print(f"{url} is up!")
      else:
        print(f"{url} is down")
    except:
      print(f"{url} is not valid url")
  while True:    
    retry = input("Do you want to try again? (y/n) : ")
    if retry == "y":
      break
    if retry == "n":
      print("bye bye~ see you again")
      run = False
      break
    else:
      print("please enter 'y' for 'Yes' and 'n' for 'No'")