import cv2
import shutil
import os
import opencv
from tkinter import messagebox 
import sample2, adduser
def capt():
        face_dec=cv2.CascadeClassifier('face_model1.xml')
        smile_dec=cv2.CascadeClassifier('smile_model.xml')
        try:
            shutil.rmtree('data')
            os.rmdir('data')
            os.mkdir('data')
        except:
            os.mkdir('data')
        # define a video capture object
        vid = cv2.VideoCapture(0)
        currentframe=0
        pictures=[]
        while(True):

            # Capture the video frame
            # by frame
            ret, frame = vid.read()
            frame = cv2.flip(frame,1)
            if not ret:
                break
            gs_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces=face_dec.detectMultiScale(gs_frame)
            
            # print(faces)
            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (34, 250, 150),4)
                # print(x,y,w,h)
                the_face=frame[y:(y+h),x:(x+w)]
                # print(the_face)
                gs_the_face=cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

                smiles=smile_dec.detectMultiScale(gs_the_face,1.7,20)

                if len(smiles)>0:
                    cv2.putText(frame, "Smiling", (x,y+h+40), fontScale=2, fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))
                # for (x_,y_,w_,h_) in smiles:
                #     cv2.rectangle(the_face, (x_, y_), (x_+w_, y_+h_), (34, 30, 200),2)

            # Display the resulting frame
            cv2.imshow('frame', frame)
            # cv2.createButton('Click',lambda :click(frame),None,cv2.QT_PUSH_BUTTON,1)

            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice


            k=cv2.waitKey(1) &0xFF        
            if k==13:
                # print(currentframe)
                cv2.imshow('Captured Picture | Click s to save',frame)
                framee=frame
            elif k==113:
                break 
            elif k==115:
                name='data/capturedpicture.jpg'
                cv2.imwrite(name, framee)
                try:
                    a=sample2.search(name)
                    if a:
                        messagebox.showinfo("Attention", "Face already registered")
                        data0=''
                        vid.release()
                        cv2.destroyAllWindows()
                    else:
                        data0=name
                        pictures.append(name)
                        print(pictures)
                        vid.release()
                        cv2.destroyAllWindows()
                except opencv.fr.api_error.APIError:
                    data0=name
                    pictures.append(name)
                    adduser.Frame1.face=name
                    vid.release()
                    cv2.destroyAllWindows()
                    # self.fr3.destroy()
                    # obj=Frame4.Frame4(self.root)
                    # obj.create4()
            elif k==8:
                try:
                    # print('destroy')
                    cv2.destroyWindow('Captured Picture | Click s to save')
                    if len(pictures)>0:
                        os.remove(pictures[-1])
                        pictures.pop()
                except:
                    pass
            currentframe+=1
            # print(currentframe)
        # After the loop release the cap object
        vid.release()
        cv2.destroyAllWindows()
        return data0