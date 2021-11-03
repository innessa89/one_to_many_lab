from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import book_repository
from repositories import author_repository
from models.book import Book

books_blueprint = Blueprint('books', __name__)

@books_blueprint.route('/books')
def books():