const formulario = document.getElementById("form-funcionario");
const mensagem = document.getElementById("mensagem");

formulario.addEventListener("submit", async function(evento) {
    evento.preventDefault();

    mensagem.textContent = "";

    const funcionario = {
        nome: document.getElementById("nome").value,
        cpf: document.getElementById("cpf").value,
        email: document.getElementById("email").value,
        data_nascimento: document.getElementById("data_nascimento").value,
        telefone: document.getElementById("telefone").value
    };

    try {
        const resposta = await fetch("/funcionarios", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(funcionario)
        });

        const resultado = await resposta.json();

        if (resposta.ok) {
            mensagem.textContent = "Funcionário cadastrado com sucesso!";
            formulario.reset();
            console.log("Funcionário cadastrado:", resultado);
        } else {
            mensagem.textContent = "Erro ao cadastrar funcionário: " + (resultado.detail || "Dados inválidos.");
            console.error("Erro da API:", resultado);
        }

    } catch (erro) {
        mensagem.textContent = "Não foi possível conectar ao servidor.";
        console.error("Erro de conexão:", erro);
    }
});