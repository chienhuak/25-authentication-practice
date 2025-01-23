from fastapi import *
from fastapi.responses import JSONResponse
import bcrypt # 將密碼哈希處理
import jwt

app=FastAPI(debug=True)

fake_db = []
current_id = 1
# register_test_input = {
# 	"username": "john_doe",
# 	"password": "StrongP@ssw0rd"
# }


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
			"message": "User registered successfully.",
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



# 函數的內容，對密碼進行哈希處理並返回結果
def hash_password(password: str) -> str:
	# 生成鹽，並用bcrypt進行哈希
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # 返回加密後的密碼
    