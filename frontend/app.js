async function decode() {
    const manufacturer = document.getElementById("manufacturer").value;
    const serial = document.getElementById("serial").value;
    const resultDiv = document.getElementById("result");
  
    if (!manufacturer || !serial) {
      resultDiv.style.display = "block";
      resultDiv.className = "error";
      resultDiv.innerHTML = "<p>Please select a manufacturer and enter a serial number.</p>";
      return;
    }
  
    try {
      const res = await fetch(`http://127.0.0.1:8000/decode?manufacturer=${encodeURIComponent(manufacturer)}&serial=${encodeURIComponent(serial)}`);
      const data = await res.json();
  
      resultDiv.style.display = "block";
  
      if (res.ok) {
        resultDiv.className = "success";
        resultDiv.innerHTML = `<p>🗓 Manufacture Date: <strong>${data.result}</strong></p>`;
      } else {
        resultDiv.className = "error";
        resultDiv.innerHTML = `<p>Error: ${data.detail}</p>`;
      }
    } catch (err) {
      resultDiv.style.display = "block";
      resultDiv.className = "error";
      resultDiv.innerHTML = `<p>Network error. Is the backend running?</p>`;
    }
  }
  