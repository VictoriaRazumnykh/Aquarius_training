import json
import pytest


def pytest_addoption(parser):
    parser.addoption("--file", action="store", default="C:/Users/Mukhina-V/PycharmProjects/Aquarius_training"
                                                       "/json_files_in/target1.json1")
    parser.addoption("--id", action="store", default=1)


# 1. На вход через командную строку подаются два аргумента: конфигурационный файл и номер конфигурации в нем
# 2. Решение прочитывает конфигурацонный файл, находит в нем конфигурацию по номеру
@pytest.fixture
def load_file(request):
    config_id = int(request.config.getoption("--id"))
    my_file = request.config.getoption("--file")
    with open(my_file) as f:
        res = json.load(f)
    for i in res:
        if i.get("id") == config_id:
            res = i
    res.update({"config_file": my_file})
    return res
