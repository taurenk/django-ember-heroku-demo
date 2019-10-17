# Django Ember Heroku Demo
The basic POC for this repo is a Django app that serves an Ember single-page-app via a route url all running on heroku. 

I have also thrown in a review app pipeline for fun. 

## Heroku Deployment 
If you run into any trouble, check out https://devcenter.heroku.com/articles/git#for-a-new-heroku-app. But basic pipeline:

1) `heroku create` -> Create an app in Heroku
    1a) if you get a fun name such as "frozen-lava-inuit", you can rename it via `heroku apps:rename your-new-name --app old-name`
    1b) You can enable some [helpful config info](https://devcenter.heroku.com/articles/dyno-metadata) with `heroku labs:enable runtime-dyno-metadata -a your-app-name`
2) `git push heroku master` -> pushes your latest master branch code to heroku for a deployment

Thats it.


## Local Development

### Up and Running
The easiest setup is as follows:
1. `pipenv install` -> Setup pipenv + install dependencies
2. `npm install` -> Install Ember app dependencies
3. `pipenv shell` ->  Activate pipenv environemnt
4. `foreman start -f Procfile.dev` -> Starts both Django + Ember in live reload mode

You can of course run Django and Ember indepently, by running:
`pipenv run ./manage.py runserver` and `npm run` in different tabs


## Architecture + Notes

### Django Config 
- Whitenoise
- Database config 

### TODO; Ember Config 
- routing with a prefix
- Build path