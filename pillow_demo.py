from PIL import Image


im_file = "Timetable_7th_Sem.jpeg"

im = Image.open(im_file)

im.show()
print(im.size)