async function getLogin(){
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
                window.open("/html/main.html")
                window.close()
            }
            else{
                document.getElementById("error").innerHTML = `Erro: ${login.error}`
            }
        }
        catch(error){
            console.log('Erro na autenticação da conta')
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

function getClickLogout(){
    window.open("AccountsManagment.html")
    window.close()
}
