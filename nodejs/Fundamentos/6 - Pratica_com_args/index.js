const minimist = require('minimist')

// Modulo externo
// const args = minimist(process.argv.slice(2))


// Modulo Interno
const soma = require('./soma').soma

const args = minimist(process.argv.slice(2))

const a = parseInt(args['a'])
const b = parseInt(args['b'])

soma(a, b)


