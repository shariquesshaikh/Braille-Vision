import json
from selenium.webdriver import Chrome

# with open('path to json file', encoding='utf-8') as s:
#     data = json.loads(s.read())

# for site in data['sites']:
#     driver = Chrome('path to chrome driver')
#     driver.get(data['sites'][site])
#     driver.get_screenshot_as_file(site + '.png')
# driver.close()

driver = Chrome('path to chrome driver')