import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #讀取視訊鏡頭(此鏡頭編號為0)
mpHands = mp.solutions.hands #告訴電腦我們現在要使用的是手部模型
hands = mpHands.Hands() #呼叫函式
mpDraw = mp.solutions.drawing_utils

while True:
    ret,img=cap.read() #回傳前面兩個值
    if ret: #假如回傳的圖片沒有問題
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #將bgr轉換成rgb
        result = hands.process(imgRGB) #結果
        #print(result.multi_hand_landmarks) #回傳偵測到的每個手的21點座標
        if result.multi_hand_landmarks: #如果有偵測到手的話
            for handLms in result.multi_hand_landmarks:#用for迴圈去跑過偵測到的每一隻手
                mpDraw.draw_landmarks(img, handLms) #畫點
        
        cv2.imshow("Window",img) #顯示圖片的每一張每一貞
        
    if cv2.waitKey(1) == ord('q'):#一毫秒/若按下q則離開迴圈
        cv2.destroyAllWindows() #關掉視窗
        cap.release() #關掉攝影機
        break