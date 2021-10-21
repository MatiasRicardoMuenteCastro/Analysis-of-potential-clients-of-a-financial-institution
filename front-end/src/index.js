async function getLogin(){
    document.getElementById("error").innerHTML = ""

    UserName = document.querySelector("#IdUser").value;
    pass = document.querySelector("#IdPass").value;

        try{
            const response = await fetch('http://localhost:5000/session',{
            method:"POST",
            body:JSON.stringify({
                user: UserName,
                password: pass
            })
            })
            const login = await response.json()
            if (login.id != undefined && login.user != undefined){
                localStorage.setItem("id", login.id);

                window.open("/html/main.html")
                window.close()
            }
            else{
                document.getElementById("error").innerHTML = `Erro: ${login.error}`
            }
        }
        catch(error){
            document.getElementById("error").innerHTML = "Ocorreu um erro na autenticação da conta"
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

function getClickManagment(){
    window.open("AccountsManagment.html")
    window.close()
}

function getClickLogout(){
    window.open("/index.html")
    window.close()
}
