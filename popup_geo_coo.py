import tkinter as tk
import get_geo_coo  # type: ignore # geo_coo.py 파일을 불러옴

def on_confirm_click():
    address = entry.get()  # 입력된 주소 가져오기
    latitude, longitude = get_geo_coo.get_geo_coo(address)

    if latitude is not None and longitude is not None:
        print(f"위도: {latitude}, 경도: {longitude}")
        popup.destroy()  # 팝업 창 닫기
    else:
        print("위도와 경도를 가져올 수 없습니다.")

# 팝업 창 생성
popup = tk.Tk()
popup.title("주소 입력")

# 주소 입력란 생성
label = tk.Label(popup, text="주소를 입력하세요:")
label.pack()
entry = tk.Entry(popup)
entry.pack()

# 확인 버튼 생성
button = tk.Button(popup, text="확인", command=on_confirm_click)
button.pack()

# 팝업 창 실행
popup.mainloop()
