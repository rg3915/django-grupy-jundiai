# django-grupy-jundiai

Palestra apresentada no Grupy Jundiai em Abril de 2019.

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/django-grupy-jundiai.git
cd django-grupy-jundiai
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

## Slides

Esboço dos slides em https://github.com/rg3915/django-grupy-jundiai/blob/master/slides.md