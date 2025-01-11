async function calculateSum() {
    const values = [...document.querySelectorAll('td')].map(cell => parseFloat(cell.innerText) || 0);

    const response = await fetch('/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ function: 'SUM', values: values })
    });

    const result = await response.json();
    alert('SUM: ' + result.result);
}
