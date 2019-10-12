# Django Ember Heroku Demo
Basic heroku app demo'ing abilty for a django app to host a bundled ember app. 

## Deployment 

-> `git push heroku master`

enable labs -> `heroku labs:enable runtime-dyno-metadata -a frozen-inlet-30069`

## Local Development
TODO

## Django Setup
https://devcenter.heroku.com/articles/getting-started-with-python#define-config-vars

### Notes on building 

`pipenv install gunicorn`
`pipenv lock -r > requirements.txt`

### Some funkiness on inital deploy; https://stackoverflow.com/questions/36665889/collectstatic-error-while-deploying-django-app-to-heroku
`heroku config:set DISABLE_COLLECTSTATIC=1`


# Ember Setup


