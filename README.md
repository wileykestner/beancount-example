# Beancount / Fava Example

This small repository exists to quickly demonstrate what the [beancount](https://github.com/beancount/beancount) library and [fava](https://github.com/beancount/fava) web application for plain text accounting look like in practice.

Visit [https://plaintextaccounting.org/](https://plaintextaccounting.org/) more information about plain text accounting.

Run through the setup steps below to install the libraries in a virtual environment and create an example.beancount plain text ledger file and start the `fava` web application.

## Setup

1. `git clone https://github.com/wileykestner/beancount-example`
2. `cd beancount-example`
3. `./bin/bc bean-check` (This script will create an `example.beancount` data file if you do not already have one and ensure that it is valid.)
4. `./bin/bc fava` (This will open the beautiful fava web application using your new `example.beancount` file as input.)
5. Visit http://localhost:5000/ in your web browser to see fava in action!
