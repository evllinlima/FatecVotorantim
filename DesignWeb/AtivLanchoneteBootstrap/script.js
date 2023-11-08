let totalPedido = 0;
let totalAdicionais = 0;
let totalEntrega;

function calcularTotalPedido() {
    let combo = Number(document.getElementById("combos").value);
    calcularAdicionais();
    calcularEntrega();
    totalPedido = combo + totalAdicionais + totalEntrega;
    // para chamar uma variável dentro de um texto é utilizado ${}. Só irá funcionar se estiver entre crases ``.. O innerHTML e o innerText serão usados para escrever 
    document.getElementById("totalPagar").innerHTML = `O total que será pago é R$${totalPedido}!`;
    document.getElementById("DescPedido").innerHTML = `Seu combo custará R$${combo} com R$${totalAdicionais} de adicionais e R$${totalEntrega} de taxa de entrega!`

    console.log(combo);
    console.log(totalAdicionais);
    console.log(totalEntrega);
    console.log(totalPedido)
}

function calcularAdicionais() {
    totalAdicionais = 0;
    let adicionais = document.querySelectorAll("input[name='adicionais']");
    for (let i = 0; i < adicionais.length; i++) {
        if (adicionais[i].checked) {
            totalAdicionais = totalAdicionais + Number(adicionais[i].value);
        }
    }
}

function calcularEntrega() {
    let entrega = document.querySelectorAll("input[name='entrega']");

    // i < pacotes.length como outra opção para verificar a var.
    for (var i = 0; i < entrega.length; i++) {
        if (entrega[i].checked) {
            totalEntrega = Number(entrega[i].value);
            break;
        }
    }
}


