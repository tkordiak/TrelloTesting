 # Trello API and UI tests

Project contains both api and selenium tests. At the beginning I wanted to seperate integration and acceptance testing but eventually 
put them within one project.

- Api Test Cases: tests -> api -> test_trello.py
- Selenium Test Case: tests -> acceptance -> TrelloUiTests.py

"Resources" folder stores chromedriver for Chrome version 87
Regarding API testing, each test case is a separete, individual unit.
For Selenium I've created a board in trello ("Selenium Test") with two cards.
External packages utilized are: requests and selenium. 
