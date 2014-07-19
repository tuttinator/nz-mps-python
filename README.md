nz_mps
======

Simple Python JSON API using Flask for displaying the current list of NZ MPs in a machine readable format.

This project includes a scraper to run at periodic intervals (ideally
using cron), and the simple web app.

## Project Setup

Install dependencies:

``
pip install -r requirements.txt
``

### Setup up the database:

From the python interpreter:

``
from database import init_db
init_db()
``

### Scrape the data

``
python scraper.py
``

## Running the Flask app

``
python nz_mps.py
``

## Testing

WIP

## Deploying

WIP

## Contributing

If you'd like to help improve this project, clone the project with Git
by running:

``
$ git clone git@github.com:tuttinator/nz_mps.git
``

Work your magic and then submit a pull request.

## Contributors

Caleb Tutty

## License

This project is released under the MIT license.
