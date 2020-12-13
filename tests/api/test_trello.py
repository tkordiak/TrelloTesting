import requests
from unittest import TestCase

KEY = '413b3a42803a9792c0cd531c543955fd'
TOKEN = '4885a79ad3fdddf77e5f8b426a07f548065502494e8a2676697864495bda0f9b'


class TrelloApiTests(TestCase):

    def test_create_board_status_is_200(self):
        # Arrange
        url = "https://api.trello.com/1/boards/"
        query = {
            'key': KEY,
            'token': TOKEN,
            'name': 'NewTomaszBoard'
        }

        # Act
        response = requests.request(
            "POST",
            url,
            params=query
        )

        # Assert
        resp_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp_json['name'], 'NewTomaszBoard')

    def test_create_3_cards_cards_created(self):
        # Arrange
        # Create Board first
        board_json = TrelloApiTests._create_board(name='BoardWith3Cards')
        board_id = board_json['id']

        # Create a list on the board
        list_json = TrelloApiTests._create_list('TomaszNewList', board_id)
        list_id = list_json['id']

        # Act
        # Create 3 cards on a list
        response_first_card, first_card_json = TrelloApiTests._create_card(list_id, name='FirstCard')
        response_second_card, second_card_json = TrelloApiTests._create_card(list_id, name='SecondCard')
        response_third_card, third_card_json = TrelloApiTests._create_card(list_id, name='ThirdCard')

        # Assert
        self.assertEqual(response_first_card.status_code, 200)
        self.assertEqual(response_second_card.status_code, 200)
        self.assertEqual(response_third_card.status_code, 200)

        self.assertEqual(first_card_json['idList'], list_id)
        self.assertEqual(second_card_json['idList'], list_id)
        self.assertEqual(third_card_json['idList'], list_id)

        self.assertEqual(first_card_json['idBoard'], board_id)
        self.assertEqual(second_card_json['idBoard'], board_id)
        self.assertEqual(third_card_json['idBoard'], board_id)

    def test_edit_card_card_changed(self):
        # Arrange
        # Create Board first
        board_json = TrelloApiTests._create_board(name='BoardEditCard')
        board_id = board_json['id']

        # Create a list on the board
        list_json = TrelloApiTests._create_list('ListEditCard', board_id)
        list_id = list_json['id']

        # Create 1 card on a list
        response_first_card, first_card_json = TrelloApiTests._create_card(list_id, name='FirstCard')

        # Act
        url = f"https://api.trello.com/1/cards/{first_card_json['id']}"

        query = {
            'key': KEY,
            'token': TOKEN,
            'name': 'FirstCardEdited',
            'desc': 'This card has been edited'
        }

        response = requests.request(
            "PUT",
            url,
            params=query
        )

        actual_card_name = response.json()['name']
        actual_card_desc = response.json()['desc']

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(actual_card_desc, query['desc'])
        self.assertEqual(actual_card_name, query['name'])

    def test_delete_card_card_deleted(self):
        # Arrange
        # Create Board first
        board_json = TrelloApiTests._create_board(name='BoardDeleteCard')
        board_id = board_json['id']

        # Create a list on the board
        list_json = TrelloApiTests._create_list('ListDeleteCard', board_id)
        list_id = list_json['id']

        # Create 1 card on a list
        response_first_card, first_card_json = TrelloApiTests._create_card(list_id, name='FirstCard')

        # Act
        url = f"https://api.trello.com/1/cards/{first_card_json['id']}"

        query = {
            'key': KEY,
            'token': TOKEN
        }

        response = requests.request(
            "DELETE",
            url,
            params=query
        )

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(TrelloApiTests._get_card(first_card_json['id']).status_code, 404 )

    def test_add_comment_comment_added(self):
        # Arrange
        # Create Board first
        board_json = TrelloApiTests._create_board(name='BoardCommentCard')
        board_id = board_json['id']

        # Create a list on the board
        list_json = TrelloApiTests._create_list('ListCommentCard', board_id)
        list_id = list_json['id']

        # Create 1 card on a list
        response_first_card, first_card_json = TrelloApiTests._create_card(list_id, name='FirstCard')

        # Act
        url = f"https://api.trello.com/1/cards/{first_card_json['id']}/actions/comments"

        query = {
            'key': KEY,
            'token': TOKEN,
            'text': 'This is a comment'
        }

        response = requests.request(
            "POST",
            url,
            params=query
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['text'], query['text'])

    @classmethod
    def _create_card(cls, list_id, name='DefaultCardName'):
        url = "https://api.trello.com/1/cards"
        query_card = {
            'key': KEY,
            'token': TOKEN,
            'name': name,
            'idList': list_id
        }
        response_card = requests.request(
            "POST",
            url,
            params=query_card
        )
        return response_card, response_card.json()

    @classmethod
    def _create_list(cls, name, board_id):
        url_list = "https://api.trello.com/1/lists"
        name_list = "TomaszNewList"
        query_list = {
            'key': KEY,
            'token': TOKEN,
            'name': name,
            'idBoard': board_id
        }
        response_list = requests.request(
            "POST",
            url_list,
            params=query_list
        )
        list_json = response_list.json()
        return list_json

    @classmethod
    def _create_board(cls, name):
        url_board = "https://api.trello.com/1/boards/"
        query_board = {
            'key': KEY,
            'token': TOKEN,
            'name': name,
        }
        response_board = requests.request(
            "POST",
            url_board,
            params=query_board
        )
        board_json = response_board.json()
        return board_json

    @classmethod
    def _get_card(cls, card_id):
        url = f"https://api.trello.com/1/cards/{card_id}"

        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': KEY,
            'token': TOKEN
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        return response
