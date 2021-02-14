# Welcome to MEMEWORLD

This a Meme Streaming app made using Flask backend, SQLalchemy as Database and HTML+CSS+JS in frontend.

The backend exposes 3 apis http://localhost:8081/memes which on GET request return top 100 memes as a json list.

We can make POST request to above URL, then the meme will be saved in Database and the meme_id will be returned.

http://localhost:8081/memes/meme_id which on GET request returns the info about particular meme_id.

To test this app first run install.sh, server_run.sh and sleep.sh for configuartion.


