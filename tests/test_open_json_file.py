import json
import os

# В случае режима dir - берем путь из параметра path и все файлы в этой директории. Можно считать, что файлов не много и они все текстовые, поддиректорий нет
# На верхнем уровне записать путь к файлу конфигурации, номер конфигурации, состав конфигурации,
# Далее список где на k-ом месте стоит список k-х строчек всех файлов поочереди. Есл в файле нет k-й строчки - то поле оставить пустым.

def test_open_json_file(load_file):
    res = {}
    configFile = load_file.get("config_file")
    configurationID = load_file.get("id")
    configurationPath = load_file.get("path")
    configurationMode = load_file.get("mode")
    configuratioData = {"mode": configurationMode, "path": configurationPath}
    if configurationMode == "dir":
        res.update({"configFile": configFile, "configurationID": configurationID, "configuratioData": configuratioData,
                    "out": "вв"})
        files = os.listdir(configurationPath)
        num_files = len(files)
        # записываем в массив out_list содержимое N необходимых строк по каждому файлу
        out_list = []
        for i in range(num_files):
            filepath = os.path.join(configurationPath, files[i])
            out = {}
            i_out_list = []
            # открываем i-й файл
            with open(filepath, 'r') as f:
                # считываем все строчки в файле
                lines = f.readlines()
                for k in range(num_files):
                    file_str = lines[k].rstrip()
                    i_out_list.append(file_str)
            out_list.append(i_out_list)

        # записываем в словарь out_dict содержимое N необходимых строк по k-й строке
        out_dict = {}
        # i - номер строки, k - номер файла
        for i in range(num_files):
            out_dict_i = {}
            for k in range(len(out_list)):
                # k+1 - номер файла начиная с 1, out_list[k][i] - значение в строке i
                out_dict_i[str(k + 1)] = out_list[k][i]
            out_dict[str(i + 1)] = out_dict_i
        res["out"] = out_dict
        print(res)

        with open("C:/Users/Mukhina-V/PycharmProjects/Aquarius_training/json_files_out/out_file.txt", "w", encoding="utf-8") as file:
            json.dump(res, file)
