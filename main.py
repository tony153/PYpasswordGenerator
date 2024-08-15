from random import choice
from string import ascii_lowercase,ascii_uppercase,digits,punctuation
import os.path

def read_config_file(filename):
    config = None
    if os.path.exists(filename):
        config = {}
        with open(filename, "r") as file:
            for line in file:
                key, value = line.strip().split(" = ")
                config[key] = value
    return config

def generate_unique_filename(base_filename):
    # 如果文件不存在，直接返回基本文件名
    if not os.path.exists(f"{base_filename}.txt"):
        return f"{base_filename}.txt"

    # 否則，添加括號和序號，直到找到一個不存在的文件名
    index = 1
    while True:
        new_filename = f"{base_filename}({index}).txt"
        if not os.path.exists(new_filename):
            return new_filename
        index += 1

def generate_password(length=32):
    lowercase = ascii_lowercase
    uppercase = ascii_uppercase

    all_characters = lowercase + uppercase + digits + punctuation
    password = "".join(choice(all_characters) for _ in range(length))
    return password


config_filename = "pwg.conf"
config_dict = read_config_file(config_filename)

# 設定基本文件名
base_filename = "New password"
# 設定基本密碼長度
pw_len = 32
if config_dict is not None:
    if "output_filename" in config_dict:
        base_filename = config_dict["output_filename"]
    if "password_length" in config_dict:
        pw_len = int(config_dict["password_length"])
        if pw_len < 12:
            pw_len = 12

unique_filename = generate_unique_filename(base_filename)

# 創建文件或打開現有文件
with open(unique_filename, "w") as file:
    # 寫入密碼或其他內容
    strong_password = generate_password(pw_len)
    file.write(strong_password)

print(f"已寫入文件：{unique_filename}")


