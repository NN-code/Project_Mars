# Чтобы установить face-recognition (На Linux)
# 1) sudo apt-get install libboost-all-dev libgtk-3-dev build-essential cmake
# 2) pip install face-recognition

import face_recognition, os

def name_transformation():
    name = "Константин"
    name_length = len(name)
    result = (name_length * 100500) / 9022003
    with open("UltraTornado.txt", "w") as file:
        file.write("Жизни на Марсе нету - " + str(result))

def name_encryption():
    name = "Константин"
    result = list(name)
    counter = 0
    j = 0
    for i in name:
        if counter == 2:
            result[j] = "ШШ"
            counter = 0
        else:
            result[j] = i
            counter += 1
        j += 1
    result = ''.join(result)
    with open("SuperJobsDream.txt", "w") as file:
        file.write("Жизнь на марсе есть - " + result)

def face_rec(img_name):
    img = face_recognition.load_image_file(img_name)
    img = face_recognition.face_locations(img)

    print(img)
    print(f"Нашлось {len(img)} лиц(о) на фотографии ", img_name)
    return len(img)

def find_life():
    finds = 0
    dir_name = "mars_photos/"
    list = os.listdir(dir_name)
    for image in list:
        finds += face_rec(dir_name + image)
    if finds > 0:
        print("Жизнь на Марсе существует!")
        name_encryption()
    else:
        print("Жизни на Марсе не обнаружено")
        name_transformation()

def main():
    find_life()

if __name__ == '__main__':
    main()