# Set up develop environment (Mac OSX)

## System Dependences

    brew install pyenv pyenv-virtualenv \ # Python interprator
                 npm
    
    pip install aws-sam-local

## Python interprator (If necessary)
    pyenv install 3.6.1
    pyenv shell 3.6.1

## Python Dependences

#### dependency
	pip install -r ./src/requirements.txt -t ./src
	
#### dev  dependency
	source local-env
    pipenv install
	
#### dev dependency activate
    pipenv shell

### Run lambda
    LogLevel=INFO sam local invoke "EchoLambda" -e events/sample.json
	
## Build
    make build
