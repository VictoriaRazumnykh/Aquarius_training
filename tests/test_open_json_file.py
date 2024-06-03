import json
import os
import random
import string


def create_list_of_each_file(files, configurationPath, configurationMode):
    # записываем в массив out_list содержимое N необходимых строк по каждому файлу
    out_list = []
    for i in range(len(files)):
        if configurationMode == "dir":
            filepath = os.path.join(configurationPath, files[i])
        elif configurationMode == "path":
            filepath = files[i]
        i_out_list = []
        # открываем i-й файл
        with open(filepath, 'r') as f:
            # считываем все строчки в файле
            lines = f.readlines()
            for k in range(len(files)):
                file_str = lines[k].rstrip()
                i_out_list.append(file_str)
        out_list.append(i_out_list)
    return out_list


def create_itog_file(files, out_list, res):
    # записываем в словарь out_dict содержимое N необходимых строк по k-й строке
    out_dict = {}
    # i - номер строки, k - номер файла
    for i in range(len(files)):
        out_dict_i = {}
        for k in range(len(out_list)):
            # k+1 - номер файла начиная с 1, out_list[k][i] - значение в строке i
            out_dict_i[str(k + 1)] = out_list[k][i]
        out_dict[str(i + 1)] = out_dict_i
    res["out"] = out_dict
    print(res)
    return res


# для записи в итоговый файл названия out_file + набор символов
def random_string(prefix, maxlen):
    symbols = string.ascii_letters * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def write_to_file(res):
    out_filepath = "C:/Users/Mukhina-V/PycharmProjects/Aquarius_training/json_files_out/" + random_string("out_file",
                                                                                                          10) + ".txt"
    with open(out_filepath, "w", encoding="utf-8") as file:
        json.dump(res, file)


# В случае режима dir - берем путь из параметра path и все файлы в этой директории. Можно считать, что файлов не много и они все текстовые, поддиректорий нет
# На верхнем уровне записать путь к файлу конфигурации, номер конфигурации, состав конфигурации,
# Далее список где на k-ом месте стоит список k-х строчек всех файлов поочереди. Есл в файле нет k-й строчки - то поле оставить пустым.

def test_open_json_file(load_file):
    res = {}
    configFile = load_file.get("config_file")
    configurationID = load_file.get("id")
    configurationPath = load_file.get("path")
    configurationMode = load_file.get("mode")
    configurationData = {"mode": configurationMode, "path": configurationPath}
    res.update(
        {"configFile": configFile, "configurationID": configurationID, "configurationData": configurationData})
    if configurationMode == "dir":
        files = os.listdir(configurationPath)

    elif configurationMode == "path":
        files = configurationPath

    out_list = create_list_of_each_file(files, configurationPath, configurationMode)
    res = create_itog_file(files, out_list, res)
    write_to_file(res)
