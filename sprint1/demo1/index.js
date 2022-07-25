// Comentário

/*
    Funções
*/


// function greetings(){
//     return 'olá M5'
// }

// console.log(typeof greetings)
// console.log(greetings())


/*
    Tipos Primitivos
*/

// // Inteiro
// const num = 10
// console.log(num)
// console.log(typeof num)

// // Float
// let f_num = 5.2
// console.log(f_num)
// console.log(typeof f_num)

// // String
// const string = "uma string"
// console.log(string)
// console.log(typeof string)

// // Boleano
// const boolean = true
// console.log(string)
// console.log(typeof string)


// Tipagem fraca
// console.log(1 + '1')

// /*
//     Estruturas Condicionais
// */


// let x = 5

// if (x > 5){
//     console.log("x é maior que 5")
// } else if (x == 5){
//     console.log("x é igual a 5")
// } else {
//     console.log("x é menor que 5")
// }

// let y = 10

// if (x == 5 && y == 10){
//     console.log('x = 5 E y = 10')
// }

// if (x == 5 || y == 10){
//     console.log('x = 5 OU y = 10')
// }

// if (!(x == 20)){
//     console.log('x NÃO é 20')
// }

// /*
//     Estruturas de Repetição
// */

let my_str = 'olá M5!'

for (let x of my_str){
    console.log(x)
}

for (let i = 0; i < my_str.length; i++){
    console.log(i, my_str[i])
}

for (let i = 0; i < 10; i++){
    console.log(i)
}

for (let i = 0; i < 10; i++){
    console.log(i)
    if (i == 3){
        break
    }
}

let z = 0

while (z < 3){
    console.log('loop while', z)
    z++
}

