# django-grupy-jundiai

Palestra apresentada no Grupy Jundiai em Abril de 2019.

Era uma vez 2013...

https://github.com/rg3915/django

* Django==1.6.6

* Slides sem Form

img dr. strange

## Como o Django funciona?

https://raw.githubusercontent.com/rg3915/tutoriais/master/django-basic/img/mtv1.png

https://raw.githubusercontent.com/rg3915/tutoriais/master/django-basic/img/mtv2.png

https://raw.githubusercontent.com/rg3915/tutoriais/master/django-basic/img/diagrama.png


## Apresentar

### 1 - Admin - Login

login.png

```
<form action="/admin/login/?next=/admin/" method="post" id="login-form"><input type="hidden" name="csrfmiddlewaretoken" value="X9I8a87GjMYBWo5OBwHc5VjkIuOdkgjDZBIOCQnTFrxov9orGE7jyvxlDGZQTy1d">
  <div class="form-row">

    <label class="required" for="id_username">Usuário:</label> <input type="text" name="username" autofocus required id="id_username">
  </div>
  <div class="form-row">

    <label class="required" for="id_password">Senha:</label> <input type="password" name="password" required id="id_password">
    <input type="hidden" name="next" value="/admin/">
  </div>

  <div class="submit-row">
    <label>&nbsp;</label><input type="submit" value="Acessar">
  </div>
</form>
```

https://github.com/django/django/blob/master/django/contrib/admin/templates/admin/login.html#L44-L63



### 2 - [Building a form](https://docs.djangoproject.com/en/2.2/topics/forms/#building-a-form)

```
<form action="/your-name/" method="post">
    <label for="your_name">Your name: </label>
    <input id="your_name" type="text" name="your_name" value="{{ current_name }}">
    <input type="submit" value="OK">
</form>
```


### 3 - Admin - Auth User Add

auth_user_add.png

```
<form action="" method="post" id="user_form" novalidate>
    <input type="hidden" name="csrfmiddlewaretoken" value="3QsChOoIE6kzzQe9kEzoySfJ4fhjCAF0MglMTnnNWUAYqLij0O6qGTqieYQewK5n">
    <p>Primeiro, informe um nome de usuário e senha. Depois você será capaz de editar mais opções do usuário.</p>
    <div>
        <fieldset class="module aligned wide">
            <div class="form-row field-username">
                <div>
                    <label class="required" for="id_username">Usuário:</label>
                    <input type="text" name="username" class="vTextField" maxlength="150" autofocus required id="id_username">
                    <div class="help">Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.</div>
                </div>
            </div>
            <div class="form-row field-password1">
                <div>
                    <label class="required" for="id_password1">Senha:</label>
                    <input type="password" name="password1" required id="id_password1">
                    <div class="help"><ul><li>Sua senha não pode ser tão parecida com suas outras informações pessoais.</li><li>Sua senha precisa conter pelo menos 8 caracteres.</li><li>Sua senha não pode ser uma senha habitualmente utilizada.</li><li>Sua senha não pode ser inteiramente numérica.</li></ul></div>
                </div>
            </div>
            <div class="form-row field-password2">
                <div>
                    <label class="required" for="id_password2">Confirmação de senha:</label>
                    <input type="password" name="password2" required id="id_password2">
                    <div class="help">Informe a mesma senha informada anteriormente, para verificação.</div>
                </div>
            </div>
        </fieldset>
        <div class="submit-row">
            <input type="submit" value="Salvar" class="default" name="_save">
            <input type="submit" value="Salvar e adicionar outro(a)" name="_addanother">
            <input type="submit" value="Salvar e continuar editando" name="_continue">
        </div>
        <script type="text/javascript"
        id="django-admin-form-add-constants"
        src="/static/admin/js/change_form.js"
        data-model-name="user"
        >
        </script>
        <script type="text/javascript"
        id="django-admin-prepopulated-fields-constants"
        src="/static/admin/js/prepopulate_init.js"
        data-prepopulated-fields="[]">
        </script>
    </div>
</form>
```

Clean code

```
<form action="" method="post" id="user_form" novalidate>
    <input type="hidden" name="csrfmiddlewaretoken">
    <p></p>
    <div>
        <fieldset class="module aligned wide">
            <div class="form-row field-username">
                <div>
                    <label class="required" for="id_username">Usuário:</label>
                    <input type="text" name="username" class="vTextField" maxlength="150" autofocus required id="id_username">
                </div>
            </div>
            <div class="form-row field-password1">
                <div>
                    <label class="required" for="id_password1">Senha:</label>
                    <input type="password" name="password1" required id="id_password1">
                </div>
            </div>
            <div class="form-row field-password2">
                <div>
                    <label class="required" for="id_password2">Confirmação de senha:</label>
                    <input type="password" name="password2" required id="id_password2">
                </div>
            </div>
        </fieldset>
        <div class="submit-row">
            <input type="submit" value="Salvar" class="default" name="_save">
            <input type="submit" value="Salvar e adicionar outro(a)" name="_addanother">
            <input type="submit" value="Salvar e continuar editando" name="_continue">
        </div>
    </div>
</form>
```

https://github.com/django/django/blob/master/django/contrib/admin/templates/admin/change_form.html#L49-L51

https://github.com/django/django/blob/master/django/contrib/admin/templates/admin/includes/fieldset.html




### 4 - Admin - TabularInline

admin_tabular_inline.png



### 5 - Tela de Contato com forms.py

    * BandContactForm

```
{% load widget_tweaks %}

  <style>
    span.required:after {
      content: "*";
      color: red;
    }
  </style>

  <h1>Send e-mail</h1>
  <form class="form" method="POST">
    {% csrf_token %}
    {% for field in form.visible_fields %}
      <div class="form-group{% if field.errors %} has-error {% endif %}">
        <label for="{{ field.id_for_label }}">
          {% if field.field.required %}
            <span class="required">{{ field.label }} </span>
          {% else %}
            {{ field.label }}
          {% endif %}
        </label>
        {% render_field field class="form-control" %}
        {% for error in field.errors %}
          <span class="text-muted">{{ error }}</span>
        {% endfor %}
      </div>
    {% endfor %}
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
```


### 6 - `form.as_p`

```
<form class="form" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
```

Jinja

```
<form class="form" method="POST">
  <input type="hidden" name="csrfmiddlewaretoken" value="zoQhKvyhfA6wJjagdIFK4ofxsJfHAEgJbBu3QyaIMaFfXRYrPeaMdPDgRlqGUyPT">
  <p>
    <label for="id_subject">Subject:</label>
    <input type="text" name="subject" maxlength="100" required id="id_subject">
  </p>
  <p>
    <label for="id_message">Message:</label>
    <textarea name="message" cols="40" rows="10" required id="id_message"></textarea>
  </p>
  <p>
    <label for="id_sender">Sender:</label>
    <input type="email" name="sender" required id="id_sender">
  </p>
  <p>
    <label for="id_cc_myself">Cc myself:</label>
    <input type="checkbox" name="cc_myself" id="id_cc_myself">
  </p>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

Fazer ele pegar os valores na view

Segundo https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html#how-not-implement-a-form

este é o jeito errado de implementar um formulário

Perai... mas a doc... fala do template

https://docs.djangoproject.com/en/2.2/topics/forms/#building-a-form

```
#views.py
def my_send_email(request):
    email = request.POST
    import ipdb; ipdb.set_trace()
    subject = email.get('subject')
    message = email.get('message')
    sender = email.get('sender')
    cc_myself = email.get('cc_myself')
    # enviar email
    pass
```


### 7 - Live Code completo

https://raw.githubusercontent.com/rg3915/tutoriais/master/django-basic/img/diagrama.png

1. Criar url em urls.py
2. Criar função em views.py
3. Criar formulário em forms.py
4. Criar template

```
# urls.py
path('band/create/', v.band_create, name='band_create'),
```

```
# views.py
def band_create(request):
    ''' https://coderwall.com/p/o8tida/better-way-to-initialize-django-forms '''
    form = BandForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        # Process the data in form.cleaned_data
        form.save()
        return HttpResponseRedirect(resolve_url('bands'))
    return render(request, 'bands/band_create.html', {'form': form})
```

```
# forms.py
class BandForm(forms.ModelForm):

    class Meta:
        model = Band
        fields = '__all__'
```

```
# band_create.html
{% extends "base.html" %}

{% block title %}
  <title>Band Create</title>
{% endblock title %}

{% block content %}

  <h1>Band Create</h1>
  <form class="form" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>

{% endblock content %}
```


### 8 - `form.as_table`

```
<form class="form" method="POST">
    {% csrf_token %}
    {{ form.as_table }}
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
```

```
<form class="form" method="POST">
  <input type="hidden" name="csrfmiddlewaretoken" value="jKXg5XBxZoKCH8wJxDC8DDC48ofPUZrxVXB2b0dYwYjlVGkU997aM40Nx0qOeT0H">

  <tr>
    <th>
      <label for="id_subject">Subject:</label>
    </th>
    <td>
      <input type="text" name="subject" maxlength="100" required id="id_subject">
    </td>
  </tr>

  <tr>
    <th>
      <label for="id_message">Message:</label>
    </th>
    <td>
      <textarea name="message" cols="40" rows="10" required id="id_message">
      </textarea>
    </td>
  </tr>

  <tr>
    <th>
      <label for="id_sender">Sender:</label>
    </th>
    <td>
      <input type="email" name="sender" required id="id_sender">
    </td>
  </tr>

  <tr>
    <th>
      <label for="id_cc_myself">Cc myself:</label>
    </th>
    <td>
      <input type="checkbox" name="cc_myself" id="id_cc_myself">
    </td>
  </tr>

  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

https://simpleisbetterthancomplex.com/tag/forms/



### 9 - Manualmente

Mostrar https://docs.djangoproject.com/en/2.2/topics/forms/#rendering-fields-manually



### 10 - Creating Forms The Right Way

https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html#creating-forms-the-right-way

Usando forms.py

```
# forms.py
class BandContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
```

```
# views.py
def band_contact(request):
    """ A example of form """
    if request.method == 'POST':
        form = BandContactForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO: Implementar o send_email
            return redirect('home')
    else:
        form = BandContactForm()
    return render(request, 'bands/band_contact.html', {'form': form})
```


### 11 - django-widget-tweaks

```
pip install django-widget-tweaks==1.4.3
```

```
# settings.py
INSTALLED_APPS = [
    ...
    'widget_tweaks',
```

```
# band_contact.html
<form class="form" method="POST">
{% csrf_token %}

{% for field in form.visible_fields %}
    <label for="{{ field.id_for_label }}">{{ field.label }}</label>

    {% render_field field class="form-control" %}

{% endfor %}

<button type="submit" class="btn btn-primary">Submit</button>
</form>
```

### 12 - Setting arguments for widgets

Mostrar

https://docs.djangoproject.com/en/2.2/ref/forms/widgets/#setting-arguments-for-widgets



### 13 - Django Bootstrap

https://github.com/zostera/django-bootstrap4

```
pip install django-bootstrap4
```

```
# settings.py
INSTALLED_APPS = [
    ...
    'bootstrap4',
```

https://getbootstrap.com/

```
# base.html
<!-- Bootstrap core CSS -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css">

<!-- jQuery -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js"></script>

<!-- Bootstrap core JS -->
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"></script>
```

```
# band_contact_bootstrap.html
{% extends "base.html" %}
{% load bootstrap4 %}

{% block content %}

  <form class="form" method="POST">
    {% csrf_token %}

    {% bootstrap_form form %}

    {% buttons %}
        <button type="submit" class="btn btn-primary">Submit</button>
    {% endbuttons %}
  </form>

{% endblock content %}
```


### 14 - Django Crispy Forms

https://django-crispy-forms.readthedocs.io/en/latest/


```
pip install django-crispy-forms
```

https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html

```
# settings.py
INSTALLED_APPS = [
    ...
    'crispy_forms',
    ...
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
```

```
# band_contact_crispy.html
{% extends "base.html" %}
{% load crispy_forms_tags %}

{% block content %}

  <form class="form" method="POST">
    {% csrf_token %}

    {{ form|crispy }}

    <button type="submit" class="btn btn-primary">Submit</button>
  </form>

{% endblock content %}
```

### 15 - CreateView

https://ccbv.co.uk/projects/Django/2.1/django.views.generic.edit/CreateView/

```
class BandCreate(CreateView):
    model = Band
    form_class = BandForm
    template_name = 'bands/band_form.html'
    success_url = reverse_lazy('bands')
```


### 16 - UpdateView

https://ccbv.co.uk/projects/Django/2.1/django.views.generic.edit/UpdateView/


### 17 - Upload File

https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html

implementar
    one file
    multiple files


### 18 - inline_formset_factory

    pegar links + github



### 19 - django-registration-redux https://django-registration-redux.readthedocs.io/en/latest/

    registration https://i.stack.imgur.com/SgFlV.jpg
    login https://discuss.hellowebapp.com/uploads/default/original/1X/262249cf7d76163b5573bd325b3bd9674948ca8e.png
    reset password https://hellowebbooks.com/static/images/blog/2016/3/28/password-change-form.png

Implementar, se der tempo




### 20 - POST via Ajax

veganista/arrayToTable.js

https://gist.github.com/veganista/6413299

1. Requer jQuery
2. Criar uma tabela com arrayToTable.js
3. Alimentar essa tabela com dados vindos do banco (views.py)
4. Criar formulário num Modal
5. Criar uma url para fazer o Post
6. Criar View que salva os dados
7. Fazer o Post via Ajax
8. Retornar os novos dados na tabela



### 21 - POST com VueJS

    Implementar

