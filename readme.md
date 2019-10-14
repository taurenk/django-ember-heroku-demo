# Django Ember Heroku Demo
Basic heroku app demo'ing abilty for a django app to host a bundled ember app. 

## Deployment 
- Basic Push -> `git push heroku master`
- Rename -> `heroku apps:rename newname --app oldname`
- Enable Metadata -> `heroku labs:enable runtime-dyno-metadata -a frozen-inlet-30069`

## Local Development
1. `pipenv install`
2. `npm install` 
3. `pipenv shell`: activate pipenv
4. `foreman start -f Procfile.dev`: start django + ember


### Some funkiness on inital deploy; https://stackoverflow.com/questions/36665889/collectstatic-error-while-deploying-django-app-to-heroku
`heroku config:set DISABLE_COLLECTSTATIC=1`


# Ember Setup
You may notice the package.json in the main directory, the NodeJS buildpack looks in this directory for a package.json but ours is in the `demosite/ember` directory. This will just foward the buildback to our actual js code. The order is:

- The buildpack will first run `npm install`. This will do nothing since there is no dependencies. 
- Next, the `postinstall` hook will be run. This will forward the buildpack to the actual package.json for install.
- Next, `build` will get run. again this will call our actual package.json.
- Done.


