idAuth = sessionStorage.getItem("id");
const header = new Headers()
header.append("id",idAuth)
count = 0
UserID = null
countSelect = 0
LastIdButton = null

async function getUsers(){
    try{
    const response = await fetch(`http://localhost:5000/users`,{
        method: "GET",
        headers: header
    })
    const usuarios = await response.json()
        ArrayUsers = usuarios.usuarios
        if (usuarios.usuarios != undefined){
            for (users of ArrayUsers){
                count = count+1
                document.getElementById("tbody").innerHTML += `<tr id = "u${count}" onclick = "selectDelete(this)"><td id = "u${count}ID" >${users[0]}</td> <td>${users[1]}</td> </tr>`
        }
        }else{
            document.getElementById("error").innerHTML = `${usuarios.error}`
            document.getElementsByTagName("style")[0].innerHTML += "#error{color: red}"
        }
    }
    catch(error){
        document.getElementById("error").innerHTML = "Error na comunicação com o servidor"
        document.getElementsByTagName("style")[0].innerHTML += "#error{color: red}"
    }
}

getUsers()

function refreshTable(){
    document.getElementById("tbody").innerHTML = ""
    document.getElementById("error").innerHTML = "Status da operação"
    document.getElementsByTagName("style")[0].innerHTML += "#error{color: white}"
    LastIdButton = null
    UserID = null
    countSelect = 0
    getUsers()
}

async function insertUser(){
    document.getElementById("error").innerHTML = "Status da operação"
    document.getElementsByTagName("style")[0].innerHTML += "#error{color: white}"

    user = document.getElementById("user").value
    password = document.getElementById("password").value

    count = count+1

    try{
        const response = await fetch('http://localhost:5000/user/create',{
        method:"POST",
        headers: header,
        body:JSON.stringify({
            user: user,
            password: password
        })
    })
        const login = await response.json()
        if (login.id != undefined && login.user != undefined){
            document.getElementById("tbody").innerHTML += `<tr id = "u${count}" onclick = "selectDelete(this)"><td id = "u${count}ID" >${login.id}</td> <td>${login.user}</td> </tr>`
            document.getElementById("error").innerHTML = "O usuário foi cadastrado com sucesso!"
            document.getElementsByTagName("style")[0].innerHTML += "#error{color: green}"
        }
        else{
            document.getElementById("error").innerHTML = "Error: "+ login.error
            document.getElementsByTagName("style")[0].innerHTML += "#error{color: red}"
        }
    }
    catch{
        document.getElementById("error").innerHTML = "Error na comunicação com o servidor"
        document.getElementsByTagName("style")[0].innerHTML += "#error{color: red}"
    }
}

function selectDelete(idButton){
    document.getElementById("error").innerHTML = "Status da operação"
    document.getElementsByTagName("style")[0].innerHTML = ""
    countSelect = countSelect+1
    if (countSelect <= 1){
        VarIdButton = idButton.id
        UserIDPosition = VarIdButton+"ID"
        UserID = document.getElementById(UserIDPosition).innerHTML
        document.getElementsByTagName("style")[0].innerHTML += `table #${VarIdButton}{background-color: rgba(0, 0, 0, 0.815);}`
    }
    else if(countSelect > 1){
        document.getElementsByTagName("style")[0].innerHTML = ""
        LastIdButton = null
        UserID = null
        countSelect = 0
    }
}

async function Delete(){
    document.getElementById("error").innerHTML = "Status da operação"
    document.getElementsByTagName("style")[0].innerHTML += "#error{color: white}"

    countSelect = 0
    document.getElementsByTagName("style")[0].innerHTML = ''
    try{
        const response = await fetch('http://localhost:5000/user/delete',{
            method:"DELETE",
            headers: header,
            body:JSON.stringify({
                user_id: UserID
            })
        })
            const deleteRes = await response.json()
        
            if(deleteRes.sucess != undefined){
                document.getElementById("error").innerHTML = deleteRes.sucess
                document.getElementsByTagName("style")[0].innerHTML += "#error{color: green}"
            }
            else{
                document.getElementById("error").innerHTML = "Error: "+ deleteRes.error
                document.getElementsByTagName("style")[0].innerHTML += "#error{color: red}"
            }
    }
    catch{
        document.getElementById("error").innerHTML = "Error na comunicação com o servidor"
        document.getElementsByTagName("style")[0].innerHTML += "#error{color: red}"
    }
}

function back(){
    window.open("main.html")
    window.close()
}
