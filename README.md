# TP_users_tasks

### Clonez le projet sur votre poste :
- `git clone https://github.com/Mildor/TP_users_tasks.git`

### Placez vous dans la racine du projet :
- `cd /VotreChemin/TP_users_tasks/`

### Créez un environnement virtuel : 
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

### Installez selenium
- `pip install selenium`

### Vérifier l'installation de selenium:
- `pip install selenium`
> "Requirement already satisfied"

## Vérifiez que vous vous trouvez bien dans la racine du projet
>/VotreChemin/TP_users_tasks/

### Installez les packages npm/yarn:
- `npm/yarn install`

### Installez la bade de données :
- `./manage.py sqlmigrate lesTaches 0001`
- `./manage.py migrate`

### Lancez le projet :
- `./manage.py runserver`
