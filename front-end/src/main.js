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
    localStorage.setItem("id", undefined);
    window.close()

}