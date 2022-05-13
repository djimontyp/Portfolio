import React from 'react';

import axios from 'axios';

export default class SongsList extends React.Component {
  state = {
    songs: []
  }

  componentDidMount() {
    axios.get(`http://localhost:8080/tracks`)
      .then(res => {
        const songs = res.data.items;
        this.setState({songs});
      })
  }

  render() {
    return (
      <div className="List">
        <ul>
          {this.state.songs.map(song =>
            <li key={song.toString()}>
              Track-name: {song.track.name}
            </li>
          )}
        </ul>
      </div>
    )
  }
}