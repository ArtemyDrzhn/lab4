import json

path_json_out = r"D:\Study\University\Sem 7\КПРС ПО\Лабораторные\4\response.json"

path_json_in = r"D:\Study\University\Sem 7\КПРС ПО\Лабораторные\4\request.json"


# Чтение данных с текстового файла
def open_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()


# Чтение данных с json файла
def read_json(filename_json):
    with open(filename_json) as json_file:
        return json.load(json_file)


# Поиск слов в текстовом файле
def search_words():
    json_obj = read_json(path_json_in)
    s = json_obj["file name"]
    s = "D:/Study/University/Sem 7/КПРС ПО/Лабораторные/4/" + s
    file_read = open_file(s)

    paragraph = []

    for str_read in file_read:
        if json_obj["example minimum length"] <= len(str_read) <= json_obj["example maximum length"]:
            fl_search = True
            for words in json_obj["words"]:
                if words not in str_read:
                    fl_search = False
                    break
            if fl_search:
                paragraph.append(str_read)
        if len(paragraph) == json_obj["number of examples"]:
            break

    # Запись в файл
    with open(path_json_out, 'w') as json_file:
        if len(paragraph) != 0:
            cnt = 1
            data = {}
            for str_s in paragraph:
                data[cnt] = str_s
                cnt += 1
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        else:
            json.dump({"Result": "The search failed"}, json_file, indent=4)


search_words()
