txt = input('Ingrese una cadena de caracteres: ')


def extract_info_string(string):
    string = string.split(' ')
    tmp_dict = {}
    for item in string:
        if item in tmp_dict:
            tmp_dict[item]+=1
        else:
            tmp_dict[item]=1
    sorted_result = sorted(tmp_dict.items(), key=lambda x:x[1],reverse=True)
    return sorted_result

extract_info_string(txt)