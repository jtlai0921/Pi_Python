import cv2
from opencv import config
from opencv import face
from opencv import hardware

if __name__ == '__main__':
    print('Loading training data...')
    model = cv2.face.createEigenFaceRecognizer(config.COMPONENT_NUMBER, config.POSITIVE_THRESHOLD)
    model.load(config.TRAINING_FILE)
    print('Training data loaded!')
    camera = config.get_camera()
    box = hardware.Box()
    box.lock()
    print('Running box...')
    print('Press button to lock (if unlocked), or unlock if the correct face is detected.')
    print('Press Ctrl-C to quit.')

    while True:
        if box.is_button_up():
            if not box.is_locked:
                box.lock()
                print('Box is now locked.')
            else:
                print('Button pressed, looking for face...')
                box.starttest()
                image = camera.read()
                image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
                result = face.detect_single(image)
                box.endtest()
                if result is None:
                    print('Could not detect single face! Check the image in capture.pgm' \
                        ' to see what was captured and try again with only one face visible.')
                    continue
                x, y, w, h = result
                crop = face.resize(face.crop(image, x, y, w, h))
                label = model.predict(crop)
                if label == config.POSITIVE_LABEL:
                    print('Recognized face!')
                    box.unlock()
                else:
                    print('Did not recognize face!')
