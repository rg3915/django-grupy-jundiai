### 20 - POST via Ajax - FAIL

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


1. Requer jQuery

```html
# base.html
<script src="https://code.jquery.com/jquery-3.4.0.min.js"></script>
```

2. Criar uma tabela com arrayToTable.js - DEU RUIM

2.1 url - `path('members/', v.members, name='members'),`
2.2 url 
2.3 views

```python
# views.py
class MemberList(ListView):
    model = Member
    # template_name =
    # context_object_name =
    paginate_by = 10
```

2.4 member_list

```html
# member_list.html
{% extends "base.html" %}

{% block title %}
    <title>Member List</title>
{% endblock title %}

{% block content %}
    <h1>All Members</h1>
    <div id="my-table"></div>
{% endblock content %}

{% block js %}

  <script>

    var arrayToTable = function (data, options) {
      // https://gist.github.com/veganista/6413299
    };

  </script>

  <script>

    var data = [
      ['Name', 'Age', 'Email'],
      ['John Doe', '27', 'john@doe.com'],
      ['Jane Doe', '29', 'jane@doe.com']
    ];

    var table = arrayToTable(data, {
      thead: true,
      attrs: {class: 'table'}
    })

    $('#my-table').append(table);

  </script>
{% endblock js %}
```

3. Alimentar essa tabela com dados vindos do banco (views.py)

...