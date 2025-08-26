# Python Virtual Environment (VENV)

I created a Python virtual environment for this project's dependencies.  
It is installed **outside the synchronized project folder**, in the Docker container’s home directory, to keep it separate from the project files.

## Activation
```bash
source ~/env/bin/activate
```

## Deactivation
```bash
deactivate
```

### Cheat Sheet
https://python-guide.readthedocs.io/en/latest/dev/virtualenvs/
--------

# Install Required Python Packages

### Creating requirements file
It's best practice to list all of the required Python Packages in a file called `requirements.txt`.
We list all the required packages as well as the version. 

```txt
django==2.2
djangorestframework==3.9.2
```

These packages are not updated for 2025, but I kept them for the sake of following the videos.
To update versions I can go to https://pypi.org.

### Installing requirements in Python virtual environment

1. Make sure we're on the project's folder in the dev server. 

2. Make sure the venv is activated. (`source ~/env/bin/activate`) 
3. Install requirements from requirements file: 
```bash
pip install -r requirements.txt 
```
-----
