DATABASES = {

#look on geodjango tutorial and there's a specific things...
    'default': {
        'ENGINE' : 'django.contrib.gis.db.backends.postgis',
      #  'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'salary',
        'PORT': '5433',
        'HOST': '/tmp/',
    }
}
