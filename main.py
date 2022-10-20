import eel;
import qrcode;
from hashing import hashing, string_randomizer, alphabet_list, alphabet_list_upper;
from PIL import Image;



eel.init("web")

def image_opener(image):
    im = Image.open(r"./" + image)
    im.show()



@eel.expose
def message_returner(test):
    if(len(test) > 0):
        return "Qr code saved successfully!"
    else:
        return "Please type something to input!"
                



@eel.expose
def get_element(str):
    if(len(str) > 0):
        img = qrcode.make(str)
        hash_number = hashing()
        hash_string = string_randomizer(alphabet_list, alphabet_list_upper)
        fileName = "image" + hash_number + hash_string + ".png"
        img.save(fileName)
        image_opener(fileName)
    else:
        return



eel.start("index.html", size = (400, 300))