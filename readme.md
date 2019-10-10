# Django Ember Heroku Demo

## Notes on building 

`pipenv install gunicorn`
`pipenv lock -r > requirements.txt`

### Some funkiness on inital deploy; https://stackoverflow.com/questions/36665889/collectstatic-error-while-deploying-django-app-to-heroku
`heroku config:set DISABLE_COLLECTSTATIC=1`

## Deployment 

