import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# Создание вызова API и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:python' \
      '&sort=stars'

r = requests.get(url)
print("Status code: ", r.status_code)

# Сохранение ответа API в переменной.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Анализ информации о репозиториях.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
    }
    plot_dicts.append(plot_dict)

# Построение визуализации.
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 107333, 'label': 'Description of httpie.'},
    {'value': 85850, 'label': 'Description of django'},
    {'value': 66183, 'label': 'Description of flask.'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
