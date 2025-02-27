from utils.dep_file_search import dep_search
from utils.get_file_imports import get_imports
import json
import os


def dependency_check(file_to_check ,folder_path): 
    if file_to_check.endswith(".py"):
          file_to_check = file_to_check.replace(".py","")
    all_file_path = []
    all_files = []
    for (dirpath,dirnames, filenames) in os.walk(folder_path):
                for file in filenames:
                    if file.endswith(".py"):
                        all_files.append(file)  
                        file_path = os.path.join(dirpath, file)
                        file = file.replace(".py","")
                        all_file_path.append({"file_name":file,"file_path":file_path})
    file_name_imports = get_imports(all_file_path)
    result =  dep_search(file_to_check,file_name_imports)
    imp_list = result[0]
    tupled_dep = result[1]
    file_to_check_info = [
    {"file_name": item["file_name"], "file_path": item["file_path"]}
    for item in all_file_path if item["file_name"] == file_to_check]
    if file_to_check_info:
          file_to_check_info = file_to_check_info[0]
    else:
         None
    dependencies = [
    {"file_name": item["file_name"], "file_path": item["file_path"]}
    for item in all_file_path if item["file_name"] in imp_list]
    imp_list_json = json.dumps({"file_to_check": file_to_check_info,"dependencies": dependencies}, indent=4)
    with open(f"{file_to_check}_dependencies.json", "w") as outfile:
        outfile.write(imp_list_json)
    print(f"imp_list_json:{imp_list_json}")
    return imp_list_json



