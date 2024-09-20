document.getElementById("encryptBtn").addEventListener("click", async function() {
    await processCipher("encrypt");
});

document.getElementById("decryptBtn").addEventListener("click", async function() {
    await processCipher("decrypt");
});

async function processCipher(action) {
    event.preventDefault(); 
    let formData = new FormData(document.getElementById("cipherForm")); 

    let url = "/" + action + "/"; 

    try {
       
        let response = await fetch(url, {
            method: "POST",
            body: formData
        });

        
        if (response.ok) {
            let result = await response.json();
            
            if (action === "encrypt") {
                document.getElementById("result").textContent = "Ciphertext: " + result.ciphertext;
            } else if (action === "decrypt") {
                document.getElementById("result").textContent = "Plaintext: " + result.plaintext;
            }
        } else {
            document.getElementById("result").textContent = "Error: Could not " + action + ".";
        }
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").textContent = "Error: " + error.message;
    }
}
