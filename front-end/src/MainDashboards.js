countError = 0;
nextCount = 0;
idAuth = localStorage.getItem("id");
const header = new Headers();
header.append("id",idAuth)
const imgs = document.getElementById("img");
const img = document.querySelectorAll("#img img");
        
async function getImages(){
    for(i = 0; i < img.length; i++){
        try{
            routes = ["AgeWithBalance","AgeWithDuration","ClientsQuantityAge","AgeMarital","JobsQuantity","BalanceWithJob","AgeWithLoan","AgeWithHousing","ContactWithDuration","ContactWithAge","StatusCampaign","AgeWithDefault"]
            document.getElementById('load').style.visibility = "visible";
            document.getElementById("LoadLabel").innerHTML = `Carregando o gráfico número: ${i+1}`
            const response = await fetch(`http://localhost:5000/${routes[i]}`,{
                method: "GET",
                headers: header
            })

            const imageObj = await response.json()
            imageBytes = imageObj.image
            document.getElementById(`graph${i}`).src = "data:image/png;base64," +imageBytes;
            if (imageBytes == undefined){
                countError = countError+1
                document.getElementById("ErrorLabel").innerHTML = `Falha no carregamento do gráfico: ${i+1}`
                }
            }
            catch(error){
                countError = countError+1
                document.getElementById("ErrorLabel").innerHTML = `Falha no carregamento do gráfico: ${i+1}`
            }
            document.getElementById('load').style.visibility = "hidden";
            if(countError > 0){
                document.getElementById("LoadLabel").innerHTML = `Houve falhas no carregamento de ${countError} gráficos`
            }
            else{
                document.getElementById("LoadLabel").innerHTML = "Carregamento de gráficos compeltado com sucesso!"
                }
            }
    document.getElementById('ErrorLabel').style.visibility = "hidden";
}
getImages()
let idx = 0;

function carrossel(){
    idx++;
    if(idx > img.length - 1){
        idx = 0;
    }
    document.getElementById("GraphCount").innerHTML = `Gráfico número: ${idx+1}`
    imgs.style.transform = `translateX(${-idx*100}%)`; // * 100% é a largura que foi setada
}
        
function anterior(){
    idx = idx-1;
    if(idx < 0){
        idx = 0;
    }
    document.getElementById("GraphCount").innerHTML = `Gráfico número: ${idx+1}`
    imgs.style.transform = `translateX(${-idx*100}%)`;
}

function next(){
    carrossel()
}

function last(){
    anterior()
}

function back(){
    window.open("main.html")
    window.close()
}