let valorPacote = 0;
let totalAdicionais;

function calcularTotalViagem() {
    calcularPacote();
    calcularAdicionais();
    console.log(totalAdicionais)
}

function calcularAdicionais() {
    totalAdicionais = 0;
    let adicionais = document.querySelectorAll("input[name='adicionais']");
    console.log(adicionais);
    for (let i = 0; i < adicionais.length; i++) {
        if (adicionais[i].checked) {
            console.log(adicionais[i].value)
            totalAdicionais = totalAdicionais + Number(adicionais[i].value);
            document.getElementById
        }
    }
}

function calcularPacote() {
    let qtdPacotes = document.querySelectorAll("input[name='pacotes']").length;
    console.log(qtdPacotes);
    let pacotes = document.querySelectorAll("input[name='pacotes']");
    console.log(pacotes);

    // i < pacotes.length como outra opção para verificar a var.
    for (var i = 0; i < qtdPacotes; i++) {
        if (pacotes[i].checked) {
            console.log(pacotes[i].value);
            valorPacote = pacotes[i].value;
            break;

        }
    }
}

