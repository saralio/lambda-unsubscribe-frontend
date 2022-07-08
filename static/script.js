async function changeButtons(url) {
    var unsubscribeButton = document.getElementById("deregisterLink")
    var deregisterSuccessText = document.getElementById("deregisterSuccessText")
    var deregisterUnsuccessText = document.getElementById("deregisterUnSuccessfulText")

    const response = await fetch(url);

    if (response.ok) {
        unsubscribeButton.style.display = "none"
        deregisterSuccessText.style.display = "block"
        deregisterUnsuccessText.style.display = "none"
        return response.json();
    } else {
        unsubscribeButton.style.display = "none"
        deregisterSuccessText.style.display = "none"
        deregisterUnsuccessText.style.display = "block"
        const errorMessage = await response.text();
        throw new Error(errorMessage);
    }


}

async function handleFormSubmit(event) {
    event.preventDefault();

    const url = document.getElementById('deregisterLink').getAttribute('href')

    try {
        const responseData = await changeButtons(url);
        console.log({ responseData });
    } catch (error) {
        console.error(error);
    }
}

const unsubscribeEvent = document.getElementsByClassName('unsubscribe');
unsubscribeEvent.item(0).addEventListener("click", handleFormSubmit);