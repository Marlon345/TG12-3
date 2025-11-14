document.getElementById("spielerForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // Seite soll nicht neu geladen werden
    alert("test");
    // Formulardaten sammeln
    const spieler = {
        name: document.getElementById("name").value,
        position: parseInt(document.getElementById("position").value),
        motivation: parseFloat(document.getElementById("motivation").value)
    };

    // Daten an den Server senden
    const response = await fetch("https://effective-invention-qrjj5vgj6vpfxp5-12345.app.github.dev/spieler", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(spieler)
    });

    // Antwort anzeigen
    const ergebnis = await response.json();
    document.getElementById("serverAntwort").textContent = JSON.stringify(ergebnis, null, 2);
});
//server public, machen richtigen "link" als referenz angeben und mit cors irgendrie java zugriff erlauben