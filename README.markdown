# AshMail
The Free and Simple Mass Emailing System 

On version: `v2.1.0`

## Usage

### Files needed
- `config.yml` - the configuration file
- `content.html` - the html content of the email with variables inside squiggled brackets
- `recievers.csv` - a file with names and emails

Note: all of these files with some example data can be found in the `_tests_/` directory

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

### Running AshMail

#### If this is the first time running AshMail on your computer
1. Clone the repository with `git` or download the source code
2. Go into the directory with the code
3. Run `python3 setup.py install`
4. Installation Complete!

#### Continued from last steps or already installed AshMail
1. `ashmail <configuration>` where `<configuration>` is the filename of the configuration yaml file
    - Note: make sure all the files described above are in the same directory before running the script.

## Important Notes
- AshMail currently only works with Gmail based accounts
- Turn on Less Secure Apps on your email before using the app, or if you have two factor authentication on, create an App Password and use that in the configuration file.

## Copyright &copy; 2021 Aarush Gupta
This code is copyrighted but licensed to the public under the GNU AGPLv3 license and any later versions.
