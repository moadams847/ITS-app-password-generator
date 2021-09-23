# ITS Password Generator API

This is a web API for generating random characters.

## Motivation

I started this project to automate an aspect of the work I do as an ITS support officer at the University Of Ghana Computing System.

## URL

[Password Generator API](https://fierce-anchorage-76525.herokuapp.com)

## Installation

1. Clone Repo
2. cd to the directory where requirements.txt is located
3. activate your virtual environment.
4. run: pip install -r requirements.txt in your shell

```bash
pip install -r requirements.txt
```

## Tech/framework used

1. Python (Flask)
2. Heroku

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# How To Use The API

## The API has two paths and a single query parameter.

## 1. API EndPoint

GET
https://fierce-anchorage-76525.herokuapp.com/passwordapi/v2/

## 2. API Paths

- special-characters:

* GET
  https://fierce-anchorage-76525.herokuapp.com/passwordapi/v2/special-characters

- no-special-characters:

* GET
  https://fierce-anchorage-76525.herokuapp.com/passwordapi/v2/no-special-characters

## 3. Query Parameter

- key: passwordLength
- value: number or integer

## Examples

- An example of a 10-character password containing special characters:

https://fierce-anchorage-76525.herokuapp.com/passwordapi/v2/special-characters?passwordLength=10

- Another example of a 10-character password without special characters:

https://fierce-anchorage-76525.herokuapp.com/passwordapi/v2/no-special-characters?passwordLength=10

## License

[MIT](https://choosealicense.com/licenses/mit/)
