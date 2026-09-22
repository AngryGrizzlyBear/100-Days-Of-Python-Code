"""Hangman — The Gibbet of the Gem Warden.

The game itself is a browser game (see index.html in this folder): three
adventurers are trapped in a dungeon time loop and must each solve a
birthstone-riddle hangman to escape. GitHub Pages can only host static
files, so the gameplay runs in JavaScript in the browser.

This script is the Python launcher: it serves the folder on a local web
server and opens the game in your default browser.

Run it with:
    python hangman_project.py
"""

import http.server
import socketserver
import webbrowser
from pathlib import Path

PORT = 8000
GAME_DIR = Path(__file__).parent


class GameRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Serves files from the game folder regardless of where the script is run from."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(GAME_DIR), **kwargs)


def main():
    # allow_reuse_address lets us restart the server immediately after a
    # previous run without waiting for the OS to release the port.
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), GameRequestHandler) as server:
        url = f"http://localhost:{PORT}/"
        print("The Gem Warden awaits…")
        print(f"Serving the dungeon at {url}  (Ctrl+C to close the loop)")
        webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nThe torches gutter out. Goodbye.")


if __name__ == "__main__":
    main()
