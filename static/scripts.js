function sendMessage(event) {
  event.preventDefault();

  const inputElement = document.getElementById('user-message-input');
  const message = inputElement.value.trim();

  if (message !== '') {
    const chatMessagesElement = document.querySelector('.chat-messages');
    const userMessageElement = createMessageElement(message, 'user-message');
    chatMessagesElement.appendChild(userMessageElement);

    inputElement.value = '';

    // Enviar mensagem para o servidor Flask
    fetch('/sendMessage', {
      method: 'POST',
      body: new FormData(document.getElementById('message-form'))
    })
    .then(response => response.json())
    .then(data => {
      const botResponse = data.bot_response;
      if (botResponse) {
        const botMessageElement = createMessageElement(botResponse, 'bot-message');
        chatMessagesElement.appendChild(botMessageElement);
      }
    });
  }
}