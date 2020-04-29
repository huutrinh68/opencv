import cv2


def main(mirror=True, size=None):
    fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
    # read webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        # read image from camera
        ret, frame = cap.read()

        # blur
        frame = cv2.GaussianBlur(frame, (5, 5), 3)

        # apply background subtraction
        fgmask = fgbg.apply(frame)

        # settin window
        cv2.namedWindow("ManabiTV", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("ManabiTV", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('ManabiTV', fgmask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
