import face_recognition as fr


image = fr.load_image_file('./filename.jpg')
face_locations = fr.face_locations(image)

print(face_locations)