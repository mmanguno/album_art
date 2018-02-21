#!/usr/bin/env python3
"""server supplying data to the album_art widget"""

# Copyright (C) 2018 Mitchell Manguno

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>


import functools
from typing import Dict

from flask import Flask, jsonify
from spotipy import Spotify, util
import yaml


def _get_config(file_handle: str) -> Dict:
    """Read and return the config file."""
    with open(file_handle) as file_:
        configuration = yaml.load(file_)
    return configuration


def _get_spotify(username, client_id, client_secret, redirect_uri) -> Spotify:
    """Initialize and return a Spotify client."""
    scope = "user-read-currently-playing"  # only need to read current track
    token = util.prompt_for_user_token(username, scope,
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri)

    return Spotify(auth=token)


# TODO: make this asycnchronous, and call it first in the update so we
# get a full second to make the Spotify call
def get_spotify_info(spotify_client) -> Dict:
    """Query Spotify API for currently playing track."""

    track = spotify_client.current_user_playing_track()
    album = track["item"]["album"]
    name = track["item"]["name"]
    art = album["images"]
    is_playing = track["is_playing"]

    largest = max(art, key=lambda img: img["height"] * img["width"])

    payload = {
        "link": largest["url"],
        "album": album["name"],
        "playing": is_playing,
        "name": name,
        "height": largest["height"],
        "width": largest["width"]
    }

    return jsonify(payload)


def main():
    """Run the server."""
    app = Flask(__name__)
    config = _get_config("config.yaml")
    spotify = _get_spotify(config["username"], config["client_id"],
                           config["client_secret"], config["redirect_uri"])

    # supply the main endpoint with the spotify client
    endpoint = functools.partial(get_spotify_info, spotify)
    app.add_url_rule('/', 'get_spotify_info', endpoint)

    app.run()


if __name__ == "__main__":
    main()
