// 註冊
async function register() {

    const response = await fetch('http://127.0.0.1:8000/api/users/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
          },
        body: JSON.stringify({ 
          "username":test_register_input["username"], 
          "password":test_register_input["password"] 
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


const test_register_input = {
	"username": "john_doe",
	"password": "StrongP@ssw0rd"
}
register()