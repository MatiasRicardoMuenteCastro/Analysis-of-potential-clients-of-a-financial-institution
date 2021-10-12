async function getLogin(){
    UserName = document.querySelector("#IdUser").value;
    Password = document.querySelector("#IdPass").value;

    if (UserName == "admin" && Password == "root"){
        try{
            const response = await fetch('http://localhost:5000/Session',{method:"POST"})
            const token = await response.json()
            console.log(token.Token)
        }
        catch(error){
            console.log('Erro na geração do token')
        }
    }
    else{
        alert("Usuário ou senha incorretos")
    }
}