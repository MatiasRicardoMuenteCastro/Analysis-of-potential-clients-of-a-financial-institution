async function getImage(){
    try{
        const response = await fetch('http://localhost:5000/BalanceWithServices')
        console.log(response)
        const data = await response.json()
        addImage(data)
    }
    catch(error){
        console.log('Erro na captação da imagem por API')
    }
}

getImage()

function addImage(ImageObj){
    imageBytes = ImageObj.image
    document.getElementById("graph1").src = "data:image/png;base64," +imageBytes;
}