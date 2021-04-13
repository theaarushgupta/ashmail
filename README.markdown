<div align = "center">
    <h1>Dispatch</h1>
    Mass-emailing made simple and affordable
</div>

## Overview

Services such as Mailchimp are have advertising in sent emails and aren't afforable for small businesses to use on a regular basis. To combat this, I created Dispatch. Dispatch has the same qualities Mailchimp does -- it can:
- Send neat html-based messages
- Have dynamic content within those emails to personalize them
- Support large emailing lists
- Do everything with a simple installation and usage

## Usage

### Files needed
- `config.yml` - the configuration file
- `content.html` - the html content of the email with variables inside squiggled brackets
- `recievers.csv` - a file with names and emails
Note: all of these files with some example data can be found in the `_sampleData/` directory

### Data required in files

#### `config.yml`
- `content`: name of the html file with the content to send in the email
- `recivers`: name of the csv file with data with names and emails
- `from`: the address to send the email from
- `password`: the password of the aforementioned email
- `subject`: the subject of the email

#### `content.html`
An html file with content. Variables can be inside double squiggled brackets:
```html
<h1 style = "color: red;">Hello {{ name }}</h1>
<h3 style = "color: blue;">Nice email! {{ email }} looks so professional</h3>
```

#### `recievers.csv`
A csv file with names and their corrosponding emails
```csv
name,email
Mr. Example,example@example.com
```

### Running Dispatch

#### If this is the first time running dispatch on your computer
- Clone the repository with `git` or download the source code
- Go into the directory with the code
- Run `python3 setup.py install`
- Installation Complete!

#### Continued from last steps or already installed dispatch
- `dispatch <configuration>` where `<configuration>` is the filename of the configuration yaml file
Note: make sure all the files described above are in the same directory before running the script.

## Important Notes
- Dispatch currently only works with Gmail based accounts
- Turn on Less Secure Apps on your email before using the app, or if you have two factor authentication on, create an App Password and use that in the configuration file.

## Copyright &copy; 2021 Aarush Gupta
This code is copyrighted but licensed to the public under the GNU AGPLv3 license and any later versions.