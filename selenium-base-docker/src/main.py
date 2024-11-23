from seleniumbase import SB
import time
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

learner_id = config['learner_id']
password = config['password']

url = 'https://www.cdc.com.sg/'
with SB(uc=True, headless=True) as sb:
    sb.uc_open(url)
    sb.uc_click('#login > div > div > span')
    print("Clicked user icon")
    sb.type('#userId_4', learner_id)
    print(f"Entered learner id: {learner_id}")
    sb.type('#password_4', password)
    print(f"Entered password: {password}")
    print("Exiting in 5 seconds...")
    time.sleep(5)