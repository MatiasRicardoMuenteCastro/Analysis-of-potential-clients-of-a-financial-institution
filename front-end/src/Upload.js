idAuth = localStorage.getItem("id");
const form = document.getElementById('myForm')
const inputFile = document.getElementById('fileSend')

form.addEventListener("submit", async e =>{
    document.getElementById("statusServer").innerHTML = ""
    document.getElementById("status").innerHTML = ""
    document.getElementById('load').style.visibility = "visible";
    document.getElementById("LoadLabel").innerHTML = "Fazendo o upload do dataset..."
    e.preventDefault()

    const header = new Headers()
    const formData = new FormData()
    
    formData.append("excel", fileSend.files[0])
    header.append("id",idAuth)

    url = "http://localhost:5000/Upload"

    try{
    const response = await fetch(url,{
        method: "post",
        headers: header,
        body: formData
    })

        let result = await response.json()

        if (result.sucess == "Upload feito com sucesso"){
            document.getElementById("status").innerHTML = "Sucesso: "+result.sucess;
            document.getElementsByTagName("style")[0].innerHTML += "#status{color: green; margin-top: -15px}"
        }
        else if (result.error != ""){
            document.getElementById("status").innerHTML = "Erro: "+result.error;
            document.getElementsByTagName("style")[0].innerHTML += "#status{color: red; margin-top: -15px}"
        }
    }catch{
        document.getElementById("statusServer").innerHTML = 'O servidor está offline'
        document.getElementsByTagName("style")[0].innerHTML += "#statusServer{color: red}"
        document.getElementById('load').style.visibility = "hidden";
        document.getElementById("LoadLabel").innerHTML = ""
    }
    document.getElementById('load').style.visibility = "hidden";
    document.getElementById("LoadLabel").innerHTML = ""
})

async function buttonMine(){
    document.getElementById("statusServer").innerHTML = ""
    document.getElementById("statusMine").innerHTML = ""
    document.getElementById('load').style.visibility = "visible";
    document.getElementById("LoadLabel").innerHTML = "Fazendo a mineração de dados do dataset..."
    const header = new Headers()
    header.append("id",idAuth)
    try{
    const response = await fetch('http://localhost:5000/Data_Mining',{
        method:"PUT",
        headers:header
    
    })
    let result = await response.json()

    if (result.sucess == "A mineração de dados foi concluida"){
        document.getElementById("statusMine").innerHTML = "Sucesso: "+result.sucess;
        document.getElementsByTagName("style")[0].innerHTML += "#statusMine{color: green; margin-top: -15px}"
    }
    else if (result.error == "Por favor faça o upload de um dataset compátivel com o modelo de mineração"){
        document.getElementById("statusMine").innerHTML = "Error: "+result.error;
        document.getElementsByTagName("style")[0].innerHTML += "#statusMine{color: red; margin-top: -15px}"
    }
    }catch{
        document.getElementById("statusServer").innerHTML = 'O servidor está offline'
        document.getElementsByTagName("style")[0].innerHTML += "#statusServer{color: red}"
        document.getElementById('load').style.visibility = "hidden";
        document.getElementById("LoadLabel").innerHTML = ""
    }
    document.getElementById('load').style.visibility = "hidden";
    document.getElementById("LoadLabel").innerHTML = ""
}

function back(){
    window.open("main.html")
    window.close()
}