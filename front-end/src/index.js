async function getLogin(){
    UserName = document.querySelector("#IdUser").value;
    Password = document.querySelector("#IdPass").value;

    if (UserName == "admin" && Password == "root"){
        window.open("html/main.html")
        window.close()
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

function getClickMain(){
    window.open("MainDashboard.html")
    window.close()
}

function getClickSecundary(){
    window.open("SecundaryDashboard.html")
    window.close()
}

function getClickUpload(){
    window.open("Upload.html")
    window.close()
}

function getClickLogout(){
    window.open("/index.html")
    window.close()
}

function sendFile(){

}