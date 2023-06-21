import face_recognition 
import os



images = []
directory  = os.fsencode("./images")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg"):
        images.append(filename)
        print(filename)
        continue
    else:
        continue


joeretz_image = face_recognition.load_image_file('./joeretz.jpg')
joeretz_face_encoding = face_recognition.face_encodings(joeretz_image)[0]




unknown_image = face_recognition.load_image_file(images[2])
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# compare images
results = face_recognition.compare_faces([joeretz_face_encoding],unknown_face_encoding)



if results[0]:
    print("match")
else:
    print("not match")
