async function handleFormSubmit(event) {
    event.preventDefault();

    var unsubscribeButton = document.getElementById("deregisterLink");
    var deregisterSuccessText = document.getElementById("deregisterSuccessText");
    var deregisterUnsuccessText = document.getElementById("deregisterUnSuccessfulText");
    let baseUrl = document.getElementById('deregisterLink').getAttribute('href');
    let emailId = document.getElementById('emailId').value;
    let suggestion = document.getElementById('deregisterSuggestion').value;
    let url = suggestion == '' ? baseUrl + 'emailId=' + emailId : baseUrl + 'emailId=' + emailId + '&suggestion=' + suggestion;

    try {
        var response = await fetch(url);
    } catch (error) {
        console.error(error);
        var response = {ok: false, text: error} 
    }

    if (response.ok) {
        unsubscribeButton.style.display = "none"
        deregisterSuccessText.style.display = "block"
        deregisterUnsuccessText.style.display = "none"
        return response.json();
    } else {
        unsubscribeButton.style.display = "none"
        deregisterSuccessText.style.display = "none"
        deregisterUnsuccessText.style.display = "block"
        const errorMessage = response.text;
        throw new Error(errorMessage);
    }

}

const unsubscribeEvent = document.getElementsByClassName('unsubscribe');
unsubscribeEvent.item(0).addEventListener("click", handleFormSubmit);