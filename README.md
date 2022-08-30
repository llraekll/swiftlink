
# R-Shortlinks
## Python 
![alt tag](https://github.com/llraekll/r-shortlinks/blob/main/images/python.png)

## Django
![alt tag](https://github.com/llraekll/r-shortlinks/blob/main/images/dj1.png)

## A python app built on the framework Django generates a short link/URL for every URL entered.
### The URL entered by the user is stored in the database, the app generates a URL unique 5-digit variable consisting numbers, uppercase letters and lowercase letters also redirects


# http://r-shortlinks.herokuapp.com/ 

![alt text](https://github.com/llraekll/r-shortlinks/blob/main/images/web.jpg?raw=True)

![alt tag](https://github.com/llraekll/FastAPI/blob/main/images/Heroku.png)
### Deploy on Heroku
WhiteNoise allows your web app to serve its own static files, making it a self-contained unit that can be deployed anywhere without relying on nginx, Amazon S3 or any other external service.
```bash
    pip install whitenoise
```
In settings settings.py add 

```bash
    MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
```
Want forever-cacheable files and compression support? Just add this to your settings.py:

```bash
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
``` 
In wsgi.py file add whitenoise as application

```bash
    import os
    from whitenoise import WhiteNoise

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'r_solutions.settings')

    application = get_wsgi_application()
    application = WhiteNoise(application)
```

* Create a Procfile mentioning the app’s web server
```bash
    web: gunicorn r_solutions.wsgi --log-file - 
```

* Create a requirements.txt file for Heroku to identify the language
* Ensure there are no unused libraries mentioned in the source code
* Add and commit source code, create a Heroku remote as mentioned on Heroku
* Deploy your code 

```bash
    git add --all
    git commit -am "comment"
    git push heroku main
```



