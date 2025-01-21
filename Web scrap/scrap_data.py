import requests
from bs4 import BeautifulSoup



url_data = ["https://sdgs.un.org/goals/goal1#targets_and_indicators", 
            "https://sdgs.un.org/goals/goal2#targets_and_indicators",
            "https://sdgs.un.org/goals/goal3#targets_and_indicators",
            "https://sdgs.un.org/goals/goal4#targets_and_indicators",
            "https://sdgs.un.org/goals/goal5#targets_and_indicators",
            "https://sdgs.un.org/goals/goal6#targets_and_indicators",
            "https://sdgs.un.org/goals/goal7#targets_and_indicators",
            "https://sdgs.un.org/goals/goal8#targets_and_indicators",
            "https://sdgs.un.org/goals/goal9#targets_and_indicators",
            "https://sdgs.un.org/goals/goal10#targets_and_indicators",
            "https://sdgs.un.org/goals/goal11#targets_and_indicators",
            "https://sdgs.un.org/goals/goal12#targets_and_indicators",
            "https://sdgs.un.org/goals/goal13#targets_and_indicators",
            "https://sdgs.un.org/goals/goal14#targets_and_indicators",
            "https://sdgs.un.org/goals/goal15#targets_and_indicators",
            "https://sdgs.un.org/goals/goal16#targets_and_indicators",
            "https://sdgs.un.org/goals/goal17#targets_and_indicators"]



for u in range(len(url_data)): #loop through list of URLs
    print("\nExtracting Page", u+1,  ">>>>>>>>>>>>>>\n")
    r = requests.get(url_data[u])
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='goal-text') #finding text in class goal-text
    content = soup.find_all('p')
    print(content)
    


input("Press over...")