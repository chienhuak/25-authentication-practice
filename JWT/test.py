from fastapi import *
from fastapi.responses import JSONResponse
import jwt

app=FastAPI(debug=True)

fake_db = []
# register_test_input = {
# 	"username": "john_doe",
# 	"password": "StrongP@ssw0rd"
# }


# 註冊
@app.post("/api/users/register", response_class=JSONResponse)
async def register(request: Request, data:dict):
	try:
		fake_db.append(data)
		print(fake_db)

		return JSONResponse(status_code=201, content={
			"message": "User registered successfully.",
			"user": {
				"id": 1,
				"username": data["username"]
			}
		})

	except Exception as e:
		return JSONResponse(status_code=500, content={
				"error": True,
				"message": e
				}) 