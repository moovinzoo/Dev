function isPrime(n) {
    for (let i = 2; i < n; i++) {
        if (n % i === 0) return false;
    }
    return true;
}

for (let i = 5; i <= 50; i++) {
    if (isPrime(i)) {
        document.write(`${i} is a prime number`);
        document.write("<br/>");
    }
}
