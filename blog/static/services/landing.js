async function logout() {

    alert(window.location.host);

        try {
            const response = await fetch("/login/");
            if (!response.ok) {
                throw new Error("Network response was not OK");
            }
            const todos = await response.json();
            console.log(todos);
        } catch (error) {
            console.error("There was a problem with your fetch request: ", error);
        }
}