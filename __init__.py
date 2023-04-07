from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup;

options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(
    service=Service("C:\Program Files\chromium_driver\chromedriver.exe"), 
    options=options,
)

class ApStudyQuestion:
    number: int
    
    def __init__(self, number: int) -> None:
        self.number = number

class SpringBreakPacketQuestion:
    number: int

    def __init__(self, number: int) -> None:
        self.number = number

    def to_ap_study(self) -> ApStudyQuestion:
        return ApStudyQuestion(self.number + 91)
    
def get_answer_from_question(q_number: ApStudyQuestion) -> str:
    url = f"https://www.apstudy.net/ap/spanish-language-culture/question-{q_number.number}-answer-and-explanation.html"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, features="html.parser")

    for a in soup.find_all('span', attrs={'id': 'key'}):
        return a.text
    
    raise LookupError

NUM_PACKET_QUESTIONS = 84

result: list[tuple[int, str]] = []
for i in range(1, NUM_PACKET_QUESTIONS + 1):
    question = SpringBreakPacketQuestion(i)
    result.append((i, get_answer_from_question(question.to_ap_study())))

for (q_num, ans) in result:
    print(f"#{q_num}: {ans}")