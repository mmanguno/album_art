# album_art
an uebersicht album-art widget that displays Spotify's currently-playing
album's artuses a client-server architecture

# Example
![good album][art.png]


## What it is
An uebersicht widget for displaying album art from Spotify. The
front-end makes a curl call to a localserver. The localserver, backed
by Flask, calls Spotify, pulls out what it wants, and gives it to the widget.

## How to run it
1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Setup Spotify credentials, so we can poll spotify. Fill out the
   config.yaml.example, and rename it to "config.yaml". I followed the
   steps in the [spotipy docs][0]. This will require you to make an app
   as a Spotify dev. If you don't want to do this, just comment out the
   spotify stuff in the server code.

3. Run the server, preferably keeping it in a background process:
   ```bash
   python3 server.py&
   ```
   The first time it runs, it will open up your browser (or whatever
   `$BROWSER` is configured in your shell), and ask you to authenticate. This
   won't be often.

4. Move/symlink the widget into the widgets folder.

That's it.

## What's next
Make it so the damn thing doesn't de-authorize after a time. Maybe no
server if authorizing can be done once and curls made directly to
Spotify.

[0]: http://spotipy.readthedocs.io/en/latest/#authorized-requests
