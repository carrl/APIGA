APIGA
=====

	WEB API (python) 的 Google Analytics 追蹤程式

說明
----
	使用 python 來設計 WEB API (使用瀏覽器)
	當此 API 輸出的是 JSON 之類的資料時, 無法填入 Google Analytics 的追蹤程式碼 (javascript) 來做追蹤
	因此利用此程式 來讓 Google Analytics 可以追蹤 API 的使用記錄
	
作法
----
	將 gatrack.py 程式放到你的 API程式資料夾裡
	在你的 API 程式 加上
	-----------------------------------
	import gatrack

	gatrack.google_analytics_track(account="XX-XXXXXX-X", title="MY-TITLE")
	-----------------------------------
	以下兩個參數要自行輸入
	XX-XXXXXX-X: Google Analytics 追蹤代號
	MY-TITLE: 要在 Google Anaytics 報告裡顯示的抬頭

	PS: 請看範例 test.py

參考網站
----
	https://developers.google.com/analytics/resources/articles/gaTrackingTroubleshooting
	http://www.analyticsmarket.com/blog/__utmgif-data
