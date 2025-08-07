import cv2
import numpy as np

# カメラを起動 (0は内蔵カメラを意味します)
cap = cv2.VideoCapture(0)

# 最初のフレームを背景として取得するための準備
# 少し待ってから背景を取得すると、カメラの明るさ調整が安定します
for i in range(60):
    ret, frame = cap.read()
    if not ret:
        cap.release()
        print("エラー: カメラを起動できませんでした。")
        exit()

# 最初のフレームをグレースケールに変換して背景として設定
ret, frame = cap.read()
if not ret:
    cap.release()
    print("エラー: フレームをキャプチャできませんでした。")
    exit()

bg_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
bg_gray = cv2.GaussianBlur(bg_gray, (21, 21), 0) # ノイズを減らすためのぼかし処理

print("動体検出を開始します。'q'キーを押すと終了します。")

while True:
    # 現在のフレームを読み込む
    ret, frame = cap.read()
    if not ret:
        break # ビデオの終わりか、エラー

    # 現在のフレームも同様に処理
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # 背景との差分を計算
    frame_delta = cv2.absdiff(bg_gray, gray)

    # 差分画像を白黒（2値化）にする
    # 閾値(thresh)より大きい差分を白(255)に、それ以外を黒(0)にする
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

    # 輪郭を見つける
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 輪郭を一つずつ処理
    for contour in contours:
        # 小さすぎる輪郭はノイズなので無視する
        if cv2.contourArea(contour) < 500:
            continue

        # 輪郭を囲む四角形（バウンディングボックス）を取得
        (x, y, w, h) = cv2.boundingRect(contour)
        # 元のフレームに緑色の四角形を描画
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 結果のウィンドウを表示
    cv2.imshow("Motion Detector", frame)

    # 'q'キーが押されたらループを抜ける
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 後処理
print("プログラムを終了します。")
cap.release() # カメラを解放
cv2.destroyAllWindows() # すべてのウィンドウを閉じる
