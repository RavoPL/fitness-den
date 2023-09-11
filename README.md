![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# The Fitness Den
Developed by **Dorian Wolarz**, a Code Institute Student

*The Fitness Den is a Full Stack fitness website. Users can create personal accounts and purchase fitness products.*

[LINK TO HEROKU VERSION](https://fitness-den-01445db6e33a.herokuapp.com/)

![The Fitness Den on a PC](N/A)

## Contents
1. [How to Play](#how-to-play)
2. [Features](#features)
3. [Data Model](#data-model)
4. [Planning](#planning)
5. [Technologies Used](#technologies-used)
6. [Testing and Validation](#testing-and-validation)
6. [Known Bugs](#known-bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)

## Deployment

### GitHub

This project was deployed using *Code Institute's CI Full Template* on GitHub.

You can *deploy the repository* on GitHub by following these steps:

1. In your GitHub repository navigate to the *Settings* tab
2. In the menu on the left hand side select *Pages*
3. For the source of your repo select *branch: main*
4. After the webpage refreshes, you will see a ribbon on the top saying: *"Your site is published at https://ravopl.github.io/fitness-den/"*

You can *fork the repository* by following these steps:

1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner

You can *clone the repository* by following these steps:

1. Go to the GitHub repository
2. Locate the Code button above the list of files and click on it
3. Select if you prefer to clone using HTTPS, SSH or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open GitBash
5. Change the current directory to the one you previously cloned
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press 'Enter' to create your local clone

### Django

This project uses *Django* with *Code Institute's CI Full Template* and requires a set of commands to work properly.

1. In your GitPod workspace type: `pip3 install django`
2. To make sure everything is working as intended run the following command: `python3 manage.py runserver`
3. Run the initial migration with the following command: `python3 manage.py migrate`
4. In order to access the admin panel you have to create a superuser by using the following command: `python3 manage.py createsuperuser` after which you fill out the necessary details.
5. Once everything is set up properly you can run the initial commit and push to GitHub.

### Heroku

This project was deployed on Heroku.

After the repository is forked, you can deploy it by following these steps:

1. Create an account on Heroku or log into your existing one
2. Go to the *Dashboard*
3. Create a new app, add its name and your geographical region
4. Click on *Create App*
5. Go to your *Settings* tab
6. Under *Config Vars* make sure you have set the following:
    * *USE_AWS* with its value of *True*
    * *AWS_ACCESS_KEY_ID* with its custom value
    * *AWS_SECRET_ACCESS_KEY* with its custom value
    * *DATABASE_URL* with its custom value
    * *SECRET_KEY* with its custom value
    * *STRIPE_PUBLIC_KEY* with its custom value
    * *STRIPE_SECRET_KEY* with its custom value
    * *STRIPE_WH_SECRET* with its custom value
    * *HEROKU_POSTGRESQL_CRIMSON_URL* with its custom value
7. Go to your *Resources* tab and make sure you have *Heroku Postgres* either as a hobby dev or the paid options.
8. In your GitPod install the database url with the following command: `pip3 install dj_database_url`
9. Then, once that is installed, proceed to install the psycopg binary with the following command: `pip3 install psycopg2-binary`
10. Make sure you install and load all app requirements in GitPod with the following command: `pip3 freeze > requirements.txt`
11. In *settings.py* import dj_database_url at the top of the file and parse the temporary database settings.
12. Run migrations and create superuser for Heroku.
13. Remove the temporary database you set up previously and create an if statement in *settings.py* to run the postgres on Heroku.
14. Install the package called gunicorn with the following command: `pip3 install gunicorn`
15. Alternatively, if the package doesn't load properly, you can install Heroku functionality directly with the following command: `npm install -g heroku`
16. Create a Procfile and input the following content: `web: gunicorn fitness_den.wsgi:application`
17. In the *Config Vars* in Heroku temporarily input *DISABLE_COLLECTSTATIC* with the value of 1 to stop Heroku from collecting static files during initial deployment.
18. Add Heroku to your *ALLOWED_HOSTS* section in *settings.py*. Make sure to enable localhost as well.
19. Deploy directly to Heroku with the following command: `git push heroku main`
20. If you want Heroku to keep automatically updating the project you can set *'enable automatic deploys'* under the *'deployment method'* option.

### Amazon AWS S3

1. Open your browser and navigate to Amazon AWS.
2. Log in to an existing account or create a new one.
3. Create a new S3 bucket as well as "media" and "static" directories within the bucket itself.
4. Copy the details of your newly made bucket from the dashboard. You will need the following:
    * Storage Bucket Name
    * Storage Bucket Region Name
    * Access Key ID
    * Secret Access Key
5. You must then add the following settings to the env.py file to link directly to AWS:
    * os.environ["AWS_ACCESS_KEY_ID"] = `'your access key'`
    * os.environ["AWS_SECRET_ACCESS_KEY"] = `'your secret access key'`
6. Once that's done, you can go back to Heroku and add the keys and values from AWS and env.py to the config vars

### Stripe

1. Open your browser and navigate to Stripe.com.
2. Create a Stripe account or log into an existing one.
3. Ensure you click *"Developer Account"* to gain access to the API keys required to run the payment processes.
4. Once you have successfully created your Stripe account make sure you do the following:
    * Copy the Stripe Public Key, Stripe Secret Key and Stripe Webhook Key into your env.py file and into the Heroku Config Vars section.
5. Then, configure the *settings.py* file with the following variables required by Stripe:
    * `STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')`
    * `STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')`
    * `STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')`

## Credits

### Code and Assets

* *Code Institute* for the CI Full Template on GitHub
* *Code Institute* for the deployment terminal on Heroku
* *Code Institute* for *Boutique Ado*

### Media

* [Main Page Photo by Invictus at Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1300550)
* [Creatine, Whey and New Arrivals Pictures](https://evergreen.ie/)
* [Aminoacid and Deals Pictures](https://www.hollandandbarrett.ie/)
* [Equipment and Clearance Pictures](https://www.streetgains.eu/)