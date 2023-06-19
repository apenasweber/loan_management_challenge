// Função para enviar a proposta para o backend
function submitProposal() {
  // Obtém os valores dos campos do formulário
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const phone = document.getElementById("phone").value;
  const message = document.getElementById("message").value;

  // Cria um objeto com os dados da proposta
  const proposal = {
    name: name,
    email: email,
    phone: phone,
    message: message,
  };

  // Envia a proposta para o backend usando a API fetch
  fetch("/api/proposals/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(proposal),
  })
    .then((response) => {
      if (response.ok) {
        // Proposta enviada com sucesso
        alert("Proposta enviada com sucesso!");
        // Limpa os campos do formulário
        document.getElementById("name").value = "";
        document.getElementById("email").value = "";
        document.getElementById("phone").value = "";
        document.getElementById("message").value = "";
      } else {
        // Erro ao enviar a proposta
        alert("Erro ao enviar a proposta. Por favor, tente novamente.");
      }
    })
    .catch((error) => {
      console.error("Erro ao enviar a proposta:", error);
    });
}

// Captura o evento de envio do formulário
document
  .getElementById("proposalForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Evita o comportamento padrão de recarregar a página
    submitProposal(); // Envia a proposta para o backend
  });
