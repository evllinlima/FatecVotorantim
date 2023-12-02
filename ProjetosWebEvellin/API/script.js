elementoPesquisaClima = document.getElementById("pesquisaClima")
// Para função, abrir e fechar o parenteses. LEMBRE-SE: feche os parenteses principais após a ação do botão.
elementoPesquisaClima.addEventListener('click', async function () {
    cidade = document.getElementById("cidade").value;
    const apiClimaURL = `https://api.openweathermap.org/data/2.5/weather?q=${cidade}&units=metric&appid=${apiKey}&lang=pt_br`;
    let respostaClima = await fetch(apiClimaURL);
    let objDados = await respostaClima.json()
    temperatura = objDados.main.temp;
    descricao = objDados.weather[0].description
    document.getElementById('resultado').innerText = `Hoje está ${temperatura} e ${descricao}.`;
})

let elemento = document.getElementById("pesquisa");
//é preciso fechar o parenteses no final da função function. TODA FUNÇÃO TEM INICIO E FIM.
elemento.addEventListener('click', async function () {
    document.getElementById('resultado').innerText = ""
    //input é sempre .value 
    var valor = document.getElementById("cep").value
    if (valor == '')
        alert("Informe o CEP");
    else {
        //o replace substitui. /D retira os digitos e o /g é de forma global. REGEX É UMA EXPRESSÃO REGULAR, MUITO USADA PARA REGISTROS.
        var cep = valor.replace(/\D/g, '');
        var validacep = /^[0-9]{8}$/;

        if (validacep.test(cep)) {
            var api = 'https://viacep.com.br/ws/' + cep + '/json/';

            // await aguarda para dar o retorno da resposta. O FETCH é uma interface pronta para fazer requisições de forma assincrona.
            // promise é uma promessa de resposta. Ao fazer ua requisição é necessário dar uma resposta
            let resposta = await fetch(api);
            //dado seria o produto. Se não colocar o await em uma função assincrona irá dar erro.
            dados = await resposta.json();
            console.log(dados);
            if (dados.erro)
                document.getElementById('resultado').innerText = "CEP Não Existe";
            else { }
            document.getElementById('resultado').innerText = dados.logradouro + "" + dados.bairro + dados.localidade + dados.uf
            document.getElementById('cidade').value = dados.localidade
        }
        else

            //if (!(resposta.ok))
            alert("cep inválido");
    }
})

let apiKey = "4bb3dae061426448a0ee50e65dac5b65";

let bandeira = "//flagsapi.com/";
