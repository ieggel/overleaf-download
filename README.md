# Overleaf-Download

This is just a tiny and partially incomplete project that allows downloading a zipped file containing all Overleaf projects.

## Execution

Bash and Python are used. The Bash script calls the Python script, which logins to Overleaf, grabs the cookie as well as the projects IDs and passes them back to the Bash script which in turn downloads the projects. Google Chrome needs to be installed on your system.

In order to run the `download`, do the following
```bash
# Clone this project
$ git clone <this_project>
# cd into project
$ cd overleaf-info
# install python deps
$ pip install -r requirements.txt
# Execute bash script and follow instructions
$ ./download
```
By default, the downloaded zip file will be saved in the home directory with the name overleaf-backup-YYYY-MM-DD.zip. You can adapt it in the `download` script (read comments). 

### Limitations

#### Browser
- Currently only Google Chrome is supported.
- Browser cannot be run in headless mode because Overleaf often asks for a Google ReCaptcha.

#### Credentials
- Currently only native overleaf credentials are supported.
- Credentials are asked by the bash script
  - Possibly it would be better to hard code the credentials (comments in `download` script)

#### Paging
Currently the script only works for a small number of Overleaf projects. The python script would need to implement clicking the `Load more` button in order to get a complete list of all project IDs.

## Depencies
- Bash
- Python
  - Selenium
- Google Chrome
