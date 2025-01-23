from fastapi import *
from fastapi.responses import JSONResponse
import bcrypt # 將密碼哈希處理
import jwt

app=FastAPI(debug=True)

fake_db = []
current_id = 1
# { "id": "1",
# 	"username": "john_doe",
# 	"password": "StrongP@ssw0rd"
# }


# 登入驗證
@app.post("/api/users/signin", response_class=JSONResponse)
async def signin(request: Request, data:dict):
	try:

		data = await request.json()  # 從 request body 中取得資料
		print(data)

		username = data["username"]
		pw = data["password"]


		for i in fake_db:
			if username == i["username"] and bcrypt.checkpw(pw.encode('utf-8'), i["password"].encode('utf-8')):

				print(f"登入成功: {username}")


				return JSONResponse(status_code=201, content={
					"message": "登入成功。",
					"token": "TBD"
				})
			else :
				print("登入失敗")
				return JSONResponse(status_code=201, content={
					"message": "登入失敗。",
					"token": "TBD"
				})

	except Exception as e:
		print("其他錯誤。")
		return JSONResponse(status_code=500, content={
				"error": True,
				"message": str(e)  
				# 出現 Exception，但前端拿到 null。
				# 原因：e 是一個例外物件（Exception），它無法直接被 JSON 序列化（即無法轉換為 JSON 格式），因此需將 e 轉換為字串。
				}) 


# 註冊
@app.post("/api/users/register", response_class=JSONResponse)
async def register(request: Request, data:dict):
	try:
		hashed_password = hash_password(data["password"])

		global current_id
		data["id"] = current_id

		fake_db.append({
			"id": data["id"],
			"username": data["username"],
			"password": hashed_password
		})
		current_id += 1
		print(fake_db)

		return JSONResponse(status_code=201, content={
			"message": "註冊成功。",
			"user": {
				"id": data["id"],
				"username": data["username"]
			}
		})

	except Exception as e:
		return JSONResponse(status_code=500, content={
				"error": True,
				"message": e
				}) 



# 對密碼進行哈希處理並返回結果的函數
def hash_password(password: str) -> str:
	# 生成鹽，並用bcrypt進行哈希
	salt = bcrypt.gensalt()
	hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
	return hashed_password.decode('utf-8')  # 返回加密後的密碼
	