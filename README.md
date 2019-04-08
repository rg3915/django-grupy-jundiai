# django-grupy-jundiai

Palestra apresentada no Grupy Jundiai em Abril de 2019.

Era uma vez 2013...

https://github.com/rg3915/django

* Django==1.6.6

* Slides sem Form

## Apresentar

### Admin - Login

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



[Building a form](https://docs.djangoproject.com/en/2.2/topics/forms/#building-a-form)

```
<form action="/your-name/" method="post">
    <label for="your_name">Your name: </label>
    <input id="your_name" type="text" name="your_name" value="{{ current_name }}">
    <input type="submit" value="OK">
</form>
```

### Admin - Auth User Add

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

Clear code

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


### Admin - TabularInline

admin_tabular_inline.png



### Tela de Contato com forms.py

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

### `form.as_p`

pegar codigo

### `form.as_table`

pegar codigo

Fazer ele pegar os valores na view

https://simpleisbetterthancomplex.com/tag/forms/

