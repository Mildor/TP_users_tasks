# TP_users_tasks
### Tout d'abord créez un environnement virtuel : 
- sur linux : `virtualenv -p python3 ~/venv3`
- sur windows (avec anaconda) : `conda create -n myenv python=3.10 python`

### Activez votre environnement virtuel :
- sur linux : `source ~/venv3/bin/activate`
- sur windows (avec anaconda) : `conda activate myenv`

### Installez django : 
- `pip install django`

### Vérifiez l'installation de django:
- `django-admin --version`
> 4.1.1

### Installez crispy-forms:
- `pip install django-crispy-forms`

### Vérifier l'installation de cripsy-forms:
- `pip install django-crispy-forms`
> "Requirement already satisfied: django-crispy-forms in path_to_your_package (1.14.0)"


### Installez les modules npm/yarn:
- `npm/yarn install`

### Déplacez le répertoire node_modules dans le répertoire static

### Installez la bade de données :
- `./manage.py sqlmigrate lesTaches 0001`
- `./manage.py migrate`

### Créez un superuser afin d'accéder au backoffice :
- `./manage.py createsuperuser`
- **_Suivez les indications_ (vous pouvez ne pas mettre d'email en laissant la champ vide)**


### Lancez le projet :
- `./manage.py runserver`


### Pour pouvoir accéder au backoffice ajouter "admin" a l'url de base exemple:
- mon url de base "127.0.0.1:8000" accéder au backoffice : "127.0.0.1:8000/admin/"