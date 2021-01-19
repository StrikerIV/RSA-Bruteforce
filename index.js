let key = 4317
let modulus = 23701
let plaintext = "yessir"

let ciphertext = "19120, 3817, 5810, 5810, 5921, 5395"

async function encrypt(key, n, plaintext) {

    let splitPlaintext = plaintext.split("")
    splitPlaintext.forEach((char, index) => {
        console.log(char)
        console.log(index)
        char = plaintext.charCodeAt(index)
        console.log(char)
        console.log(parseInt(char) ** key)
    })
    console.log(splitPlaintext)

}

async function decrypt() {

}

console.log((121 ** key) % modulus)
encrypt(key, modulus, plaintext)