let lampada = document.getElementById("lampada");
function ligar() {
    lampada.src = "luzLigada.gif";
};

function desligar() {
    lampada.setAttribute("src", "luzDesligada.gif");
};

function alternar() {
    if (lampada.getAttribute("src") == "luzLigada.gif") {
        desligar();
    }

    else if (lampada.getAttribute("src") == "luzDesligada.gif") {
        ligar();
    };
};

function sumir() {
    // lampada.hidden = True
    lampada.style.display = "none";
    document.getElementById("titulo").style.color = "red"
}
function aparecer() {
    // lampada.hidden = False
    lampada.style.display = "inline";
}

function piscar() {
    alternar()
}setInterval(piscar, 500)