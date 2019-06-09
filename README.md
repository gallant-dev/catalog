# My Catagories Project

A python web application that allows users to create, read, update and delete
flower arrangements and their associated flowers. API endpoints were also used
to allow JSON requests to be made to receive user data, arrangement and flower
information. To do this it uses a PostgreSQL database, flask, and SQL
Alchemy. Google's OAuth2.0 was implemented for user authentication, preventing
unregistered users from modifying content.

## Requirements

* Bootstrap 4.3.1
* JQuery 3.3.1
* popper.js 1.14.7
* Python 2.7.12
* Flask 0.12.2
* VirtualBox 5.1.32
* Vagrant 2.0.2
* FSND Virtual Machine configuration files. [Repository](https://github.com/udacity/fullstack-nanodegree-vm "Download VM configuration files")
* Valid Google OAuth2.0 client id and secret saved as `client_secret.json`

## How to run the app

Open the command prompt in the downloaded FSND Virtual Machine folder. In it
type: `vagrant up` press enter, and then enter `vagrant ssh` and press enter.

Ensure that the `catalog` folder is moved into the vagrant folder
in the FSND Virtual Machine directory.

To run the program you will need to make sure you meet the listed requirements,
including saving your Valid Google OAuth2.0 application id and secrets as
`client_secret.json` in the `catalog` folder.

Ensure that you are in the `catalog` directory, and in the command
prompt enter `python application.py`. This will initialize the application.

To view the application you must open your browser and enter `localhost:8000`
in the address bar.

Authored by: Adam Gallant, 2018-05-17
