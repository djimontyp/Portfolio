import React from 'react';

import axios from 'axios';

export default class BooksList extends React.Component {
  state = {
    books: []
  }

  componentDidMount() {
    axios.get(`http://localhost:8080/books`)
      .then(res => {
        const books = res.data;
        this.setState({books});
      })
  }

  render() {
    return (
      <div className="Books-list">
        <ul>
          {this.state.books.map(book =>
            <li key={book.id}>{book.title} {book.pages}</li>
          )}
        </ul>
      </div>
    )
  }
}