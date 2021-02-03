import uuid
from flask import request,jsonify

class BookInfo():
    def __init__(self):
        # 书本信息
        self.BOOKS = [
            {'id': uuid.uuid4().hex,'title': 'On the Road',
             'author': 'Jack Kerouac','read': True},
            {'id': uuid.uuid4().hex,'title': 'Harry Potter and the Philosopher\'s Stone',
             'author': 'J. K. Rowling','read': False},
            {'id': uuid.uuid4().hex,'title': 'Green Eggs and Ham',
             'author': 'Dr. Seuss','read': True}
        ]

    def remove_book(self,book_id):
        for book in self.BOOKS:
            if book['id'] == book_id:
                self.BOOK.remove(book)
                return True
        return False

    def all_books(self):
        response_object = {'status': 'success'}
        print(request.data)
        if request.method == 'POST':

            post_data = request.get_json()
            self.BOOKS.append(
                {'id': uuid.uuid4().hex,'title': post_data.get('title'),
                'author': post_data.get('author'),'read': post_data.get('read')})


            response_object['message'] = 'Book added!'
        else:
            response_object['books'] = self.BOOKS

        return jsonify(response_object)

    def single_book(self,book_id):
        response_object = {'status': 'success'}
        if request.method == 'PUT':
            post_data = request.get_json()
            self.remove_book(book_id)
            self.BOOKS.append({'id': uuid.uuid4().hex,'title': post_data.get('title'),
                               'author': post_data.get('author'),'read': post_data.get('read')})
            response_object['message'] = 'Book updated!'
        if request.method == 'DELETE':
            self.remove_book(book_id)
            response_object['message'] = 'Book removed!'
        return jsonify(response_object)