// 註冊
async function register() {

    const response = await fetch('http://127.0.0.1:8000/api/users/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
          },
        body: JSON.stringify({ 
          "username":test_input["username"], 
          "password":test_input["password"] 
          })
      })

      if (response.ok) {
        const result = await response.json()
        if(result.user)
          console.log(result.message)
        else
          console.log('註冊失敗')

      } else {
        const result = await response.json()
        console.log(result.message)
      }
}


// 登入驗證
async function signin() {

	const response = await fetch('http://127.0.0.1:8000/api/users/signin', {
		method: 'POST',
		headers: {
		  'Content-Type': 'application/json'
		  },
		body: JSON.stringify({ 
		  "username":test_input["username"], 
		  "password":test_input["password"] 
		  })
	  })
  
	  if (response.ok) {
		const result = await response.json()
		console.log(result) //糾錯
		if(result.token)
		  console.log(result.message)
		else
		  console.log('登入失敗或未返回 token')
  
	  } else {
		const result = await response.json()
		console.log(result.message)
	  }
  }



// 測試
const test_input = {
	"username": "john_doe",
	"password": "StrongP@ssw0rd"
}
register()
signin()