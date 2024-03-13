function generate_public_keys() {
    const q = parseInt(document.getElementById('primeinput').value);
    const a = parseInt(document.getElementById('proot').value);
    const xa = parseInt(document.getElementById('alice').value);
    const xb = parseInt(document.getElementById('bob').value);
    const ya = power(a, xa, q);
    const yb = power(a, xb, q);

    document.getElementById('ya').value = ya;
    document.getElementById('yb').value = yb;
}

function generate_shared() {
    const ya = parseInt(document.getElementById('ya').value);
    const xb = parseInt(document.getElementById('bob').value);
    const q = parseInt(document.getElementById('primeinput').value);

    const kab = power(ya, xb, q);

    document.getElementById('kab-alice').value = kab;
    document.getElementById('kab-bob').value = kab;
}

function power(a, b, c) {
    let result = 1;
    a = a % c;
    while (b > 0) {
        if (b % 2 == 1)
            result = (result * a) % c;
        b = Math.floor(b / 2);
        a = (a * a) % c;
    }
    return result;
}
