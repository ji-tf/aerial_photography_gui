import jinja2

name_object = 'werty'
filming_location = 'werty'
executor = 'werty'
aircraft = 'aasdfgh' # Воздушное судно"))
add_information = 'a809990fgh' # Дополнительные сведения по требованию ТЗ

fields = [
            {"name_object": name_object,  "filming_location": filming_location, "executor": executor,
            "aircraft": aircraft, "add_information": add_information}
        ]

        # Загрузка шаблона из файла
template_path = "template_table.html"
loader = jinja2.FileSystemLoader(searchpath="templates")
environment = jinja2.Environment(loader=loader)
template = environment.get_template(template_path)

        # Рендеринг шаблона для каждого набора данных
for field in fields:
    filename = f"tableAP111.html"
    content = template.render(field=field)

            # Сохранение отрендеренного шаблона в файл
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {filename}")
